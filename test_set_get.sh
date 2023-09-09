#!/bin/bash

echo "Sending SET command"
echo -en "*3\r\n\$3\r\nSET\r\n\$5\r\nmykey\r\n\$7\r\nmyvalue\r\n" | nc -N -w1 127.0.0.1 5000

echo "Sending GET command"
echo -en "*2\r\n\$3\r\nGET\r\n\$5\r\nmykey\r\n" | nc -N -w1 127.0.0.1 5000
