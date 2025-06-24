-- Creating States table!
create table states(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(545) NOT NULL, 
    acronym VARCHAR(2) NOT NULL,
    regions ENUM("North", "Northeast", "Midwest", "Southeast",  "South")NOT NULL,
    population DECIMAL(5,2) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY(name),
    UNIQUE KEY(acronym)
);