SELECT COUNT(*) AS Total_students FROM Students;

SELECT Department_ID,COUNT(*) AS Total
FROM Students
GROUP BY Department_ID;

Select Department_ID,COUNT(*) AS Total_faculty
FROM Faculty
GROUP BY Department_ID

SELECT Status, COUNT(*) AS Total
FROM Fees
GROUP BY Status;

SELECT Status, COUNT(*) AS Total
FROM Attendance
GROUP BY Status;

SELECT TOP 10 *
FROM Students;

SELECT
    s.Student_ID,
    s.Student_Name,
    d.Department_Name
FROM Students s
INNER JOIN Departments d
ON s.Department_ID = d.Department_ID;

SELECT
    f.Faculty_Name,
    d.Department_Name,
    f.Designation
FROM Faculty f
INNER JOIN Departments d
ON f.Department_ID = d.Department_ID;

SELECT Status, COUNT(*) AS Total_Tickets
FROM IT_Tickets
GROUP BY Status;

SELECT AVG(Age) AS Average_Age
FROM Students;

