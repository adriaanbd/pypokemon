build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

test: up
	docker-compose run --rm --no-deps --entrypoint=pytest api /tests/

dbsh:
	docker-compose exec db psql -U postgres

api:
	docker-compose exec api bash
