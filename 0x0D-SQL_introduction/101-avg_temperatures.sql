-- a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

SELECT city, AVG(value) AS avrg_temps FROM  temperatures GROUP BY city ORDER BY avrg_temps DESC;
