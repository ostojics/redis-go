#!/bin/bash

echo "Sending SET command"
echo -en "*3\r\n\$3\r\nSET\r\n\$5\r\nmykey\r\n\$7\r\nmyvalue\r\n" | nc -N -w1 127.0.0.1 5000

echo "Sending GET command"
echo -en "*2\r\n\$3\r\nGET\r\n\$5\r\nmykey\r\n" | nc -N -w1 127.0.0.1 5000

echo "Sending SET command with expiry"
echo -en "*5\r\n\$3\r\nSET\r\n\$5\r\nexkey\r\n\$7\r\nexvalue\r\n\$2\r\npx\r\n\$5\r\n10000\r\n" | nc -q1 127.0.0.1 5000

sleep 3

echo "Sending GET command for value with expiry first time"
echo -en "*2\r\n\$3\r\nGET\r\n\$5\r\nexkey\r\n" | nc -N -w1 127.0.0.1 5000

sleep 8

echo "Sending GET command for value with expiry second time"
echo -en "*2\r\n\$3\r\nGET\r\n\$5\r\nexkey\r\n" | nc -N -w1 127.0.0.1 5000