CREATE TABLE IF NOT EXISTS enterprises(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    cnpj INT UNSIGNED,
    PRIMARY KEY (id),
    UNIQUE KEY (cnpj)
);

CREATE TABLE IF NOT EXISTS companies_unities (
    enterprise_id INT UNSIGNED NOT NULL,
    city_id INT UNSIGNED NOT NULL,
    headquarter TINYINT(1) NOT NULL,
    PRIMARY KEY (enterprise_id, city_id)
);