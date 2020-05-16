#Makefile
CC = gcc
INCLUDE = /usr/lib
LIBS = -lcrypto -lssl
OBJS = 
CFLAGS = -g 
all: clean ipfs_server ipfs_client start run

ipfs_server:
	$(CC) -o bin/ipfs_server -Iheaders headers/*.c ipfs_server.c $(CFLAGS) $(LIBS)

ipfs_client:
	$(CC) -o bin/ipfs_client -Iheaders headers/*.c ipfs_client.c $(CFLAGS) $(LIBS)

kill:
	fuser -k 11001/tcp &
	fuser -k 11002/tcp &
	fuser -k 11003/tcp &
	fuser -k 11004/tcp &

clear:
	rm -rf SERVER*/*

clean:
	rm -rf bin
	mkdir -p bin

start:
	bin/ipfs_server /SERVER1 11001 &> logs/SERVER1.log &
	bin/ipfs_server /SERVER2 11002 &> logs/SERVER2.log &
	bin/ipfs_server /SERVER3 11003 &> logs/SERVER3.log &
	bin/ipfs_server /SERVER4 11004 &> logs/SERVER4.log &
	
run:
	tail -f logs/SERVER*

ipfsc:
	rm bin/ipfs_client
	$(CC) -o bin/ipfs_client -Iheaders headers/*.c ipfs_client.c $(CFLAGS) $(LIBS)
	gdb -tui bin/ipfs_client --args bin/ipfs_client conf/ipfs_client.conf 2> logs/client.log

ipfss:
	rm bin/ipfs_server
	$(CC) -o bin/ipfs_server -Iheaders headers/*.c ipfs_server.c $(CFLAGS) $(LIBS)
	gdb -tui bin/ipfs_server --args bin/ipfs_server /SERVER1 11001

client:
	rm bin/ipfs_client
	$(CC) -o bin/ipfs_client -Iheaders headers/*.c ipfs_client.c $(CFLAGS) $(LIBS)
	bin/ipfs_client conf/ipfs_client.conf 2> logs/ipfs_client.log

