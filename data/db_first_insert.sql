INSERT INTO Clients 
VALUES (1, "Montaigné", "Gilbert", '1990-03-04', "38 allée d'Ahm");

INSERT INTO Clients 
VALUES (2, "Rousseau", 'Lénaic', '2002-11-04', "38 allée d'Ahm");

INSERT INTO Clients 
VALUES (3, "Garcia", "Giulio", '2000-08-06', "15 Gabriel Peri");

INSERT INTO Clients 
VALUES (4, "Salina", "Martha", '2003-07-02', "13 Rue de la Republique");


----------------------------------------------------


INSERT INTO Employes 
VALUES (1, "Montaigné", "Albert", '1991-03-04', "37 allée d'Ahm", 
"10h30,12h00 | 13h30,17h30 : 13h30,17h30 | : | : | 13h30,17h30 : |13h30,17h30 : |: |");

INSERT INTO Employes 
VALUES (2, "Perez", "Rafaela", '2000-03-05', "14 Rue Colonel", 
"10h30,12h00 | 13h30,17h30 : 13h30,17h30 | : | : | 13h30,17h30 : |13h30,17h30 : |: |");

INSERT INTO Employes 
VALUES (3, "Martinez", "Pablo", '2005-03-05', "14 Rue d'henry vallon", 
"10h30,12h00 | 13h30,17h30 : 13h30,17h30 | : | : | 13h30,17h30 : |13h30,17h30 : |13h30,17h30: |");

INSERT INTO Employes 
VALUES (4, "Rodriguez", "Angela", '1999-03-05', "14 Rue d'henry vallon", 
"10h30,12h00 | 13h30,17h30 : 13h30,17h30 | : | : | 13h30,17h30 : |13h30,17h30 : |13h30,17h30: | 15h00, 20h00");


-------------------------------------------------------


INSERT INTO Batteries 
VALUES (1, "petit");

INSERT INTO Batteries 
VALUES (2, "moyen");

INSERT INTO Batteries 
VALUES (3, "grand");

INSERT INTO Batteries 
VALUES (4, "grand");

INSERT INTO Batteries 
VALUES (5, "moyen");

INSERT INTO Batteries 
VALUES (6, "moyen");


-------------------------------------------------------


INSERT INTO Modeles 
VALUES ("fast", "blanc", 60, 11, 7);

INSERT INTO Modeles 
VALUES ("xiaomi", "rouge", 25, 10, 6);

INSERT INTO Modeles 
VALUES ("MOBYGUM", "bleu", 65, 12, 9);


-------------------------------------------------------


INSERT INTO Trottinettes 
VALUES (1, '2019-03-04', "bon", "fast", 1);

INSERT INTO Trottinettes 
VALUES (2, '2000-07-01', "bon", "xiaomi", 2);

INSERT INTO Trottinettes 
VALUES (3, '2012-01-01', "moyen", "MOBYGUM", 3);

INSERT INTO Trottinettes 
VALUES (4, '2012-01-01', "mauvais", "MOBYGUM", 4);

INSERT INTO Trottinettes 
VALUES (5, '2012-01-01', "bon", "fast", 6);


-------------------------------------------------------


INSERT INTO Locations 
VALUES (1, '2022-03-04 17:50', "77 rue allié", NULL, NULL, 1, 1);


INSERT INTO Locations 
VALUES (2, '2022-03-04 18:50', "77 rue allié", "88 place du peuple", "2022-03-04 20:20", 1, 1);

INSERT INTO Locations 
VALUES (3, '2022-03-04 13:00', "77 rue allié", "88 place du peuple", "2022-03-04 15:00", 4, 2);


-------------------------------------------------------


INSERT INTO LocationsTrottinettes 
VALUES (1, 1);

INSERT INTO LocationsTrottinettes 
VALUES (2, 1);

INSERT INTO LocationsTrottinettes 
VALUES (3, 2);

INSERT INTO LocationsTrottinettes 
VALUES (3, 1);