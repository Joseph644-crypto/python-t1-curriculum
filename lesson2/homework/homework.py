# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines.
num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number (non-zero): "))
quotient = num1 // num2
        remainder = num1 % num2
        print("Quotient)
        print("remainder")



# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
favorite_animal = input("What is your favorite animal? ").strip()
favorite_color = input("What is your favorite color? ").strip()
print("A light blue dog would be awsome!")


# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).
print("Even numbers from 0 to 10:")
for i in range(0, 11, 2):
    print(i, end="")




# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
try:
    pushups = int(input("How many push-ups can you do? "))
    if pushups < 0:
        print("Push-ups can't be negative!")
    else:
        total_week = pushups * 7
        print(f"In a week, you could do 7 push-ups in a week!")
except BalueError:
    print("Invalid input. Please enter a whole number.")



# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)
print("Squares from 1 to 6:")     
for i in range(1, 7):
    print(f"1*1=2, 2*2=4, 3*3=6")
