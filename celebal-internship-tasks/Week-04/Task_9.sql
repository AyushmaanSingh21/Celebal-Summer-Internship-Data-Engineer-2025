-- Ollivander's Inventory
-- https://www.hackerrank.com/challenges/harry-potter-and-wands/problem

SELECT w.id, wp.age, w.coins_needed, w.power
FROM wands w
JOIN wands_property wp ON w.code = wp.code
WHERE wp.is_evil = 0
  AND w.coins_needed = (
    SELECT MIN(w2.coins_needed)
    FROM wands w2
    JOIN wands_property wp2 ON w2.code = wp2.code
    WHERE w2.power = w.power AND wp2.age = wp.age AND wp2.is_evil = 0
  )
ORDER BY w.power DESC, wp.age DESC;

