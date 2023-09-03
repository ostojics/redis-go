package main

import (
	"bufio"
	"fmt"
	"io"
	"net"

	redis_protocol "github.com/ostojics/redis-go/internal"
)

func handleConnection(conn net.Conn) {
	defer conn.Close()

	reader := bufio.NewReader(conn)

	for {
		value, err := redis_protocol.DecodeRESP(bufio.NewReader(reader))
		if err != nil {
			if err == io.EOF {
				fmt.Printf("Connection closed by client at address %s \n", conn.RemoteAddr().String())
				break
			}

			fmt.Println("Error decoding from connection: ", err.Error())
			return
		}

		command := value.Array()[0].String()
		args := value.Array()[1:]

		switch command {
		case "PING":
			conn.Write([]byte("+PONG\r\n"))
		case "ECHO":
			conn.Write([]byte(fmt.Sprintf("%s\r\n", args[0].String())))
		default:
			conn.Write([]byte("-ERR unknown command\r\n"))
		}

	}
}
