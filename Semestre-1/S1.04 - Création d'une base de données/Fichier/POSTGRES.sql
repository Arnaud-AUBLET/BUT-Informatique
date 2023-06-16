DROP TABLE tempo;
DROP TABLE estevalue;
DROP TABLE evaluations;
DROP TABLE modules;
DROP TABLE enseignants;
DROP TABLE etudiants;
DROP TABLE personnes;



CREATE TABLE personnes (
	IdPersonne INTEGER PRIMARY KEY,
	Nom VARCHAR,
	Prenom VARCHAR );

CREATE TABLE etudiants (
	IdEtudiant INTEGER PRIMARY KEY REFERENCES personnes (IdPersonne) );

CREATE TABLE enseignants (
	IdEnseignant INTEGER PRIMARY KEY REFERENCES personnes (IdPersonne) );

CREATE TABLE modules (
	IdModule INTEGER PRIMARY KEY,
	Intitule_module VARCHAR,
	Code VARCHAR,
	UE VARCHAR,
	IdEnseignant INTEGER REFERENCES enseignants (IdEnseignant) );

CREATE TABLE evaluations (
	IdEvaluation INTEGER PRIMARY KEY,
	Nom_Evaluation VARCHAR,
	Date DATE,
	IdModule INTEGER REFERENCES modules (IdModule) );

CREATE TABLE estevalue (
	IdEtudiant INTEGER REFERENCES etudiants (IdEtudiant),
	IdEvaluation INTEGER REFERENCES evaluations (IdEvaluation),
	Note FLOAT CHECK (note > 0 OR note IS NULL),
	PRIMARY KEY (IdEtudiant, IdEvaluation) );
	
CREATE TABLE tempo	(
	id_enseignant INTEGER,
	nom_enseignant VARCHAR,
	prenom_enseignant VARCHAR,
	id_module INTEGER,
	code VARCHAR,
	ue VARCHAR,
	intitule_module VARCHAR,
	id_evaluation INTEGER,
	nom_evaluation VARCHAR,
	date_evaluation DATE,
	note FLOAT,
	id_etudiant INTEGER,
	nom_etudiant VARCHAR,
	prenom_etudiant VARCHAR );
	
INSERT INTO tempo VALUES (161,'Coignard','Charles',18,'R107','UE12','Outils_mathématiques_fondamentaux',1,'Contrôle_1','2021-11-24',7.25,37,'Havez','Catherine' );

INSERT INTO tempo VALUES (157,'Donizeau','Leon',14,'R106','UE12','Mathématiques_discrètes',2,'Mini-test_3_Logique','2021-11-08',6,7,'Schilling','Marius');

INSERT INTO tempo VALUES (157,'Donizeau','Leon',14,'R106','UE12','Mathématiques_discrètes',3,'Contrôle_Ensembles_et_relations','2021-10-20',12.16,51,'Canet','Georgette');

INSERT INTO tempo VALUES (150,'Gervais','Vincent',7,'R110','UE12','Anglais_technique',4,'Oral_presentation','2022-01-20',15.5,126,'Chaumaz','Herve');

INSERT INTO tempo VALUES (157,'Donizeau','Leon',14,'R106','UE12','Mathématiques_discrètes',5,'Mini-test_2_Relations','2021-10-04',10,43,'Bagur','Gerard');

INSERT INTO tempo VALUES (145,'Heron','Anne',2,'R101','UE12','Initiation_au_développement',6,'Controle_moyen_1','2021-09-29',17.75,63,'Carron','Oceane');

INSERT INTO tempo VALUES (144,'Helin','Mohamed',1,'S104','UE13','Création_d_une_base_de_données',7,'Evaluation_phase_1','2021-09-06',2.3,131,'Delayen','Cindy');

INSERT INTO tempo VALUES (146,'Denis','Olivier',3,'R102','UE12','Développement_d_interfaces_web',8,'Contrôle_court','2021-12-15',13,123,'Badji','Elodie');

INSERT INTO tempo VALUES (157,'Donizeau','Leon',14,'R106','UE12','Mathématiques_discrètes',5,'Mini-test_2_Relations','2021-10-04',9.5,115,'Dangreaux','Ngoc');

INSERT INTO tempo VALUES (144,'Helin','Mohamed',1,'S104','UE13','Création_d_une_base_de_données',9,'Evaluation_phase_2','2021-09-06',8.3,6,'Franceschi','Bruno');

INSERT INTO tempo VALUES (145,'Heron','Anne',2,'R101','UE12','Initiation_au_développement',10,'Minicontrole_2','2021-09-20',1.5,20,'Tessier','Matthieu');

INSERT INTO tempo VALUES (159,'Carrere','Mohamed',16,'R105','UE12','Introduction_aux_bases_de_données_et_SQL',11,'Contrôle_court','2021-10-13',16.25,85,'Guiard','Alphonse');

INSERT INTO tempo VALUES (149,'Martos','Marcelle',6,'R111','UE12','Bases_de_la_communication',12,'CV_(andromeda_Cygnus)','2022-01-22',10,120,'Abdennebi','Joseph');

INSERT INTO tempo VALUES (156,'Lusseau','Patrice',13,'S105','UE13','Recueil_de_besoins',13,'Projet_mariage','2022-01-18',12,120,'Abdennebi','Joseph');

SELECT * FROM tempo;

INSERT INTO personnes (SELECT DISTINCT id_enseignant,nom_enseignant,prenom_enseignant FROM tempo);
INSERT INTO personnes (SELECT DISTINCT id_etudiant,nom_etudiant,prenom_etudiant FROM tempo);
INSERT INTO enseignants (SELECT DISTINCT id_enseignant FROM tempo);
INSERT INTO etudiants (SELECT DISTINCT id_etudiant FROM tempo);
INSERT INTO modules (SELECT DISTINCT id_module,intitule_module,ue,code, id_enseignant FROM tempo);
INSERT INTO evaluations (SELECT DISTINCT  id_evaluation,nom_evaluation,date_evaluation,id_module FROM tempo);
INSERT INTO estevalue (SELECT DISTINCT id_etudiant, id_evaluation, note FROM tempo);

SELECT DISTINCT p.prenom FROM etudiants as e, personnes as p, estevalue as eval WHERE e.IdEtudiant = p.IdPersonne AND e.IdEtudiant = eval.IdEtudiant AND eval.Note >=10 AND eval.Note <= 15;
SELECT DISTINCT modules.intitule_module FROM modules, evaluations WHERE modules.IdModule = evaluations.IdModule AND evaluations.date = '2021-09-06';