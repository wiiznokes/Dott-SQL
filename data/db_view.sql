

CREATE VIEW LocationsPrixTotal (
	numero_location, date_dep_location, date_arr_location,
    numero_client, numero_employe, prix_total_location, duree_location
) AS
SELECT L.numero_location, date_dep_location, date_arr_location,
    numero_client, numero_employe,
	SUM(M.prix_modele + M.prix_par_minutes_modele * ((julianday(L.date_arr_location) - julianday(L.date_dep_location)) * 24 * 60)) 
		AS prix_total_location,
	(julianday(L.date_arr_location) - julianday(L.date_dep_location)) * 24 * 60 
		AS duree_location
FROM Locations L
JOIN LocationsTrottinettes LT ON L.numero_location = LT.numero_location
JOIN Trottinettes T ON LT.numero_trottinette = T.numero_trottinette
JOIN Modeles M ON T.nom_modele = M.nom_modele
GROUP BY L.numero_location;