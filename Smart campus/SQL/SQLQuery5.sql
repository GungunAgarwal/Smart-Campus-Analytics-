USE SmartCampusDB;
GO

-- Students -> Departments
ALTER TABLE Students
ADD CONSTRAINT FK_Students_Departments
FOREIGN KEY (Department_ID)
REFERENCES Departments(Department_ID);

-- Faculty -> Departments
ALTER TABLE Faculty
ADD CONSTRAINT FK_Faculty_Departments
FOREIGN KEY (Department_ID)
REFERENCES Departments(Department_ID);

-- Courses -> Departments
ALTER TABLE Courses
ADD CONSTRAINT FK_Courses_Departments
FOREIGN KEY (Department_ID)
REFERENCES Departments(Department_ID);

-- Courses -> Faculty
ALTER TABLE Courses
ADD CONSTRAINT FK_Courses_Faculty
FOREIGN KEY (Faculty_ID)
REFERENCES Faculty(Faculty_ID);

-- Attendance -> Students
ALTER TABLE Attendance
ADD CONSTRAINT FK_Attendance_Students
FOREIGN KEY (Student_ID)
REFERENCES Students(Student_ID);

-- Attendance -> Courses
ALTER TABLE Attendance
ADD CONSTRAINT FK_Attendance_Courses
FOREIGN KEY (Course_ID)
REFERENCES Courses(Course_ID);

-- Library -> Students
ALTER TABLE Library
ADD CONSTRAINT FK_Library_Students
FOREIGN KEY (Student_ID)
REFERENCES Students(Student_ID);

-- Hostel -> Students
ALTER TABLE Hostel
ADD CONSTRAINT FK_Hostel_Students
FOREIGN KEY (Student_ID)
REFERENCES Students(Student_ID);

-- Fees -> Students
ALTER TABLE Fees
ADD CONSTRAINT FK_Fees_Students
FOREIGN KEY (Student_ID)
REFERENCES Students(Student_ID);

-- IT_Tickets -> Students
ALTER TABLE IT_Tickets
ADD CONSTRAINT FK_ITTickets_Students
FOREIGN KEY (Student_ID)
REFERENCES Students(Student_ID);