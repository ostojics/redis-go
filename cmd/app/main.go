package main

import (
	"fmt"
	"net"
	"os"
)

func main() {
	l, err := net.Listen("tcp", fmt.Sprintf("%s:%s", "0.0.0.0", "5000"))
	if err != nil {
		fmt.Println("Failed to bind to port 5000")
		os.Exit(1)
	}
	fmt.Println("Listening on port 5000")

	conn, err := l.Accept()
	if err != nil {
		fmt.Println("Error accepting connection: ", err.Error())
		os.Exit(1)
	}
	defer conn.Close()

	_, err = conn.Write([]byte("+PONG\r\n"))
	if err != nil {
		fmt.Println("Error writing to connection: ", err.Error())
		os.Exit(1)
	}
}
