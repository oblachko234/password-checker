special = set("!@#$%^&*()")
num = set("0123456789")
passw = input("Enter your password that must include numbers and special characters: ")
if special.isdisjoint(passw) and num.isdisjoint(passw):
    print("Your password must include numbers and special characters")
else:
    print("Your password is correct")


