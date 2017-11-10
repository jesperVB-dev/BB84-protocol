import random
Qbits = 2500
Done = False

def Keyexchange(Qbits):
    CorrectBits = []
    InCorrectBits = []

    ServerBits = []
    ServerEncrypters = []
    ServerPrivateKey = []
    ClientBits = []
    ClientDecrypters = []
    ClientPrivateKey = []

    EavesCheckServerBitsPrepare = []
    EavesCheckServerBits = []
    EavesCheckClientBitsPrepare = []
    EavesCheckClientBits = []

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
            InCorrectBits.append(i)

    #
    #   Send CorrectBits from Server to Client
    #

    for i in range(0, len(CorrectBits)):
        if CorrectBits[i] == 1:
            ClientPrivateKey.append(ClientBits[i])
        else:
            ClientDecrypters[i] = (ClientDecrypters[i] + 1) % 2

    #
    #   Check for Eavesdroppers from the Servers side
    #

    for i in range(0, len(InCorrectBits)):
        EavesCheckServerBitsPrepare.append(InCorrectBits[i])
        
    for i in range(0, len(EavesCheckServerBitsPrepare)):
        EavesCheckServerBits.append((ServerPrivateKey[EavesCheckServerBitsPrepare[i]%len(ServerPrivateKey)] + 1) % 2)
        
    #
    #   Send InCorrectBits to Client
    #

    for i in range(0, len(InCorrectBits)):
        EavesCheckClientBitsPrepare.append(InCorrectBits[i])
        
    for i in range(0, len(EavesCheckClientBitsPrepare)):
        EavesCheckClientBits.append((ClientPrivateKey[EavesCheckServerBitsPrepare[i]%len(ClientPrivateKey)] + 1) % 2)

    #
    #   Send EavesCheckClientBits to Server
    #

    return EavesCheckClientBits, EavesCheckServerBits

def main(Done):
    while Done != True:
        EavesCheckClientBits, EavesCheckServerBits = Keyexchange(Qbits)
        if (EavesCheckClientBits == EavesCheckServerBits):
            print("Key exchange complete!")
            Done = True
        else:
            print("Eavesdropper! Trying again.")
        
if __name__ == "__main__":
    main(Done)
