f = open("poem.txt")
content = f.read()
if "twinkle" in content:
    print("The word twinkle is present in the content")
else:
    print("The word twinkle is not present in the content")
f.close()


with open("log.txt") as f:
    content = f.read()
if "python" in content:
    print("Yes python is present")
else:
    print("No Python is not present")


with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "python" in line:
        print(f"Yes python is present. Line no: {lineno}")
        break
    lineno += 1
else:
    print("No Python is not present")


with open("this.txt") as f:
    content = f.read()
with open("this_copy.txt", "w") as f:
    f.write(content)


with open("this.txt") as f:
    content1 = f.read()
with open("this_copy.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("Yes these files are identical")
else:
    print("No these files are not identical")