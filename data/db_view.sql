

CREATE VIEW Locations AS(
	SELECT numero_location, 
	date_dep_location, 
	date_arr_location,
	adresse_dep_location, 
	adresse_arr_location,  
	numero_client,
	numero_employe,
	SUM(       )AS prixTotal_location
	FROM Locations JOIN Modeles ON(nom_modele=numero_location) JOIN Trottinettes ON()
	GROUP by numero_location, 
	date_dep_location, 
	date_arr_location,
	adresse_dep_location, 
	adresse_arr_location,  
	numero_client,
	numero_employe
);