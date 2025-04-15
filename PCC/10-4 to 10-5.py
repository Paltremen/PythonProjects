from pathlib import Path

path = Path("PCC/users.txt")

userstring = ""

while True:
    print(f"Enter your name. Type 'quit' to quit.")
    nameinput = input("Please enter your name: ")
    if "quit" in nameinput:
        break
    else:
        userstring += f"{nameinput}\n"

path.write_text(userstring)