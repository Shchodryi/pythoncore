def reverse(string):
    string = string.split((' '))
    string.reverse()
    string = ' '.join(string)
    return (string)
string = "re fg sjkjkjkd"
print(reverse(string))