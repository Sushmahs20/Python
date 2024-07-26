def filter_students_by_department(students, department):
    """This function takes two arguments, that is students(tuples in a list that contain name, department
    and registration number of a student) and department(name of department).
    This function checks for the department name and the input string argument(department), if department name
    matches it returns the student name and their registration number"""

    #filter the list of students based on their department
    filtered_students = [(name, reg_number) for name, reg_number, dept in students if dept.strip().lower() == department.strip().lower()]

    #check for the students present in the particular department
    if not filtered_students:
        #print appropriate error message if there are no students present in the given department
        print(f"No students found in the {department} department.")
    else:
        filtered_students_sorted = sorted(filtered_students, key=lambda x: x[1]) #sort students by registration number
        print("Name\t\tRegistration Number")
        #print one student per line, in a finely formatted table
        for name, reg_number in filtered_students_sorted:
            print(f"{name}\t\t{reg_number}")

    return filtered_students_sorted #return the students details sorted accordingly to their registration number

#define the main function
def main():
    try:
        #get user input for the file name
        file_name = input("Enter the file name: ")

        #read the file and create a list of tuples
        with open(file_name, 'r') as file:
            students = [tuple(line.strip().split(',')) for line in file]

        # display the list of tuples
        print("List of tuples:")
        print(students)

        while True:
            #get the user input for the department name
            department = input("\nEnter the name of a department (type 'quit()' to exit):")

            #break through the loop if the user input is 'quit'
            if department.lower() == 'quit':
                break

            # call the user defined function to display matching students of the user input department
            filter_students_by_department(students, department)

    except FileNotFoundError:
        #print appropriate error message if the file_name is incorrect or not found
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print("An error occurred: {e}")

if __name__ == "__main__":
    #Run the main function when the script is executed
    main()
