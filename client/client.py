import socket
import argparse
from commands import *

def send_resp_command(sock, command_parts):
    command = command_parts[0]

    try:
        if command == 'PING':
            resp_command = make_ping_command()
        elif command == 'ECHO':
            arg = command_parts[1]
            resp_command = make_echo_command(arg)
        elif command == 'SET':
            key = command_parts[1]
            value = command_parts[2]
            resp_command = make_set_command(key, value)
        elif command == 'GET':
            key = command_parts[1]
            resp_command = make_get_command(key)

        sock.send(resp_command.encode())
        response = sock.recv(1024).decode()
        print(response.strip() + "\n")
    except Exception as e:
        print("Error:", str(e))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-port", "--port", help="Network port number",  type=int)
    args = parser.parse_args()
    port = args.port if args.port is not None else 5000

    server_address = ('localhost', port) 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect(server_address)

        while True:
            user_input = input("Enter a command \n PING\n SET key value \n GET key \n ECHO message \n exit: ")

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
