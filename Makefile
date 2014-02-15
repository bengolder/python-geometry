.PHONY: test test_travis clean

test_travis:
	nosetests \
		--nocapture \
		--with-coverage \
		--cover-package=geometry

clean:
	rm .coverage
	rm geometry/*.pyc
	rm tests/*.pyc

test:
	make test_travis
	make clean


