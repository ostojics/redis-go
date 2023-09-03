#!/bin/bash

{
    echo -en "*1\r\n\$4\r\nPING\r\n"
    echo -en "*2\r\n\$4\r\nECHO\r\n\$3\r\nhey\r\n"
    echo -en "*2\r\n\$4\r\nECHO\r\n\$3\r\nhey\r\n"
} | nc -N -w1 127.0.0.1 5000