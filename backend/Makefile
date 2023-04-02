
test: test/unitary test/integration
	pytest

test/unitary:
	pytest

test/integration:
	./manage.py test --pattern="integration_*.py" --keepdb
