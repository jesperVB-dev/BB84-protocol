import random
Qbits = 500

ServerBits = []
ServerEncrypters = []
ServerPrivateKey = []
ClientBits = []
ClientDecrypters = []
ClientPrivateKey = []
CorrectBits = []

#generate Random Server Bits

for i in range(0,Qbits):
    if random.randint(0, 1) == 0:
        ServerEncrypters.append(0)
    else:
        ServerEncrypters.append(1)
        
    if random.randint(0, 1) == 0:
        ServerBits.append(0)
    else:
        ServerBits.append(1)

#
#   Sends Qbits to client
#

for i in range(0,Qbits):
    if random.randint(0, 1) == 0:
        ClientDecrypters.append(0)
    else:
        ClientDecrypters.append(1)
        
    if random.randint(0, 1) == 0:
        if ServerEncrypters[i] == ClientDecrypters[i]:
            ClientBits.append(ServerBits[i])
        else:
            ClientBits.append(random.randint(0, 1))
    else:
        if ServerEncrypters[i] == ClientDecrypters[i]:
            ClientBits.append(ServerBits[i])
        else:
            ClientBits.append(random.randint(0, 1))

#
#   Send ClientDecrypters to Server
#

for i in range(0, len(ServerEncrypters)):
    if ServerEncrypters[i] == ClientDecrypters[i]:
        ServerPrivateKey.append(ServerBits[i])
        CorrectBits.append(1)
    else:
        CorrectBits.append(0)        

#
#   Send CorrectBits from Server to Client
#
for i in range(0, len(CorrectBits)):
    if CorrectBits[i] == 1:
        ClientPrivateKey.append(ClientBits[i])

print(ServerPrivateKey)
print(ClientPrivateKey)


