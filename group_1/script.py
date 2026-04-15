# Workshop Script

def anagram(txt1, txt2):
    comp_a = [0] * 26
    comp_b = [0] * 26

    for i in range(len(txt1)):
        if 97 <= ord(txt1[i].lower()) <= 122:
            comp_a[ord(txt1[i].lower())-97] += 1

    for j in range(len(txt2)):
        if 97 <= ord(txt2[j].lower()) <= 122:
            comp_b[ord(txt2[j].lower())-97] += 1

    if comp_a == comp_b:
        return True
    else:
        return False

if __name__ == '__main__':
    print("Welcome to Geek Girls Conference!")
    txt1 = list(input())
    txt2 = list(input())
    print(anagram(txt1, txt2))
    # quid EST veritas?
    # Est vir qui adest?