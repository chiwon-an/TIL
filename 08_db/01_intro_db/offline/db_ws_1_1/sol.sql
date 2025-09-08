CREATE DATABASE hospital_db

USE hospital_db

CREATE TABLE patients (
    patient_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    birthdate DATE NOT NULL,
    phone_number VARCHAR(15),
    email VARCHAR(50) UNIQUE,
    address VARCHAR(200),
    PRIMARY KEY (patient_id)
);

ALTER TABLE patients
    ADD COLUMN gender VARCHAR(10),
    MODIFY COLUMN phone_number VARCHAR(20);

TRUNCATE TABLE patients;