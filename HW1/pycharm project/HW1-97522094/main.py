import re

# Q1
def CheckPattern(text):
    ## patterns
    if re.search("Doctor(((\s)([A-Z](\.))+)|((\s)[A-Z][a-z]*-[A-Z][a-z]*)|((\s)[A-Z][a-z]*))+", text):
        return True
    elif re.search("Dr(\.)(((\s)([A-Z](\.))+)|((\s)[A-Z][a-z]*-[A-Z][a-z]*)|((\s)[A-Z][a-z]*))+", text):
        return True
    elif re.search(
            "((([A-Z](\.))+)|([A-Z][a-z]*)|([A-Z][a-z]*-[A-Z][a-z]*))(((\s)([A-Z](\.))+)|((\s)[A-Z][a-z]*-[A-Z][a-z]*)|((\s)[A-Z][a-z]*))+,? M\.D\.",
            text):
        return True
    else:
        return False


file_address = input("Enter File Address: ")
file1 = open(file_address, 'r')
Lines = file1.readlines()
for line in Lines:
    print(f"Text: {line.strip()}")
    result = CheckPattern(line)
    if result:
        print("Matched Pattern Successfully! True")
    else:
        print("Wrong Text! False")
    print("")
    print("////////////////////////")
    print("")


