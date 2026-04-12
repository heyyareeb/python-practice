import art
def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide (n1,n2):
    return n1 / n2


operation = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    print(art.logo)
    should_accumulate = True
    user_input1 = float(input("Enter first number: "))

    while should_accumulate:

        for symbol in operation:
            print(symbol)
        choose_operation = input("Pick an operation: ")

        user_input2= float(input("Enter Second number: "))
        answer = (operation[choose_operation](user_input1,user_input2))
        print (f"{user_input1} {choose_operation} {user_input2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with "
                       f"{answer}, or type 'n' "
              f"to start new calculation: ")

        if choice == "y":
            user_input1 = answer
        else:
            should_accumulate = False
            print("\n"* 20)
            calculator()

calculator()
