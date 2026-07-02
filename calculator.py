print("=== Simple Calculator ===")
print("Operation: +(add), -(subtract), *(multiply), /(divide)")
print("type 'exit' to quit the calculator")

while True:
    #get the first number
    user_input1 = input("Enter the first number: (or exit to quit): ")
    if user_input1.lower() == 'exit':
        break
    num1=float(user_input1)

    #get the mathematical operation
    operation = input("Enter the operation: ").strip()
    if operation.lower() == 'exit':
        break

    #get the second number
    user_input2 = input("Enter the second number: ")
    if user_input2.lower() == 'exit':
        break
    num2=float(user_input2)

    #perform the calculation based on the operation
    if operation == '+':
        result = num1 + num2   
        print(f"The result of {num1} + {num2} is: {result}\n") 
    elif operation == '-':
        result = num1 - num2    
        print(f"The result of {num1} - {num2} is: {result}\n")
    elif operation == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}\n")
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}\n")
    else:
        print("Invalid operation. Please try again.")
        continue

    