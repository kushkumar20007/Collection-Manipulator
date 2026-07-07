## Collection Manipulator

## 📌 Objective

A Python program that manages a collection of student records. This project demonstrates intermediate-level Python concepts including:

- String formatting and manipulation
- Collection data types (`List`, `Tuple`, `Set`, `Dictionary`)
- Mutability and immutability
- Type casting
- The `del` keyword

---

## ✨ Features

### 🔤 String Formatting and Manipulation
- Gathers and stores student information (name, age, grade, and subjects) via user input, formatted for user-friendly display.
- Uses multiple string formatting methods (f-strings, `.format()`, and `%` formatting) to display student details.

### 📦 Collection Data Types
| Type | Usage |
|------|-------|
| **List** | Stores multiple student records |
| **Tuple** | Stores each student's unique, unchangeable info (student ID, date of birth) |
| **Set** | Manages and displays unique subjects offered, avoiding duplicates |
| **Dictionary** | Organizes student data — keys are student IDs, values are dictionaries containing name, age, grade, and subjects |

### 🔄 Mutability and Immutability
- Demonstrates **mutability** of Lists by adding or modifying student details.
- Demonstrates **immutability** of Tuples for student ID and date of birth, which never change once set.

### 🔢 Type Casting and `del` Keyword
- Performs type casting where needed (e.g., converting user input strings to integers or floats).
- Uses the `del` keyword to remove student records from the collection.

---

## 🖥️ Program Flow

### 1. Welcome and Instructions
- Displays a welcome message and an overview of the program's functionality.

### 2. Student Data Collection
- Prompts the user to enter details for each student: name, age, grade, subjects (comma-separated string), student ID, and date of birth.
- Stores the student's ID and date of birth as a **tuple**, adds subjects to a **set**, and stores each student's info in a **dictionary**. This dictionary is then added to a **list** of all student records.

### 3. Menu-Driven Options

| Option | Description |
|--------|-------------|
| **1. Add Student** | Add a new student record |
| **2. Display All Students** | Show all student records with formatted output (ID, name, age, grade, subjects) |
| **3. Update Student Information** | Update mutable info (e.g., age or subjects) for a student by ID |
| **4. Delete Student** | Remove a student record by ID using `del` |
| **5. Display Subjects Offered** | Show all unique subjects across students using a set |
| **6. Exit** | Thank the user and exit the program |

---

## 🎥 Video Demonstration

[![Watch Video](https://img.shields.io/badge/🎥-Watch_Video-red?style=for-the-badge)](https://drive.google.com/file/d/1wpLwO_HbDJRcXbrczn4U88puKnGn-Y5Y/view?usp=sharing)


### Output of code 

<img width="741" height="843" alt="image" src="https://github.com/user-attachments/assets/6b15ac4e-8757-4b7e-be08-75d06159b332" />


## 🧠 Concepts Demonstrated

- ✅ String formatting (f-strings, `.format()`, `%`)
- ✅ Lists for mutable collections
- ✅ Tuples for immutable records
- ✅ Sets for unique values
- ✅ Dictionaries for structured data
- ✅ Type casting (`int()`, `float()`)
- ✅ The `del` keyword for record removal

---
## 👨‍💻 Author

**Kush Kumar**

⭐ If you like this project, don't forget to star the repository!

