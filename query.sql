/*
Database schema:
- Users (columns: id, name, email)
- Orders (columns: id, user_id, order_total, created_at)
*/

SELECT DISTINCT u.name, u.email
FROM Users AS u
JOIN Orders AS o ON u.id = o.user_id
WHERE o.order_total > 100;