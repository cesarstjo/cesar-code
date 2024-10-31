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




#####DECODAGE######
def cesar_decode(message, decalage):
    resultat = ""
    for lettre in message:
        if lettre.isalpha():
            lettre = lettre.upper()
            offset = 65
            lettre_decodee = chr((ord(lettre) - offset - decalage) % 26 + offset)
            resultat += lettre_decodee
        else:

            resultat += lettre
    return resultat


print("=== Décodeur du chiffrement de César ===")
message_code = input("Entrez le message codé : ")
decalage = int(input("Entrez le décalage utilisé pour le codage : "))
message_decode = cesar_decode(message_code, decalage)
print("Le message décodé est :", message_decode)



#####CODAGE######
def cesar_encode(message, decalage):
    resultat = ""
    for lettre in message:
        if lettre.isalpha():
            if 'a' <= lettre <= 'z':
                lettre = chr(ord(lettre) - 32)

            offset = 65
            lettre_encodee = chr((ord(lettre) - offset + decalage) % 26 + offset)
            resultat += lettre_encodee
        else:

            resultat += lettre
    return resultat

print("=== Encodeur du chiffrement de César ===")
message_clair = input("Entrez le message à encoder : ")
decalage = int(input("Entrez le décalage pour l'encodage : "))
message_code = cesar_encode(message_clair, decalage)
print("Le message encodé est :", message_code)


