"""worker_example.py
Simple example worker (Python) that consumes Redis queue, queries MySQL and logs to MongoDB.

Requirements:
pip install redis pymysql pymongo
"""

import redis
import pymysql
from pymongo import MongoClient
import time
import os

REDIS_HOST = os.getenv('REDIS_HOST','127.0.0.1')
REDIS_PORT = int(os.getenv('REDIS_PORT',6379))

MYSQL_HOST = os.getenv('MYSQL_HOST','127.0.0.1')
MYSQL_PORT = int(os.getenv('MYSQL_PORT',3306))
MYSQL_USER = os.getenv('MYSQL_USER','root')
MYSQL_PASS = os.getenv('MYSQL_PASS','rootpass')
MYSQL_DB = os.getenv('MYSQL_DB','appdb')

MONGO_URI = os.getenv('MONGO_URI','mongodb://127.0.0.1:27017')
MONGO_DB = 'appdb'

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
mongo = MongoClient(MONGO_URI)
mdb = mongo[MONGO_DB]

def process_appointment(appointment_id):
    # Query MySQL
    conn = pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASS, db=MYSQL_DB)
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute("SELECT a.*, u.email, u.first_name, s.name AS service_name FROM appointments a JOIN users u ON a.user_id=u.user_id JOIN services s ON a.service_id=s.service_id WHERE a.appointment_id=%s", (appointment_id,))
            row = cur.fetchone()
            if not row:
                print(f'Appointment {appointment_id} not found')
                return
            print('Processing', row)
            # Log to MongoDB activity_logs
            mdb.activity_logs.insert_one({
                'user_id': row['user_id'],
                'events': [
                    {'type': 'worker_processed', 'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ'), 'metadata': {'appointment_id': appointment_id}}
                ]
            })
            # increment visit counter
            r.incr(f"service:{row['service_id']}:visits")
    finally:
        conn.close()

def main():
    print('Worker started, waiting for appointments...')
    while True:
        try:
            item = r.rpop('queue:appointments')
            if item:
                # item expected like "appointment:5"
                if ':' in item:
                    _, aid = item.split(':',1)
                else:
                    aid = item
                try:
                    aid_int = int(aid)
                    process_appointment(aid_int)
                except Exception as e:
                    print('Error processing appointment', aid, e)
            else:
                time.sleep(1)
        except KeyboardInterrupt:
            print('Stopping worker')
            break

if __name__ == '__main__':
    main()
