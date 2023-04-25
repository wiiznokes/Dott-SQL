


INSERT INTO Clients 
VALUES (1, "Montaigné", "Gilbert", '1990-03-04', "38 allée d'Ahm");

INSERT INTO Clients 
VALUES (2, "Rousseau", "Lénaic", '2002-11-04', "38 allée d'Ahm");


INSERT INTO Employes 
VALUES (1, "Montaigné", "Albert", '1991-03-04', "37 allée d'Ahm", 
"lu: 10h30,12h00, 13h30,17h30 ma:13h30,17h30 me: je: 13h30,17h30 ve:13h30,17h30 sa: di:");


INSERT INTO Batteries 
VALUES (1, "petit");

INSERT INTO Batteries 
VALUES (2, "moyen");

INSERT INTO Batteries 
VALUES (3, "grand");


INSERT INTO Modeles 
VALUES ("fast", "blanc", 60, 11, 7);


INSERT INTO Trottinettes 
VALUES (1, '2019-03-04', "bon", "fast", 1);


INSERT INTO Locations 
VALUES (1, '2022-03-04 17:50', "77 rue allié", NULL, NULL, NULL, 1, 1);


INSERT INTO Locations 
VALUES (2, '2022-03-04 18:50', "77 rue allié", "88 place du peuple", "2022-03-04 20:20", 19.2, 1, 1);


INSERT INTO LocationsTrottinettes 
VALUES (1, 1);

INSERT INTO LocationsTrottinettes 
VALUES (2, 1);

