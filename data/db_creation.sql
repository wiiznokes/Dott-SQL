CREATE TABLE Clients (
    numero_client TEXT NOT NULL,
    prenom_client TEXT  NOT NULL,
	date_naissance_client date NOT NULL, 
    adresse_client TEXT NOT NULL,
   CONSTRAINT pk_client_numero_client PRIMARY KEY(numero_client)
);