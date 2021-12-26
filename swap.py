def swap_case(s):
    out = ""
    for letter in s:
        if letter.isupper() == True:
            out+=(letter.lower())
        else:
            out+=(letter.upper())
    return out

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result()