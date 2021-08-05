#!/usr/bin/env python3
def operate(operation,x,y):
    answer = 0
    

        answer = x + y
    elif(operation == "subtract"):
        answer = x-y
    elif(operation == "divide"):
        if y != 0:
            answer = x/y
        else:
            print("You can't divide by zero!")
    elif(operation == "multiply"):
        answer = x*y
    else:
        print("use a valid OPERATION")
    print( answer)
def main():
    while True:
        try:
            x = float(input("Enter in a number: "))
            y= float(input("Enter ANOTHER  number: "))
            break
        except:
            print("Invalid input, try again.")
    operation = ""
    while(operation != "add" and operation != "subtract" and operation != "divide" and operation != "multiply"):
        operation = input("What operation would like to perform? OPTIONS: 'add', 'subtract','divide','multiply': ").lower()
    operate(operation,x,y)
if __name__ == "__main__":
    main()
