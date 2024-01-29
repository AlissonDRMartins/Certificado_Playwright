
for line in open("output.txt", "r", encoding="utf-8"):
    a = "a"
    a += line
    file = open("new_output.txt", "a", encoding="utf-8")
    file.write(f"{a}")
    file.close()