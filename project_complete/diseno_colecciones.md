# Diseño de colecciones MongoDB

Colecciones:
1. user_profiles
   - _id: ObjectId
   - user_id: int (referencia a users.user_id en MySQL)
   - bio: string
   - preferences: { notifications: bool, lang: string }
   - addresses: [ { label, street, city } ]
   - social_links: [string]
   - created_at: date

2. activity_logs
   - _id: ObjectId
   - user_id: int
   - events: [ { type: string, timestamp: date, metadata: object } ]

3. documents
   - _id: ObjectId
   - owner_id: int
   - type: string
   - content: object
   - attachments: [ { filename, url, meta } ]
