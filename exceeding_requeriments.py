def challenge1():
    data1 = input("Enter the first input: ")
    data2 = input("Enter the second input: ")
    result = data1 + data2
    print("Concatenated result:", result)

def challenge2():
    text = input("Enter a string: ")
    number = int(input("Enter an integer: "))
    result = text * number
    print("Repeated text:", result)

def challenge3():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Division by zero is not allowed."
    else:
        result = "Invalid operation."

    print("Result:", result)

def challenge4():
    number = int(input("Enter an integer: "))
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

def challenge5():
    grade1 = float(input("Enter the first grade: "))
    grade2 = float(input("Enter the second grade: "))
    grade3 = float(input("Enter the third grade: "))
    average = (grade1 + grade2 + grade3) / 3
    print("The average grade is:", average)

def challenge6():
    word = input("Enter a word: ")
    if word == word[::-1]:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome.")

# Main menu
while True:
    print("\n🧠 Python Challenges - Menu")
    print("1 - Concatenate Data 🐾")
    print("2 - Repeat Text ✏️")
    print("3 - Simple Math Operations 📐")
    print("4 - Check Even or Odd Numbers 🧮")
    print("5 - Calculate Grade Average 📚")
    print("6 - Check for Palindromes 🔄")
    print("0 - Exit")

    choice = input("Choose a challenge (0-6): ")

    if choice == '1':
        challenge1()
    elif choice == '2':
        challenge2()
    elif choice == '3':
        challenge3()
    elif choice == '4':
        challenge4()
    elif choice == '5':
        challenge5()
    elif choice == '6':
        challenge6()
    elif choice == '0':
        print("Exiting the program. See you next time! 👋")
        break
    else:
        print("Invalid option. Please try again.")