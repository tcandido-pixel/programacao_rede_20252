#importa o modulo socket do python
import socket

#A função socket do modulo socket cria um objeto socket
#socket.AF_INET configura o socket para trabalhar com IPV4
#socket.SOCK_STREAM configura o socket para trabalhar o TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#A função bind cria um vinculo entre uma maquina e uma porta TCP
servidor.bind(("127.0.0.1", 5000))

#A função listen habilita socket a ouvir pedidos de conexão
servidor.listen()

print("Esperando uma conexão!!!")

#A função accept aceita conexões devolvendo um objeto de conexão com o cliente 
#e o endereço do cliente
conn, address = servidor.accept()
print("Endereço do clinte: ", address)

#A função recv recebe a mensagens do cliente conectado (até 1024 bytes ou o vslor configurafo)
mensagem = conn.recv(1024)
print("Mensagem recebida: ", mensagem.decode())


conn.sendall("Mensagem recebida com sucesso")