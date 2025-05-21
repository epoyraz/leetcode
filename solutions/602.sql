WITH AllFriends AS (
    SELECT requester_id AS id, accepter_id AS friend_id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id, requester_id AS friend_id
    FROM RequestAccepted
),
FriendCounts AS (
    SELECT
        id,
        COUNT(DISTINCT friend_id) AS num
    FROM AllFriends
    GROUP BY id
)
SELECT
    id,
    num
FROM FriendCounts
WHERE num = (
    SELECT MAX(num) FROM FriendCounts
);
