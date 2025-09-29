while True:
 
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    print("\nChoose the operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == "1":
        print(f"Result: {num1 + num2}")
    elif choice == "2":
        print(f"Result: {num1 - num2}")
    elif choice == "3":
        print(f"Result: {num1 * num2}")
    elif choice == "4":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice! Please choose 1, 2, 3, or 4.")
    again = input("\nDo you want to calculate again? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break
