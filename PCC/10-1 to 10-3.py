from pathlib import Path

path = Path("PCC/learning_python.txt")

content1 = path.read_text()
print(content1)

content2 = content1.replace("Python", "C")

for line in content2.splitlines():
    print(line)