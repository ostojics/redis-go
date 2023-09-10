package main

import (
	"flag"
	"fmt"
	"net"
	"os"

	"github.com/ostojics/redis-go/internal/storage"
)

func main() {
	port := flag.String("port", ":5000", "network port")
	flag.Parse()

	l, err := net.Listen("tcp", *port)
	if err != nil {
		fmt.Printf("Failed to bind to port %s", *port)
		os.Exit(1)
	}
	fmt.Printf("Listening on port %s \n", *port)

	storage := storage.NewStorage()

	for {
		conn, err := l.Accept()
		if err != nil {
			fmt.Println("Error accepting connection: ", err.Error())
			os.Exit(1)
		}

		go handleConnection(conn, storage)
	}
}
