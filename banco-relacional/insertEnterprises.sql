ALTER TABLE enterprises MODIFY cnpj VARCHAR(14);

INSERT INTO enterprises
    (name, cnpj)
VALUES
    ("Bradesco", 95694186000132),
    ("Vale", 27887148000146),
    ("Cielo", 01598317000134);

DESC enterprises;
DESC mayors;
SELECT * FROM enterprises;
SELECT * FROM cities;

INSERT INTO companies_unities
    (enterprise_id, city_id, headquarter)
VALUES
    (1, 1, 1),
    (1, 2, 0),
    (2, 1, 0),
    (2, 2, 1)