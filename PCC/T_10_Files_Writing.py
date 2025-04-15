from pathlib import Path

path = Path("PCC/writing.txt")

contents = "I love programming.\n"
contents += "I love building software.\n"
contents += "I also love translation.\n"

path.write_text(contents)