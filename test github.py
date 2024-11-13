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



# Créé par quent, le 13/11/2024 en Python 3.7
####CODAGE####
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
message=input("Entrez le message à encoder : ")
decalage = int(input("Entrez le décalage pour l'encodage : "))
print(cesar_encode(message, decalage))

---------------------------------------TEST CODE ENTIER--------------------------------------

#####LETTRE CODEUSE#####
def lettre_codeuse(mot_codeur):
    deja_vu={}
    for letter in mot_codeur:
        if letter in deja_vu:
            position = ord(letter.lower())-ord('a') + 1
            return position
        deja_vu[letter]=True
    return print("Votre mot ne contient pas de lettre codeuse")

mot_codeur=input("Votre mot est:")
c=0
while c==0:
    try :
        mot_codeur=str(mot_codeur)
        c=1
    except :
        print("Veuillez entrer un mot")
        mot_codeur=input("Votre mot est:")

decalage=lettre_codeuse(mot_codeur)
print("Décalage :",decalage)


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
message_code = cesar_encode(message_clair, decalage)
print("Le message encodé est :", message_code)

