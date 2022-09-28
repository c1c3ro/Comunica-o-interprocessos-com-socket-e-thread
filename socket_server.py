from datetime import datetime
import socket
import threading

data_payload = 2048

def tratarDados(cliente):
    data = cliente.recv(data_payload)
    data = int(data.decode())
    now = datetime.now()
    response = ""
    if data == 1:
        dt_string = now.strftime("%d/%m/%Y")
        response = "A data é: " + dt_string
    elif data == 2:
        dt_string = now.strftime("%H:%M:%S")
        response = "A hora é: " + dt_string
    elif data == 3:
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        response = "A data/hora é: " + dt_string
    else:
        response = "Não entendi o que você disse."

    cliente.send(response.encode('utf-8'))
    cliente.close()

def server(host = 'localhost', port=8082):
    
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_address = (host, port)
    print ("Iniciando servidor na porta %s %s" % server_address)
    sock.bind(server_address)
    
    sock.listen(5)
    i = 0

    while True:
        print ("Esperando mensagem do cliente...")
        client, address = sock.accept()
        t1 = threading.Thread(target=tratarDados, args=(client,))
        t1.start()
        t1.join()

server()