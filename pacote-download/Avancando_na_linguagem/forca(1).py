def jogar():
    print("*"*20)
    print("Bem vindo ao jogo da forca!")
    print("*"*20)

    palavra_secreta = "banana"
    letras_acertadas = ["_"*6]

    enforcou = False
    acertou = False
    #erros = 0

    # print(letras_acertadas)

    while(not enforcou and not acertou):
        
        chute = input("Qual é a letra?")
        chute =chute.strip()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                   print(f"Encontrei a letra {chute} na posição {index}") 
                index += 1
                #     letras_acertadas[index] = letra
                # index = index + 1
            print("Jogando")
    #     else:
    #         erros = erros + 1

    #     print(letras_acertadas)

    #     print("Fim do jogo")
    
    # if (__name__ == "__main__")

