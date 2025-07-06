-- Weather Observation Station 5 : Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths
-- Resources :
-- https://www.hackerrank.com/challenges/weather-observation-station-5/problem

-- Shortest city name
SELECT TOP 1
    CITY,
    LEN(CITY) AS name_length
FROM
    STATION
ORDER BY
    name_length ASC,
    CITY ASC;

-- Longest city name
SELECT TOP 1
    CITY,
    LEN(CITY) AS name_length
FROM
    STATION
ORDER BY
    name_length DESC,
    CITY ASC;