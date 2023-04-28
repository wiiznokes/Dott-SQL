

CREATE VIEW LocationsPrixTotal(numero_location, date_dep_location, date_arr_location,adresse_dep_location, 
	adresse_arr_location,  numero_client, numero_employe, prix_total_location, duree)AS
	WITH LocationsPrixTotalTrottinette AS(
	SELECT numero_location, date_dep_location, date_arr_location,adresse_dep_location, 
	adresse_arr_location,  
	numero_client,
	numero_employe,
    (julianday(date_arr_location)-julianday(date_dep_location)) * 24 * 60 AS duree
    FROM Locations
    GROUP by numero_location, 
	date_dep_location, 
	date_arr_location,
	adresse_dep_location, 
	adresse_arr_location,  
	numero_client,
	numero_employe
	),
    PrixChaqueModeleTrottinette AS(
        SELECT numero_trottinette, SUM(prix_modele+prix_par_minutes_modele) AS PrixTrotinette
        FROM Modeles JOIN Trottinettes USING(nom_modele)
        GROUP BY numero_trottinette
    )  
    SELECT numero_location,
    date_dep_location, 
    date_arr_location,
    adresse_dep_location, 
	adresse_arr_location,  
	numero_client,
	numero_employe,
    Sum(duree*PrixTrotinette) AS prix_total_location,
	duree
	FROM  PrixChaqueModeleTrottinette JOIN LocationsTrottinettes USING (numero_trottinette) JOIN LocationsPrixTotalTrottinette USING(numero_location)
    GROUP by numero_location, 
	date_dep_location, 
	date_arr_location,
	adresse_dep_location, 
	adresse_arr_location,  
	numero_client,
	numero_employe,
	duree;

