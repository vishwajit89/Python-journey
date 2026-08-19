words = {
    "madad": "Help",
    "kursi": "Chair",
    "billi": "Cat"
}
word = input("Enter the word you want meaning of: ")
print(words[word])

s = set()
s.add(20)
s.add(20.0)
s.add('20')  # length of s after these operations?
print(len(s))  # prints 2 -> 20 and 20.0 are treated as the same value in a set, '20' (string) is different

d = {}
for _ in range(4):
    name = input("Enter friends name: ")
    lang = input("Enter Language name: ")
    d.update({name: lang})
print(d)

# s = {8, 7, 12, "Harry", [1, 2]}
# s[4][0] = 9
# TypeError: unhashable type: 'list' -> sets can only hold immutable elements, lists can't go inside a set