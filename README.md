# Interview Task

## Description
This is an implementation of a python based web socket server and client. Here, the client application connects to 
the server via a TCP socket and sends an arbitrary number of protobuf-encoded, length-prefixed messages.
I have put a copy of the log_message.proto file in both client and server as I am considering them as separate applications.


## Requirements

1. [Docker](https://www.docker.com/)
2. [Docker Compose](https://docs.docker.com/compose/install/)
3. make (might be pre-installed if you are using a linux distribution or macOS)

## How it works

The server and the client are containerized with docker and docker-compose. Therefore, there is no need to install pesky libraries and tools as long as the above 
mentioned requirements are met.

I have also created a makefile so that there is no need to deal with the commands for docker and docker-compose. Following are the different commands that will be used to run the 
application.


### Run the server
This commands starts the server in a terminal.

```shell
make server
```

After this command is executed, you can now run the client in a separate terminal. Try running the 
client multiple times to see if messages are passed to server and logged there.

Disclaimer: Don't close the terminal in which you ran this command.

### Run the client
This command runs the client and sends messages to server

```shell
make client
```

### Stop all running containers and clean up
Stop both the running containers and do cleanup

```shell
make clean
```