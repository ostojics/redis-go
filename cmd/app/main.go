package main

import (
	"fmt"
	"net"
	"os"
)

func main() {
	l, err := net.Listen("tcp", fmt.Sprintf("%s", ":5000"))
	if err != nil {
		fmt.Println("Failed to bind to port 5000")
		os.Exit(1)
	}
	fmt.Println("Listening on port 5000")

	for {
		conn, err := l.Accept()
		if err != nil {
			fmt.Println("Error accepting connection: ", err.Error())
			os.Exit(1)
		}

		go handleConnection(conn)
	}
}
