build:
	@docker build -t nezuko-kamado .

run: build
	@docker run -e WELCOME_ROLE=$(WELCOME_ROLE) -e BOT_TOKEN=$(BOT_TOKEN) -d nezuko-kamado