f = open("file.txt", "r")
data = f.read()
print(data)
f.close()


st = "Hey Harry you are amazing"
f = open("myfile.txt", "w")
f.write(st)
f.close()


f = open("file.txt")
line = f.readline()
while line != "":
    print(line)
    line = f.readline()
f.close()


st = "Hey Harry you are amazing"
f = open("myfile.txt", "a")
f.write(st)
f.close()