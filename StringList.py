string = input("Enter a string: \n")
if string.__len__() % 2 == 0:
    print(string + " is not a palindrome.")
else:
    middle = string.__len__() / 2
    middle = int(middle)
    str1 = string[:middle]
    str2 = string[middle + 1:]
    if str1.__eq__(str2):
        print(string + " is a palindrome")
    else:
        print(string + " is not a palindrome")
