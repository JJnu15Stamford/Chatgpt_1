# Define a constant for use in calculations
PI = 3.141592653589793  # The mathematical constant for π

# Function to calculate the area of a circle given a radius
def calculate_circle_area(radius):
    return PI * radius ** 2

# Function to check if a number is even or odd
def is_even_or_odd(number):
    return "even" if number % 2 == 0 else "odd"

# Function to read data from a file, calculate squares of numbers, and write to a file
def read_and_write_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            numbers = [int(line.strip()) for line in infile]
        
        with open(output_filename, 'w') as outfile:
            for number in numbers:
                outfile.write(f"{number} squared is {number ** 2}\n")
        print(f"Results written to {output_filename}")
    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except ValueError:
        print("Error: The file contains non-numeric data.")

# Function to safely take input and handle exceptions
def safe_input(prompt, conversion_type):
    try:
        return conversion_type(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

# Function for math operations with decision structure
def math_operations():
    print("Choose an operation:")
    print("1. Calculate the area of a circle")
    print("2. Check if a number is even or odd")
    print("3. Display squares of numbers up to a certain limit")
    print("4. Read numbers from a file and write squares to another file")
    
    choice = input("Enter the number of your choice (1/2/3/4): ")
    
    if choice == '1':
        radius = safe_input("Enter the radius of the circle: ", float)
        if radius is not None:
            area = calculate_circle_area(radius)
            print(f"The area of the circle with radius {radius} is {area:.2f}")
    elif choice == '2':
        number = safe_input("Enter a number to check if it is even or odd: ", int)
        if number is not None:
            print(f"{number} is {is_even_or_odd(number)}.")
    elif choice == '3':
        limit = safe_input("Enter the limit up to which to display squares: ", int)
        if limit is not None:
            print("Squares of numbers up to the limit:")
            for i in range(1, limit + 1):
                print(f"{i} squared is {i ** 2}")
    elif choice == '4':
        input_filename = input("Enter the name of the input file: ")
        output_filename = input("Enter the name of the output file: ")
        read_and_write_file(input_filename, output_filename)
    else:
        print("Invalid choice. Please choose a valid operation.")

# Main function to execute the program with repetition using a while loop
def main():
    while True:
        math_operations()
        continue_choice = input("Would you like to perform another operation? (yes/no): ").lower()
        if continue_choice != 'yes':
            print("Goodbye!")
            break

# Run the main function
main()
