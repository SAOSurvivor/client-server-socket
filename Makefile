# Docker Compose command
DOCKER_COMPOSE = docker-compose

.PHONY: all server client

all: server client

server:
	$(DOCKER_COMPOSE) up log-server

client:
	$(DOCKER_COMPOSE) up log-client

stop-server:
	$(DOCKER_COMPOSE) stop log-server

stop-client:
	$(DOCKER_COMPOSE) stop log-client

clean: stop-server stop-client
	$(DOCKER_COMPOSE) down