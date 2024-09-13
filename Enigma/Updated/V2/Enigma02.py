alpha = r"A!B?C=D-E+F@G1H2I3J4K5L6M7N8O9Я0Э*Ы/Щ(Ч)Х^У%С,П.Н:Л А;Б[В]Г'Д\Е$Ё>Ж<З#И&Й_КZМYОXРWТVФUЦTШSЪRЬQЮP"
def Transform(ciphertext): # Переобразуем числа в буквы.
    for i in range(len(ciphertext)):
        ciphertext[i] = ciphertext[i]%len(alpha)
        ciphertext[i] = alpha[ciphertext[i]]
    return ciphertext
def Handler(boole):
    c = ""
    c1 = Core(message1, key1)
    c2 = Core(message2, key2)

    i = 0
    while i != len(c1[0]): # Вернем два сообщения в одно.
        c += c1[boole][i]
        c += c2[boole][i]
        i+=1
    return c
def Core(message,keyinp):
    key = []
    originalMessage = ""

    if len(keyinp) != 5:
        print("The key must consist of 5 characters.\n")
        exit(0)
    else:
        converter = []

        message = message.upper()
        keyinp = keyinp.upper()

        for i in keyinp: # Если символа ключа нет в алфавите: завершить работу программы.
            if i in alpha:
                key.append(i)
            else:
                print("Uncorrect key.")
                exit(0)

        for i in message: # Если символа сообщения нет в алфавите: удалить символ.
            if i not in alpha:
                message = message.replace(i,"")

        for i in range(len(message)): # Переобразуем ИЗНАЧАЛЬНОЕ сообщение из текста в числа.
            converter.append(alpha.index(message[i]))


        ciphertext = ([0]*len(message)) # Шифро текст. Длинною в сообщение. Пока что из нулей.
        i = 0
        for l in range(len(alpha)): # Валы "Энигмы" (шифраторы). Принцип работы есть в иных источниках.
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
                                keyy = (oldkey + keyx + keyz + keyk + keyl) % len(alpha) # V = (Прибавим положение каждого вала, и поделем по модулю длинны алфавита).

                                ciphertext[i] = alpha.index(message[i]) + keyy # Текущее сообщение + V = шифротекст.
                                originalMessage += alpha[(converter[i] - oldkey - keyx - keyz - keyk - keyl) % len(alpha)] # Все тоже самое но наоборот и с ИЗНАЧАЛЬНЫМ сообщением.

                                i += 1
                            else:
                                return ("".join(Transform(ciphertext))), (originalMessage)

print("The key must consist of 5 characters.")
key1 = input("Input key1:    ")
key2 = input("Input key2:    ")

mess = input("Input message:    ")

if len(mess)%2!=0: # Если количество символов в сообщении не четно: добавь в конец сообщения последний символ.
    mess+=mess[-1]

message1 = ""
message2 = ""

for i in range(len(mess)): # Разделим одно сообщение на два других, по четности.
    if i % 2 == 0:
        message1 += mess[i]
    else:
        message2 += mess[i]

print("Ciphertext:    "+Handler(0)+"\n"+"Message:    "+Handler(1))

# В одном сообщении возможно зашифровать не более 16307453952 символов.
# Количество возможных комбинаций ключей 66483263599150104576-1 Или 96 в 10той степени минус 1.
# Не при каких обстоятельствах, не создавайте одинаковые ключи!
# Символы ключей желательно должны быть различны. Однако их повторение в размных пропорциях могут обеспечить больше криптостойкости.
# Советую создать ключи из неосмысленных символов. Сочетайте их с ру\en алфавитом. Это повысит криптостойкость.