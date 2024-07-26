def is_prime(num):
    """This funtion takes integer 'num' as argument and returns True if the number is prime, False otherwise"""
    if num < 2:
        return False
    #check for the factors till the square root of the integer 'num'
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_number(start, end):
    """This function takes two arguements, start and end of the range,
    and generates the list of prime numbers between the range"""
    primes = [num for num in range(start, end + 1) if is_prime(num)] #check for prime number using the defined function
    return primes #returns the list of prime numbers

def get_user_input():
    """This function returns the user inputs of two positive numbers for the start
    and end of the range prime numbers to be generated"""
    while True:
        try:
            input_1 = int(input("Please enter the first positive integer: "))
            input_2 = int(input("Please enter the second positive integer: "))
            if input_1 > 0 and input_2 > 0:
                #returns the start(minimum of the inputs 1 and 2) and the end(maximum of the inputs 1 and 2) of the range
                return min(input_1, input_2), max(input_1, input_2)
            else:
                #print warning message if non positive integers are entered by user
                print("Please enter positive integers.")
        except ValueError:
            #print appropriate error message if invalid input is entered
            print("Invalid input. Please enter valid positive integers.")

#define the main function
def main():
    try:
        start, end = get_user_input() #get start and end of the range from user input
        primes = generate_prime_number(start, end) #generate prime numbers between the range using the defined function

        print("\nPrime numbers between", start, "and", end, "are:")
        #print the prime numbers generated as 10 prime numbers per each output line
        for i, prime in enumerate(primes, start=1):
            print(prime, end='\t')
            if i % 10 == 0:
                print()

    except KeyboardInterrupt:
        #handling termination of program by the user
        print("\nProgram terminated by the user.")

if __name__ == "__main__":
    #Run the main function when the script is executed
    main()
