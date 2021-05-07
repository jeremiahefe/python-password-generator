import random
from random import choice
def password_generator():
    combine_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz@$%&"
    enter_name = input("Enter name: ")
    password_len = int(input("Enter password length:"))
    password = ""
    request = 1
    while request:
        for n in range(0,password_len):
            pass_str = choice(combine_chars)
            password = password + pass_str
        print("{}".format(enter_name), "your password is ", password)
        request = 0
password_generator()
        
