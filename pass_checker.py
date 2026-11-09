num_and_special = "1 2 3 4 5 6 7 8 9 0 ! @ # $ % ^ & * ( )".split()
passw = input("Enter your password that must include numbers and special characters: ")
if num_and_special not in passw:
    print("Your password must include numbers and special characters")
else:
    print("Your password is correct")


