Select * from states where id = 19

INSERT INTO cities (name, area, id_state)
VALUES ("Campinas", 795, 25)

INSERT INTO cities (name, area, id_state)
VALUES ("Niterói", 133.9, 19)

INSERT INTO cities
    (name, area, id_state)
VALUES (
    "Caruaru", 
    920.6, 
    (select id from states where acronym = "PE")
)

INSERT INTO cities (name, area, id_state)
VALUES ("Juazeiro do Norte", 248.2, (select id from states where acronym = "CE"))

select * from cities