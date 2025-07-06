-- Average Population : Query the average population for all cities in CITY, rounded down to the nearest integer.
-- Resources :
-- https://www.hackerrank.com/challenges/average-population/problem

SELECT FLOOR(AVG(Population)) AS Average_Population 
FROM CITY;