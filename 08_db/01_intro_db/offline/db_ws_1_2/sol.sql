USE hospital_db

CREATE TABLE hospital (
    hospital_id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(150) NOT NULL,
    location VARCHAR(200) NOT NULL,
    established_date DATE,
    contact_number VARCHAR(20) UNIQUE,
    type VARCHAR(50) NOT NULL,
    PRIMARY KEY (hospital_id)
);

ALTER TABLE hospital
    ADD COLUMN capacity INT,
    MODIFY COLUMN type VARCHAR(100),
    CHANGE COLUMN established_date founded_date DATE;

DROP TABLE hospital

DROP TABLE patients