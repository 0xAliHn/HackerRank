def capitalize(string):
    s = string.split(" ")
    st = ""
    for i in range(len(s)):
        st += s[i].capitalize()+" "
    return st
    #' '.join(i.capitalize() for i in string.split(' '))
