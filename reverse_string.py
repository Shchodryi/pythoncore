def reverse(string):
    string = string.split((' '))
    string.reverse()
    string = ' '.join(string)
    return (string)
string = "please reverse this string"
print(reverse(string))