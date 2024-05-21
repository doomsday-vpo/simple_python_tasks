# Read an integer input from the user
number = int(input())

# Check the value of the entered number and print the corresponding message
if number < 100:
    print("Less than 100")
elif 100 <= number <= 200:
    print("Between 100 and 200")
else:
    print("Greater than 200")
