.PHONY: test_local test_travis

test_travis:
	nosetests \
		--nocapture \
		--with-coverage \
		--cover-package=geometry

test_local:
	make test_travis
	rm .coverage

