.PHONY: test test_travis

test_travis:
	nosetests \
		--nocapture \
		--with-coverage \
		--cover-package=geometry

test:
	make test_travis
	rm .coverage

