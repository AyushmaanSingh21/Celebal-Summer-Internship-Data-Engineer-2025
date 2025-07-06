-- Weather Observation Station 3 : Query a list of CITY names from STATION for cities that have an even ID number
-- Resources :
-- https://www.hackerrank.com/challenges/weather-observation-station-3/problem

SELECT DISTINCT CITY 
FROM STATION 
WHERE MOD(ID, 2) = 0;