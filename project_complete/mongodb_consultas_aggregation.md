# Aggregation Pipelines - ejemplos

1) Contar eventos por tipo para user_id = 1
db.activity_logs.aggregate([
  { $match: { user_id: 1 } },
  { $unwind: "$events" },
  { $group: { _id: "$events.type", count: { $sum: 1 } } },
  { $sort: { count: -1 } }
]);

2) Total facturado por owner (documents type=invoice)
db.documents.aggregate([
  { $match: { type: 'invoice' } },
  { $group: { _id: "$owner_id", total: { $sum: "$content.amount" } } },
  { $sort: { total: -1 } }
]);

3) Project user profiles with notifications enabled
db.user_profiles.aggregate([
  { $match: { "preferences.notifications": true } },
  { $project: { user_id: 1, bio: 1, addresses: 1 } }
]);
