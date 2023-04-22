

CREATE TABLE Clients (
	numero_client TEXT(50),
    prenom_client TEXT (50) NOT NULL,
	date_naissance_client date NOT NULL, 
    adresse_client TEXT (50)NOT NULL,
   CONSTRAINT pk_client_numero_client PRIMARY KEY(numero_client),
   CONSTRAINT ck_client_numero_client CHECK (numero_client>0)
);
CREATE TABLE Employes(
	numero_employe INTEGER,
	nom_employe TEXT(50) NOT NULL,
	prenom_employe TEXT(50) NOT NULL, 
	date_naissance_employe date NOT NULL,
	adresse_employe TEXT(50),
	horaire_employe TEXT(50),
	CONSTRAINT pk_employe_numero_employe PRIMARY KEY(numero_employe),
	CONSTRAINT ck_employe_numero_employe CHECK (numero_employe>0)
	);
	
CREATE TABLE Modeles(
	nom_modele TEXT(50), 
	couleur_modele TEXT(50), 
	vitesse_modele TEXT(50), 
	prix_modele REAL,
	prixParMinutes_modele REAL,
	CONSTRAINT pk_modele_nom_modele PRIMARY KEY(nom_modele),
	CONSTRAINT ck_modele_vitesse_modele CHECK (vitesse_modele>0),
	CONSTRAINT ck_modele_prix_modele CHECK (prix_modele>0),
	CONSTRAINT ck_modele_couleur_modele CHECK (couleur_modele ='blanc' OR 
										couleur_modele ='bleu' OR couleur_modele ='rouge')
);

CREATE TABLE Batteries(
	numero_batterie INTEGER, 
	charge_batterie TEXT(50),
	CONSTRAINT pk_batterie_numero_batterie PRIMARY KEY (numero_batterie),
	CONSTRAINT ck_batterie_numero_batterie CHECK (numero_batterie>0),
	CONSTRAINT ck_batterie_charge_batterie CHECK (charge_batterie='petit' AND 
									charge_batterie>=0 AND charge_batterie<=30
									OR charge_batterie='moyen' AND charge_batterie>30 
									AND charge_batterie<= 60 OR charge_batterie='grand' AND
									charge_batterie>60 AND charge_batterie<=100)
);
		
CREATE TABLE Trottinettes(
	numero_trottinette INTEGER, 
	date_fabrication_trottinette date,
	etat_trottinette TEXT (50)NOT NULL, 
	nom_modele TEXT (54)NOt NULL, 
	numero_batterie INTEGER,
	CONSTRAINT pk_trottinette_numero_trottinette PRIMARY KEY(numero_trottinette),
	CONSTRAINT cu_trottinette_numero_batterie UNIQUE (numero_batterie),
	CONSTRAINT fk_trottinette_numero_batterie FOREIGN KEY (numero_batterie) 
											  REFERENCES Batteries (numero_batterie),
	CONSTRAINT fk_trottinette_nom_modele FOREIGN KEY(nom_modele) REFERENCES Modeles (nom_modele),
	CONSTRAINT ck_trotinette_numero_trottinette CHECK (numero_trottinette>0),
	CONSTRAINT ck_trotinette_etat_trottinette CHECK (etat_trottinette='bon' 
											OR etat_trottinette='moyen' OR
											etat_trottinette='mauvais')
												
);
 
CREATE TABLE Locations(
	 numero_location INTEGER, 
	 date_dep_location date NOT NULL, 
	 date_arr_location date NOT NULL,
	 adresse_dep_location TEXT(50), 
	 adresse_arr_location TEXT(50),  
	 prixTotal_location REAL, 
	 numero_client TEXT(50),
	 numero_employe INTEGER NOT NULL,
	 CONSTRAINT pk_locations_numero_location PRIMARY KEY (numero_location)

);

CREATE TABLE LocationsTrottinettes(
	 numero_location INTEGER, 
	 numero_trottinette INTEGER,
	 CONSTRAINT cp_LocationsTrottinettes_numero_location_numero_trottinette 
							PRIMARY KEY(numero_location,numero_trottinette),
	CONSTRAINT fk_LocationsTrottinettes_numero_location FOREIGN KEY(numero_location) 
							REFERENCES Locations(numero_location),
	CONSTRAINT fk_LocationsTrottinettes_numero_trottinette FOREIGN KEY(numero_trottinette) 
							REFERENCES Trottinettes(numero_trottinette)				
);


	



