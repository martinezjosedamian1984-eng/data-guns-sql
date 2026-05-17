USE data_guns;

SELECT COUNT(*) AS total_canciones
FROM canciones_guns;

SELECT album, COUNT(*) AS cantidad_canciones
FROM canciones_guns
GROUP BY album
ORDER BY cantidad_canciones DESC;

SELECT album, AVG(duracion_min) AS duracion_promedio
FROM canciones_guns
GROUP BY album
ORDER BY duracion_promedio DESC;

SELECT cancion, album, duracion_min
FROM canciones_guns
ORDER BY duracion_min DESC
LIMIT 10;