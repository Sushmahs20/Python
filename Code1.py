from datetime import date

def get_user_input():
    """This function returns the user input of the date of b in dd/mm/yyyy format."""
    while True:
        try:
            #accepts date of b input from the user in the format dd/mm/yyyy
            user_input = input("Enter your date of the birth in the format (dd/mm/yyyy): ")
            #split the date of b with '/' and maps it to day, month, year respectively
            day, month, year = map(int, user_input.split('/'))
            return day, month, year #returns the date, month and year of date of b
        except ValueError:
            #print error message if the user input of date of b entered is not in prescribed format of dd/mm/yyyy
            print("Invalid date format. Please use the format dd/mm/yyyy.")

def compute_age(date_of_the_birth, present_date):
    """We take two parameters, date_of_the_birth ( date of birth entered by the user) and present_date.
    We determine the user's age based on the date of the birth and the present date and return the present age."""

    #assign b date, month and year from the user input
    b_day, b_month, b_year = date_of_the_birth
    #assign present date, month and year derived from the datetime module of library date
    present_day, present_month, present_year = present_date

    #compute the difference between present date and b date to obtain the age
    age = present_year - b_year - ((present_month, present_day) < (b_month, b_day))
    return age #returns the present age of the user

#define the main function
def main():
    try:
        #get the present date
        present_date = date.today()
        #get date of birth from user input
        date_of_the_birth = get_user_input()
        #check if the entered dob is valid
        if not (1 <= date_of_the_birth[0] <= 31 and 1 <= date_of_the_birth[1] <= 12 and 1900 <= date_of_the_birth[2] <= present_date.year):
            #print appropriate error message if the date of b is invalid
            print("Invalid date. Please enter a valid date.")
            return
        #compute age using the defined function
        age = compute_age(date_of_the_birth, (present_date.day, present_date.month, present_date.year))

        #Check if its the users bday and print the appropriate message with the present age
        if (present_date.day, present_date.month) == (date_of_the_birth[0], date_of_the_birth[1]):
            print("HAPPIEST BIRTHDAY TO YOU!")
            if age == 0:
                print("You are 1 year old today!")
            else:
                print(f"You are now {age} years old.")

        else:
            print(f"Your age is: {age}")

    except KeyboardInterrupt:
        #handling termination of program by the user
        print("\nProgram terminated by the user.")

if __name__ == "__main__":
    #Run the main function when the script is executed
    main()
