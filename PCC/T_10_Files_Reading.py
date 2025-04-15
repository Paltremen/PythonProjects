from pathlib import Path

path = Path("D:/PythonProjects/PCC/pi_million.txt") # reads only the root unless directory is specified
contents = path.read_text() # method chaining

birthday = input("Enter your birthday in the format ddmmyy: ")
if birthday in contents:
    print("Your birthday is in the first million digits of pi!")
else:
    print("Well, tough luck!")