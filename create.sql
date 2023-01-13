CREATE TABLE Dinosaur
(
  dino_name            char(80)  NOT NULL,
  diet_id               INT NOT NULL,
  species_id            INT NOT NULL,
  type_id               INT NOT NULL,

  lived_in           char(80)  NOT NULL,
  length_in_meters       float8 NOT NULL

);

CREATE TABLE Diet
(
  diet_id         INT  NOT NULL,
  dino_diet    char(60)  NOT NULL 
);

CREATE TABLE Species
(
  species_id     INT  NOT NULL,
  dino_species   char(60)  NOT NULL
);

CREATE TABLE Type
(
  type_id      INT  NOT NULL ,
  type_of_dino   char(60) NOT NULL  
);

ALTER TABLE Dinosaur ADD PRIMARY KEY (dino_name);
ALTER TABLE Diet ADD PRIMARY KEY (diet_id);
ALTER TABLE Species ADD PRIMARY KEY (species_id);
ALTER TABLE Type ADD PRIMARY KEY (type_id);

ALTER TABLE Dinosaur ADD CONSTRAINT FK_dino_diet FOREIGN KEY (diet_id) REFERENCES Diet (diet_id);
ALTER TABLE Dinosaur ADD CONSTRAINT FK_dino_species FOREIGN KEY (species_id) REFERENCES Species (species_id);
ALTER TABLE Dinosaur ADD CONSTRAINT FK_type_of_dino FOREIGN KEY (type_id) REFERENCES Type (type_id);