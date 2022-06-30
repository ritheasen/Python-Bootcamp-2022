
userAge = int(input("Input your age: "))

if userAge < 0 :
    print("Age must be positive digit")
elif userAge >= 0 and userAge < 18:
    print("You aren't adult yet... Sorry can't vote")
else:
    print("You are eligible to vote")





