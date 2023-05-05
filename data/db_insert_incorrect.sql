---Result: UNIQUE constraint failed: Clients.numero_client (le numero_client EXISTS)
INSERT INTO Clients 
VALUES (1, "Perez", "Rafael", '2003-03-02', "Rue Cours Berriat");

---Result: UNIQUE constraint failed: Employes.numero_employe (numero_employe EXISTS)
INSERT INTO Employes 
VALUES (1, "Lopez", "Albert", '1991-03-04', "37 allée d'Ahm", 
"10h30,12h00 | 13h30,17h30 : 13h30,17h30 | : | : | 13h30,17h30 : |13h30,17h30 : |: |");

----Result: CHECK constraint failed: ck_modele_couleur_modele (le couleur_modele Noir, n'existe pas)
INSERT INTO Modeles 
VALUES ("fast", "Noir", 60, 11, 7);

----Result: CHECK constraint failed: ck_batterie_charge_batterie(le numero_batterie #1 EXISTS)
INSERT INTO Batteries 
VALUES (1, "Grand")
------CHECK constraint failed: ck_modele_couleur_modele(Modele fast EXISTS)
INSERT INTO Modeles 
VALUES ("fast", "Noir", 60, 11, 10);

---Result: Result: FOREIGN KEY constraint failed(nom_modele n'EXISTS pas)
INSERT INTO Trottinettes 
VALUES (7, '2019-03-04', "bon", "noir", 5);


-------Result: NOT NULL constraint failed: Locations.date_dep_location
-- (La date ne peut pas être nulle)
INSERT INTO Locations 
VALUES (4, NULL, NULL, 1, 1);

----Result: FOREIGN KEY constraint failed(Le numero_client #7 EXISTS)
INSERT INTO Locations 
VALUES (5, '2022-03-04 17:00', "2022-03-04 17:50", 7, 2);

-----Result: UNIQUE constraint failed: Locations.numero_location (le numero_location EXISTS)
INSERT INTO Locations 
VALUES (3, '2022-01-01 14:00', "2022-01-01 15:00", 4, 2);

----Result: FOREIGN KEY constraint failed (le numero_trottinette 7, n'EXISTS pas)
INSERT INTO LocationsTrottinettes 
VALUES (1, 7);

------Result: UNIQUE constraint failed: LocationsTrottinettes.numero_location, 
------LocationsTrottinettes.numero_trottinette(
-----Le couple numero_location-numero_trottinette EXISTS)

INSERT INTO LocationsTrottinettes 
VALUES (3, 1);


