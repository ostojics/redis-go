import socket

def send_resp_command(sock, command_parts):
    command = command_parts[0]

    try:
        if command == 'PING':
            resp_command = f'*1\r\n$4\r\nPING\r\n'
        elif command == 'ECHO':
            arg = command_parts[1]
            resp_command = f'*2\r\n${len(command)}\r\n{command}\r\n${len(arg)}\r\n{arg}\r\n'
        elif command == 'SET':
            key = command_parts[1]
            value = command_parts[2]
            resp_command = f'*3\r\n$3\r\nSET\r\n${len(key)}\r\n{key}\r\n${len(value)}\r\n{value}\r\n'
        elif command == 'GET':
            key = command_parts[1]
            resp_command = f'*2\r\n$3\r\nGET\r\n${len(key)}\r\n{key}\r\n'

        sock.send(resp_command.encode())
        response = sock.recv(1024).decode()
        print("Server response:", response.strip())
    except Exception as e:
        print("Error:", str(e))

def main():
    server_address = ('localhost', 5000)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(server_address)

        while True:
            user_input = input("Enter a command (e.g., PING, SET key value, GET key, ECHO message, or exit): ")

            if user_input.lower() == 'exit':
                break

            command_parts = user_input.split()

            send_resp_command(client_socket, command_parts)
    except Exception as e:
        print("Error:", str(e))
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
