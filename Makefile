PYTHON := python

.PHONY: server client 

server: src/server.py
	$(PYTHON) src/server.py

client: src/client.py
	$(PYTHON) src/client.py


