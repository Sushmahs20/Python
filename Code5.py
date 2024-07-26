import numpy as np

#Defining a named data type
dtype = np.dtype([('reg_number', int), ('exam', float), ('coursework', float), ('overall', float), ('grade', 'U10')])

def calculate_overall(exam, coursework, weighting):
    """This function takes three arguments exam, coursework and weighting to computes and returns the overall marks"""
    return round((exam * (1 - weighting / 100)) + (coursework * (weighting / 100))) #returns the roundoff of overall marks

def calculate_grade(overall):
    """This function takes overall marks computed from the defined function calculate_overall()
    and returns the appropriate grades according to the coursework, exam score and overall score obtained"""
    if overall < 30:
        return 'Fail'
    elif overall >= 70:
        return 'First'
    elif 50 <= overall <= 69:
        return 'Second'
    elif 40 <= overall <= 49:
        return 'Third'
    else:
        return 'Fail'

#define the main function
def main():
    try:
        #get user input for the file name
        file_name = input("Enter the file name: ")
        #open and read the file
        with open(file_name, 'r') as file:
            #read the first line to get the number of students and coursework weighting
            num_of_students, coursework_weighting = map(int, file.readline().split())

            #initialize the first array with zeroes
            array1 = np.array([[0, 0.0, 0.0, 0.0]] * num_of_students)

            #iterate to read the remaining lines to populate the first array
            for i in range(num_of_students):
                reg_number, exam, coursework = map(float, file.readline().split())
                #compute overall score with define function calculate_overall()
                overall = calculate_overall(exam, coursework, coursework_weighting)
                #assign values to array1 for every i-th of the total number of students in the file
                array1[i] = [reg_number, exam, coursework, overall]

            #define the second array with the named data type
            array2 = np.array([(0, 0.0, 0.0, 0.0, "")] * num_of_students, dtype=dtype)

            #populate the second array with calculated grades
            for i in range(num_of_students):
                #get the values from array1 for every i-th student in the file
                reg_number, exam, coursework, overall = array1[i]
                #round off the overall marks to the nearest integer
                rounded_overall = round(overall)
                #compute overall score with define function calculate_grade()
                grade = calculate_grade(rounded_overall)
                #create a tuple with student information and append its values to array2
                array2[i] = (int(reg_number), exam, coursework, rounded_overall, grade)

            #sort the second array by overall mark
            sortedArray2 = np.sort(array2, order='overall')

            #create a output file
            outputFile = input("Enter the output file name: ")
            #print the sorted array to the output file
            with open(outputFile, 'w') as outFile:
                print(sortedArray2, file=outFile)

            #display statistics
            first_class = np.count_nonzero(array2['grade'] == 'First')
            second_class = np.count_nonzero(array2['grade'] == 'Second')
            third_class = np.count_nonzero(array2['grade'] == 'Third')
            fail = np.count_nonzero(array2['grade'] == 'Fail')

            print("\nStatistics:")
            print(f"First class: {first_class}")
            print(f"Second class: {second_class}")
            print(f"Third class: {third_class}")
            print(f"Fail: {fail}")

            #display registration numbers of students who have failed
            failed_students = array2[array2['grade'] == 'Fail']
            print("\nRegistration numbers of students who have failed:")
            print(failed_students['reg_number'])

    except FileNotFoundError:
        #print appropriate error message if the file_name is incorrect or not found
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    #Run the main function when the script is executed
    main()
