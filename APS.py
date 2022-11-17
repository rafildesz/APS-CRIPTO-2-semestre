# Alfabeto de criptografia
alfabeto_e = {'a': '01','b': '02','c': '03','d': '04','e': '05','f': '06','g': '07','h': '08','i': '09','j': '10','k': '11','l': '12','m': '13','n': '14','o': '15','p': '16','q': '17','r': '18', 's': '19','t': '20','u': '21','v': '22','w': '23','x': '24','y': '25','z': '26',' ': '27', 'á': '28', 'à': '29', 'â': '30', 'ã': '31', 'è': '32', 'é': '33', 'ê': '34', 'ç': '35', 'ì': '36', 'í': '37', 'ó': '38', 'ò': '39', 'ô': '40', 'õ': '41', 'ù': '42', 'ú': '43', '?': '44', '!': '45', ',': '46', '0': '47', '1': '48', '2': '49', '3': '50', '4': '51', '5': '52', '6': '53', '7': '54', '8': '55', '9': '53'}

# Alfabeto de descriptografia
alfabeto_d = {n: c for c, n in alfabeto_e.items()}


# Algoritmo Euclidiano: encontre o GCD de dois numeros
def gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)


# Gerar chaves de criptografia, e & d
def gerar_chaves(p, q):
    # Parte da chave publica
    global e, d
    n = p * q

    # Parte da chave privada
    n0 = (p - 1) * (q - 1)

    # Parte da chave publica
    # Encontre e: primeiro inteiro relativamente primo de n0
    for i in range(2, n0):
        if gcd(i, n0) == 1:
            e = i
            break

    # Parte da chave privada
    # Encontre d: inverso multiplicativo de e % n0
    for i in range(0, n0):
        if ((e * i) % n0) == 1:
            d = i
            break

    return n, e, d
# Criptografar caractere
def criptografar(char, n, e):
    return str((int(char) ** e) % n).zfill(2)


# Descriptografar caractere
def descriptografar(char, n, d):
    return str((int(char) ** d) % n).zfill(2)


# Divida a palavra em caracteres
def dividir(palavra):
    return [char for char in palavra]


# Criptografar mensagem
def criptografar_mensagem(msg, n, e):

    # Mensagens
    textosimples = msg.lower().split()
    criptografado = []

    # criptografar mensagem
    for palavra in textosimples:

        # Dividir palavra em caracteres
        caractere = dividir(palavra)

        # Criar lista de caracteres criptografados
        criptografar_caractere = [criptografar(alfabeto_e[char], n, e) for char in caractere]

        # Adicionar palavra criptografada à lista
        palavra_criptografada = " ".join(criptografar_caractere)
        criptografado.append(palavra_criptografada)

    # Junte palavras criptografadas com caracteres especiais
    criptografado= f" {criptografar(alfabeto_e[' '], n, e)} ".join(criptografado)

    return criptografado

# Descriptografar mensagem
def descriptografar_mensagem(msg, N, d):
    # Mensagens
    criptografado = msg.split()
    descriptografado = []
    textosimples = []

    # descriptografar
    for char in criptografado:
        descriptografado.append(descriptografar(char, N, d))

    # Decifrar mensagem
    for char in descriptografado:
        textosimples.append(alfabeto_d[char])

    textosimples = "".join(textosimples)

    return textosimples
# Menu de opçoes dividir
def opcoes():
    print("opçoes:\n\
        0 - Gerar par de chaves\n\n\
        1 - Criptografar mensagem no terminal\n\
        2 - Descriptografar mensagem no terminal\n")


# Interface usuario
while True:

    # Mostrar opçoes
    opcoes()

    # obter seleçao de usuario
    selecao = input()

    # gerar par de chaves
    if selecao == "0":

        # entre com numeros primos
        p = int(input("Entre com o primeiro numero primo: "))
        q = int(input("Entre com o segundo numero primo: "))
        print()

        try:
            # Gerar valores para criptografia/descriptografia
            N, e, d = gerar_chaves(p, q)

            # mostrar chaves
            print(f"Chave publica:\nN: {N}\ne: {e}\n")
            print(f"Chave privada:\nN: {N}\nd: {d}\n")

        except:
            print("Erro: numeros primos invalidos\n")

    # Criptografar mensagem no terminal
    elif selecao == "1":

        # Obter chave publica
        N = int(input("Entre com a chave publica N: "))
        e = int(input("Entre com a chave publica e: "))
        print()

        # Receber mensagem do usuário
        mensagem = input("Digite a mensagem para criptografar: \n")

        # Imprimir mensagem criptografada
        print(f"\nMensagem criptografada:\n{criptografar_mensagem(mensagem, N, e)}\n")

    # Descriptografar mensagem no terminal
    elif selecao == "2":

        # Obter chave privada
        N = int(input("Entre com a chave privada N: "))
        d = int(input("Entre com a chave privada d: "))
        print()

        # Obter mensagem criptografada do usuário
        mensagem = input("Digite a mensagem para descriptografar:\n")

        # Imprimir mensagem descriptografada
        try:
            print(f"\nMensagem descriptografada:\n{descriptografar_mensagem(mensagem, N, d)}\n")

        except:
            print("Erro: chave privada inválida\n")

    # Validação de entrada
    else:
        print("Escolha inválida\n")

    # Opção para sair
    sair = input("Fazer outra seleção?\n\
        'S' para continuar\n\
        qualquer outra tecla para sair\n").upper()

    print()

    # Faça outra seleção
    if sair == "S":
        continue

    # sair
    else:
        break

