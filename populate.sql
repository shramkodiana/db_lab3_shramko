INSERT INTO Diet(diet_id, dino_diet) VALUES
(1,'Herbivorous'),
(2,'Carnivorous'),
(3,'Omnivorous');
INSERT INTO Species(species_id, dino_species) VALUES
(1,'Celestae'),
(2,'Ajax'),
(3,'Libratus'),
(4,'Mongoliensis'),
(5,'Gobiensis'),
(6,'Maximus');
INSERT INTO Type(type_id,type_of_dino) VALUES
(1,'Large theropod'),
(2,'Euornithopod'),
(3,'Ceratopsian'),
(4,'Small theropod'),
(5,'Sauropod');
INSERT INTO Dinosaur(dino_name, diet_id, species_id, type_id, lived_in, length_in_meters) VALUES
('Prosaurolophus',1,6,2,'USA',7.6),
('Albertosaurus',2,3,1,'Canada',9.0),
('Apatosaurus',1,2,5,'USA',21.0),
('Aardony',1,1,5,'South Africa', 8.0),
('Nomingia',3,5,4,'Mongolia',1.4),
('Rinchenia',3,4,4,'Mongolia',2.5),
('Saurophaganax',2,6,1,'USA',12),
('Gorgosaurus', 2,3,1,'USA',12.6),
('Microceratus',1,5,3,'Mongolia',0.5),
('Probactrosaurus',1,5,2,'China',6.0);


