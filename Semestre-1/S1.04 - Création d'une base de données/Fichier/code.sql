
CREATE TABLE public.PERSONNES (
                IdPersonne INTEGER NOT NULL,
                Nom VARCHAR NOT NULL,
                Prenom VARCHAR NOT NULL,
                CONSTRAINT personnes_pk PRIMARY KEY (IdPersonne)
);


CREATE TABLE public.ETUDIANTS (
                IdPersonne INTEGER NOT NULL,
                CONSTRAINT etudiants_pk PRIMARY KEY (IdPersonne)
);


CREATE TABLE public.ENSEIGNANTS (
                IdPersonne INTEGER NOT NULL,
                CONSTRAINT enseignants_pk PRIMARY KEY (IdPersonne)
);


CREATE TABLE public.MODULES (
                IdModule INTEGER NOT NULL,
                Code VARCHAR NOT NULL,
                Intitule_module VARCHAR NOT NULL,
                UE VARCHAR NOT NULL,
                IdPersonne INTEGER NOT NULL,
                CONSTRAINT modules_pk PRIMARY KEY (IdModule)
);


CREATE TABLE public.EVALUATIONS (
                IdEvaluation INTEGER NOT NULL,
                Nom_evaluation VARCHAR NOT NULL,
                Date_evaluation DATE NOT NULL,
                IdPersonne INTEGER NOT NULL,
                IdModule INTEGER NOT NULL,
                CONSTRAINT evaluations_pk PRIMARY KEY (IdEvaluation)
);


ALTER TABLE public.ETUDIANTS ADD CONSTRAINT personne_etudiant_fk
FOREIGN KEY (IdPersonne)
REFERENCES public.PERSONNES (IdPersonne)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.ENSEIGNANTS ADD CONSTRAINT personne_enseignant_fk
FOREIGN KEY (IdPersonne)
REFERENCES public.PERSONNES (IdPersonne)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.EVALUATIONS ADD CONSTRAINT etudiant_evaluation_fk
FOREIGN KEY (IdPersonne)
REFERENCES public.ETUDIANTS (IdPersonne)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.MODULES ADD CONSTRAINT enseignant_module_fk
FOREIGN KEY (IdPersonne)
REFERENCES public.ENSEIGNANTS (IdPersonne)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.EVALUATIONS ADD CONSTRAINT module_evaluation_fk
FOREIGN KEY (IdModule)
REFERENCES public.MODULES (IdModule)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;
