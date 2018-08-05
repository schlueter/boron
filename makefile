.phony: deploy test tree

test:
	tox

deploy:
	python setup.py sdist bdist_wheel
	twine upload dist/*

tree:
	tree -I '*.egg-info|__pycache__|*.log|build|dist'
