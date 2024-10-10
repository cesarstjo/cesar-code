# Créé par elevessi, le 10/10/2024 en Python 3.7
def codage():
    txt=input("entrez une phrase")
    txt=[txt]
    global code
    global num
    for letter in txt:
        num=ord(letter)
    [txt]=txt
    code=str.upper(txt)
    return code
    return num
codage()
print(code)
print(num)
