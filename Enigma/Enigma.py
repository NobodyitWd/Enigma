def Transform(ciphertext):
    for i in range(len(ciphertext)):
        ciphertext[i] = ciphertext[i]%len(alpha)
        ciphertext[i] = alpha[ciphertext[i]]
    return ciphertext

alpha = r"ABCDEFGHIJKLMNOPQRSTUVWXYZ АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ!?=-+=@1234567890*/()^%,.:;[]'\""
key = []
originalMessage = ""

print("The key must consist of 5 characters.")
keyinp = input("Input key:    ")
if len(keyinp) != 5:
    print("The key must consist of 5 characters.\n")

else:
    converter = []
    message = input("Input message:    ")
    message = message.upper()
    keyinp = keyinp.upper()
    for i in keyinp:
        if i in alpha:
            key.append(i)
        else:
            print("Uncorrect key.")
            exit(0)

    for i in message:
        if i not in alpha:
            message = message.replace(i,"")

    for i in range(len(message)):
        converter.append(alpha.index(message[i]))


    ciphertext = ([0]*len(message))
    i = 0
    for l in range(len(alpha)):
        keyl = alpha.index(key[4]) + l
        for k in range(len(alpha)):
            keyk = alpha.index(key[3]) + k
            for z in range(len(alpha)):
                keyz = alpha.index(key[2]) + z
                for x in range(len(alpha)):
                    keyx = alpha.index(key[1]) + x
                    for y in range(len(alpha)):

                        if i != len(message):

                            oldkey = (alpha.index(key[0]) + y)
                            keyy = (alpha.index(key[0]) + y + keyx + keyz + keyk + keyl) % len(alpha)

                            ciphertext[i] = alpha.index(message[i]) + keyy
                            originalMessage += alpha[(converter[i] - oldkey - keyx - keyz - keyk - keyl) % len(alpha)]

                            i += 1
                        else:
                            print("ciphertext:    " + "".join(Transform(ciphertext)))
                            print("mess:    " + originalMessage)
                            exit(0)

    print("".join(Transform(ciphertext)))
    print(originalMessage)
