#!/bin/sh

set -e
tmpFile=$(mktemp)
go build -o "$tmpFile" cmd/app/*.go
exec "$tmpFile"
