#!/bin/bash

for i in {1..5}; do
    echo "Sending request $i"
    echo -en "*2\r\n\$4\r\nECHO\r\n\$3\r\nhey\r\n" | nc -N -w1 127.0.0.1 5000 & done

for i in {1..5}; do
    echo "Sending request $i"
    echo -en "*1\r\n\$4\r\nPING\r\n" | nc -N -w1 127.0.0.1 5000 & done
