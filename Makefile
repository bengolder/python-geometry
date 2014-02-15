.PHONY: test_local test_travis test_btree

test_travis:
	nosetests \
		--nocapture \
		--with-coverage \
		--cover-package=geometry

test_local:
	make test_travis
	rm .coverage

test_btree:
	nosetests --nocapture tests/test_btree.py:TestBTreeNode.test_constructor


