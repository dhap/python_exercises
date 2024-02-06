def disemvowel(string_):
    vowels = "aoieu"
    for a in vowels:
        string_ = string_.replace(a,'')
    return string_
print(disemvowel('aasssdd'))