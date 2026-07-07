print("Welcome to the Data Organizer!\n")
students = []
while True:
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("\nEnter Student details:")
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ")
            dob = input("Enter Date of Birth: ")
            subjects = input("Enter Subjects (comma separated): ")

            subject_set = set(subjects.split(","))

            id_dob = (student_id, dob)

            student = {
                "name": name,
                "age": age,
                "grade": grade,
                "subjects": subject_set,
                "details": id_dob
            }

            students.append(student)

            print("Student Added Successfully!")
        case 2:
            if len(students) == 0:
                print("No student records found.")
            else:
                for student in students:
                    print(f"ID: {student['details'][0]} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']} | DOB: {student['details'][1]} | Subjects: {','.join(student['subjects'])}")
        case 3:
            sid = input("Enter Student ID to Update: ")

            found = False

            for s in students:
                if s["details"][0] == sid:

                    s["age"] = int(input("Enter New Age: "))

                    new_subjects = input("Enter New Subjects (comma separated): ")
                    s["subjects"] = set(new_subjects.split(","))

                    print("Student Updated Successfully!")
                    found = True

            if found == False:
                print("Student ID Not Found.")
        case 4:
            sid = input("Enter Student ID to Delete: ")

            found = False

            for i in range(len(students)):
                if students[i]["details"][0] == sid:
                    del students[i]
                    print("Student Deleted Successfully!")
                    found = True
                    break

            if found == False:
                print("Student ID Not Found.")
        case 5:
            all_subjects = set()
            for s in students:
                all_subjects.update(s["subjects"])

            print("\nSubjects Offered:")

            for sub in all_subjects:
                print(sub)

        case 6:
            print("\nThank You for using Student Data Organizer!")
            break

        case _:
            print("Invalid Choice! Try Again.")
