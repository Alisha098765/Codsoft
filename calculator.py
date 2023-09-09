class Calculator:
    print("Basic Arithmetic Operations Calculator")  
    def __init__(self):
       while True: 
        try:
            self.a = int(input("Please Enter value1: "))
            self.operator = input("Please Enter operator: ")
            self.b = int(input("Please Enter value2: "))
            break
        except ValueError:
            print("Invalid input. Please enter correct type for value1 and value2.")
    def operation(self):
        if self.operator == '+':
            num = self.a + self.b
            print("Your Output is:", num)
        elif self.operator == '-':
            num = self.a - self.b
            print("Your Output is:", num)
        elif self.operator == '*':
            num = self.a * self.b
            print("Your Output is:", num)
        elif self.operator == '/':
            if self.b != 0:
                num = round(self.a / self.b , 3)
                print("Your Output is:", num)
            else:
                print("Error: Division by zero is not allowed")
        elif self.operator == '**':
            num = self.a ** self.b
            print("Your Output is:", num)
        else:
            print("Error: Invalid operator")
while True:
    cal = Calculator()
    cal.operation()
    choice = input("Do you want to calculate again? (continue/quit): ").lower()
    if choice != "c":
        break
print("Thanks! for using Calculator")
        

