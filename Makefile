#########
# BUILD #
#########
develop:  ## install dependencies and build library
	python3 -m pip install -e .[develop]

build:  ## build the python3 library
	python3 setup.py build build_ext --inplace

install:  ## install library
	python3 -m pip install .

#########
# LINTS #
#########
lint:  ## run static analysis with flake8
	python3 -m black --check sec_web_scraper setup.py
	python3 -m flake8 sec_web_scraper setup.py

# Alias
lints: lint

format:  ## run autoformatting with black
	python3 -m black -v sec_web_scraper/ setup.py

# alias
fix: format

check:  ## check assets for packaging
	check-manifest -v

# Alias
checks: check

annotate:  ## run type checking
	python3 -m mypy ./sec_web_scraper

#########
# TESTS #
#########
test: ## clean and run unit tests
	python3 -m pytest -v sec_web_scraper/tests

coverage:  ## clean and run unit tests with coverage
	python3 -m pytest -v sec_web_scraper/tests --cov=sec_web_scraper --cov-branch --cov-fail-under=75 --cov-report term-missing

# Alias
cov: coverage

tests: test

###########
# VERSION #
###########
show-version:
	bump2version --dry-run --allow-dirty setup.py --list | grep current | awk -F= '{print $2}'

patch:
	bump2version patch

minor:
	bump2version minor

major:
	bump2version major

########
# DIST #
########
dist-build:  # Build python3 dist
	python3 setup.py sdist bdist_wheel

dist-check:
	python3 -m twine check dist/*

dist: clean build dist-build dist-check  ## Build dists

publish:  # Upload python3 assets
	echo "would usually run python3 -m twine upload dist/* --skip-existing"

#########
# DOCS #
#########
install-docs:
	python3 -m pip install -e .[docs]


deploy-docs:
	mkdocs gh-deploy --force


#########
# CLEAN #
#########
deep-clean: ## clean everything from the repository
	git clean -fdx

clean: ## clean the repository
	rm -rf .coverage coverage cover htmlcov logs build dist *.egg-info .pytest_cache

############################################################################################

# Thanks to Francoise at marmelab.com for this
.DEFAULT_GOAL := help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

print-%:
	@echo '$*=$($*)'

.PHONY: develop build install lint lints format fix check checks annotate test coverage show-coverage tests show-version patch minor major dist-build dist-check dist publish deep-clean clean help
