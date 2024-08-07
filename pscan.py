import socket

ip = input("Digite o host ou IP a ser verificado: ") #Para o cliente definir o host

ports = []
count = 0

while count < 2:
    ports.append(int(input("Digite a Porta a ser verificado: ")))  # Port que quer varrer
    count += 1

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET para dizer que trabalharemos com IPV4 e SOCK_STREAM para usarmos TCP/IP
    client.settimeout(0.05) #Definindo tempo de resposta da chamada TCP
    code = client.connect_ex((ip, port)) #Receber código da transação TCP (TCP_SOCKET_ERROR)

    if code == 0:
        print(str(port), "-> Porta aberta")
    else:
        print(str(port), "-> Porta fechada")

print("Scan finalizado!")

