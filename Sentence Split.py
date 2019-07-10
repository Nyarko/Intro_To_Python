sentence = input("Type your sentence here: ")

def splitted():
    splitt = sentence.split()
    return splitt

print(splitted())


splitted = sentence.split()
for any in splitted:
    print("\n", any)