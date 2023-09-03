package main

import (
	"fmt"
	"net"
	"os"
)

func handleConnection(conn net.Conn) {
	defer conn.Close()
	buf := make([]byte, 1024)

	for {
		req, err := conn.Read(buf)
		fmt.Println("Received: ", string(buf[:req]))

		if err != nil {
			fmt.Println("Error reading from connection: ", err.Error())
			os.Exit(1)
		}

		_, err = conn.Write([]byte("+PONG\r\n"))
		if err != nil {
			fmt.Println("Error writing to connection: ", err.Error())
			os.Exit(1)
		}
	}
}
