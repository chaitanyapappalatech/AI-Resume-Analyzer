<h1 align="center">🗂️ Employee Management System</h1>

<p align="center">
  A professional console-based CRUD application built with <b>Python + MySQL</b><br/>
  for managing employee records efficiently.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/MySQL-phpMyAdmin-F29111?style=for-the-badge&logo=mysql&logoColor=white"/>
  <img src="https://img.shields.io/badge/VS%20Code-Editor-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge"/>
</p>

---

## 📚 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Database Design](#-database-design)
- [Installation](#-installation)
- [Application Menu](#-application-menu)
- [Screenshots](#-screenshots)
- [Sample Record](#-sample-record)
- [Learning Outcomes](#-learning-outcomes)
- [Future Improvements](#-future-improvements)
- [Resume Description](#-resume-description)
- [Author](#-author)

---

## 📖 About

The **Employee Management System** is a console-based application developed using **Python** and **MySQL**.
It allows users to perform complete CRUD (Create, Read, Update, Delete) operations on employee records stored in a MySQL database, managed visually through **phpMyAdmin**.

This project demonstrates:
- Python Programming with modular functions
- MySQL Database Connectivity
- Parameterized SQL Queries (SQL Injection prevention)
- CRUD Operations implementation
- Input Validation and Error Handling

> Designed as a beginner-friendly portfolio project — suitable for software developer interviews.

---

## ✨ Features

- ✅ Add Employee
- ✅ View All Employees
- ✅ Search Employee by ID
- ✅ Update Employee Salary
- ✅ Delete Employee
- ✅ MySQL Database Integration
- ✅ Parameterized SQL Queries (SQL Injection safe)
- ✅ Input Validation & Error Handling
- ✅ Interactive Menu-Driven Application

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.x | Programming Language |
| MySQL | Relational Database |
| phpMyAdmin | Visual Database Management |
| mysql-connector-python | Python ↔ MySQL Connector |
| VS Code | Code Editor |
| Git & GitHub | Version Control |

---

## 📂 Project Structure

```
Employee-Management-System/
│
├── screenshots/
│   ├── demo1_connection.png
│   ├── demo2_add_employee.png
│   ├── demo3_update.png
│   └── demo4_menu_delete.png
│
├── main.py              # Core application logic
├── database.sql         # SQL schema script
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🗄️ Database Design

**Database Name:** `employee_db`  
**Table Name:** `employees`

| Column | Data Type | Description |
|---|---|---|
| id | INT (PRIMARY KEY) | Unique employee identifier |
| name | VARCHAR(50) | Employee full name |
| department | VARCHAR(50) | Department name |
| salary | DECIMAL(10,2) | Employee salary |
| email | VARCHAR(100) | Employee email address |

**SQL Script:**

```sql
CREATE DATABASE employee_db;
USE employee_db;

CREATE TABLE employees (
    id         INT PRIMARY KEY,
    name       VARCHAR(50),
    department VARCHAR(50),
    salary     DECIMAL(10, 2),
    email      VARCHAR(100)
);
```

> 💡 Run this in **phpMyAdmin** → SQL tab at `http://localhost/phpmyadmin/`

---

## ⚙️ Installation

**1. Clone the repository:**
```bash
git clone https://github.com/chaitanyapappalatech/Employee-Management-System.git
```

**2. Move into the project folder:**
```bash
cd Employee-Management-System
```

**3. Install the required dependency:**
```bash
pip install mysql-connector-python
```

**4. Run the application:**
```bash
python main.py
```

> ⚠️ Make sure **XAMPP** is running with **Apache** and **MySQL** active before running the app.

---

## 💻 Application Menu

```
===== Employee Management System =====
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Exit
Enter Choice:
```

---

## 📸 Screenshots

### 📄 Step 1 — Resume Skills Extracted
> The program reads the resume PDF and extracts the candidate's skills.

![Resume Skills](screenshots/Resume_Skills.png)

---

### 📊 Step 2 — Job Skills & Match Score
> Job description skills are loaded and compared against resume skills. A match score is calculated.

![Job Skills and Match Score](screenshots/Job_Skills___Match_Score.png)

---

### ❌ Step 3 — Missing Skills Identified
> Skills present in the job description but absent from the resume are listed.

![Missing Skills](screenshots/Missing_Skills.png)

---

### 💡 Step 4 — Suggestions to Improve Resume
> The tool suggests which skills to learn in order to improve the match score.

![Suggestions](screenshots/Suggestions.png)

---

## 🧪 Sample Record

| Field | Value |
|---|---|
| ID | 1 |
| Name | Chaitanya |
| Department | IT |
| Salary | 50000 |
| Email | chaitanya@gmail.com |

**Full test cycle:**
```
Add → View → Search → Update (salary: 60000) → Delete → View (confirm removal)
```

---

## 🎯 Learning Outcomes

During this project, I learned:

- ✅ Connecting Python with MySQL using `mysql-connector-python`
- ✅ Implementing CRUD Operations with SQL
- ✅ Writing Parameterized Queries to prevent SQL Injection
- ✅ Managing database transactions with `conn.commit()`
- ✅ Exception Handling and Input Validation in Python
- ✅ Modular Programming with reusable functions
- ✅ Visual database management using phpMyAdmin
- ✅ Version control with Git & GitHub

---

## 🚀 Future Improvements

- [ ] GUI using Tkinter or PyQt5
- [ ] Employee Login & Admin Dashboard
- [ ] CSV Export of employee records
- [ ] PDF Report Generation
- [ ] Search by Department or Salary range
- [ ] Flask Web Version
- [ ] PostgreSQL migration with SQLAlchemy ORM

---

## 📄 Resume Description

```
Employee Management System | Python | MySQL | phpMyAdmin

• Developed a console-based Employee Management System using Python and MySQL.
• Implemented full CRUD operations (Add, View, Search, Update, Delete) for employee records.
• Connected Python with MySQL using mysql-connector-python library.
• Used parameterized SQL queries throughout to prevent SQL Injection attacks.
• Designed a relational database schema and managed it visually using phpMyAdmin.
• Built an interactive menu-driven application with input validation and exception handling.
```

---

## 👨‍💻 Author

**Chaitanya Pappala**  
Aspiring Software Developer | Python Developer | SQL Developer

[![GitHub](https://img.shields.io/badge/GitHub-chaitanyapappalatech-181717?style=for-the-badge&logo=github)](https://github.com/chaitanyapappalatech)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-chaitanya--sd-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/chaitanya-sd/)

---

## ⭐ Support

If you found this project helpful:

- ⭐ **Star** this repository
- 🍴 **Fork** the project
- 📢 **Share** it with others

---

<p align="center">Made with ❤️ using Python & MySQL</p>
