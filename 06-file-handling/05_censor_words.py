word = "Donkey"
with open("file.txt", "r") as f:
    content = f.read()
contentNew = content.replace(word, "######")
with open("file.txt", "w") as f:
    f.write(contentNew)


words = ["Donkey", "bad", "ganda"]
with open("file.txt", "r") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#" * len(word))
with open("file.txt", "w") as f:
    f.write(content)