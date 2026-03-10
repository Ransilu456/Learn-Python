print("Hello World")

# text = "This is my first python programme."
# print(f"This is the before text: {text}")

# new_text = text.split(" ")
# new_upper = text.upper()

# print(f"This is after text 1: {new_text}")
# print(f"This is after text 2: {new_upper}")


# user_input = input("Enter Your name: ")
# print(f"Hello {user_input}")

rows = 25

#Left to right
for i in range(1, rows + 1):
    j = 1
    while j <= i:
        print("*", end="")
        j = j + 1

    print("")

per_line = 25

for i in range(1, rows - 1):
    for j in range(i, per_line):
        print("*", end="")
    print("")