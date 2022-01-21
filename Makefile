install:
	poetry install
	
brain-even:
	poetry run brain-games
	
build:
	poetry build
	
publish:
	poetry publish --dry-run
	
package-install:
	python3 -m pip install --user dist/*.whl
	
lint:
	poetry run flake8 brain_games
	
package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl
