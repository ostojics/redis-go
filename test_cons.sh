#!/bin/bash

for i in {1..10}; do
    echo "Sending request $i"
    echo "PING" | nc 127.0.0.1 5000 & done
