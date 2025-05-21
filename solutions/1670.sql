SELECT patient_id, patient_name, conditions
FROM Patients
WHERE CONCAT(' ', conditions, ' ') LIKE '% DIAB1%';
