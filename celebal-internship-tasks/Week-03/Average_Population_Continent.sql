-- Average Population : Query the average population for all cities in CITY, rounded down to the nearest integer.
-- Resources :
-- https://www.hackerrank.com/challenges/average-population-of-each-continent/problem

SELECT 
    COUNTRY.Continent, 
    FLOOR(AVG(CITY.Population)) AS Average_Population
FROM 
    CITY
JOIN 
    COUNTRY ON CITY.CountryCode = COUNTRY.Code
GROUP BY 
    COUNTRY.Continent;