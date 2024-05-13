#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    
#arg w no default must contain arg when called
def greet(name):
    print(f"Hello, {name}!")

#this argument has default if arg not filled in
def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

#gives back value for added numbers
def add(num1, num2):
    return num1 + num2

#returns value of num / 2 
def halve(number):
    return number / 2
