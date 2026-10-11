CC := g++
CCFLAGS := -Wall -ggdb

.PHONY: all server client clean

all: build/mdps build/mdpc

build/mdps: src/server.cpp
	@mkdir -p build
	$(CC) $(CCFLAGS) src/server.cpp -o build/mdps 

build/mdpc: src/client.cpp
	@mkdir -p build
	$(CC) $(CCFLAGS) src/client.cpp -o build/mdpc $(LDFLAGS)

server: build/mdps
	./build/mdps

client: build/mdpc
	./build/mdpc

clean:
	rm ./build/mdps ./build/mdpc

