try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have provided invalid input.  Please type numbers instead of spelling out your age.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
