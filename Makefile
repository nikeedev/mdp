CC := g++
CCFLAGS := -Wall -ggdb

.PHONY: all run_s run_c

all: run_s

build/mdps: src/server.cpp
	@mkdir -p build
	$(CC) $(CCFLAGS) src/server.cpp -o build/mdps 

build/mdpc: src/client.cpp
	@mkdir -p build
	$(CC) $(CCFLAGS) src/client.cpp -o build/mdpc $(LDFLAGS)

run_s: build/mdps
	./build/mdps

run_c: build/mdpc
	./build/mdpc

