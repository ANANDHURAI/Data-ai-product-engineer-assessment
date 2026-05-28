SELECT
    weather_condition,
    AVG(temperature) AS average_temperature,
    COUNT(*) AS total_records
FROM
    `sound-country-464003-n4.weather_pipeline.weather_data`
GROUP BY
    weather_condition
ORDER BY
    average_temperature DESC;