#!/usr/bin/env python3
def readFile():
    with  open('numfile.txt',"r") as nums:
        numList = nums.readlines()
        return  numList
def parse(numbers):
    for num in numbers:
        num = int(num)
        if num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
def main():
    parse(readFile())
    



if __name__ == "__main__":
    main()
