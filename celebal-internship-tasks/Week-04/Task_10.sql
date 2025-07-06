-- Contest Leaderboard
-- https://www.hackerrank.com/challenges/contest-leaderboard/problem

SELECT h.hacker_id, h.name, SUM(max_scores.max_score) AS total_score
FROM Hackers h
JOIN (
    SELECT s.hacker_id, s.challenge_id, MAX(s.score) AS max_score
    FROM Submissions s
    GROUP BY s.hacker_id, s.challenge_id
) AS max_scores
  ON h.hacker_id = max_scores.hacker_id
WHERE max_scores.max_score > 0
GROUP BY h.hacker_id, h.name
ORDER BY total_score DESC, h.hacker_id;