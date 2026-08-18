d = {}  # Empty dictionary
marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23
}
print(marks["Harry"])

marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}
print(marks.get("Harry2"))  # Prints None, safe lookup
# print(marks["Harry2"])    # KeyError: direct key access crashes if key missing