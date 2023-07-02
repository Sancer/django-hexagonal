
test: test/unitary test/integration

test/unitary:
	docker compose -f docker-compose.test.yml run backend pytest ./tests/

test/integration:
	docker compose -f docker-compose.test.yml run backend
