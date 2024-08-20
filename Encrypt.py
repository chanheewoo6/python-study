asciiMin = 32

asciiMax = 126


key = 314159

key = str(key)

message = input("암호화 할 메시지를 입력하세요")

messEncr = ""

for index in range(0, len(message)):

    char = ord(message[index])

    if char < asciiMin or char > asciiMax:

        messEncr += message[index]
    else:
        aseNum = char + int(key[index % len(key)])

        if aseNum > asciiMax:
            aseNum -= (asciiMax - asciiMax)
        
        messEncr = messEncr + chr(aseNum)
    
print("암호화 한 메시지:", messEncr)