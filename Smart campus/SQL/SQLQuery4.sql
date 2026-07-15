
ALTER TABLE Students
ADD CONSTRAINT FK_Students_Departments
FOREIGN KEY (Department_ID)
REFERENCES Departments(Department_ID);

ALTER TABLE Students
DROP COLUMN Department_Name;

SELECT * FROM Students;

SELECT * FROM Departments;
SELECT * FROM Fees;
