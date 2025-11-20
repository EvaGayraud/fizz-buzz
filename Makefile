.PHONY : install_pre_commit

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT


## ARGUMENTS
NAMESPACE := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))


## BIN
RUN = poetry run
DOCKER_COMPOSE = docker compose
HELM := helm
KUBECTL := microk8s.kubectl


## Variable
PACKAGE_PATH = ./vif_ai_commands_api
TEST_PATH = ./tests
CHART_NAME := vif-ai-order-analysis-api
CHAR_DIR := helm/chart
SERVICE_NAME := vif-ai-commands-api


help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

install-poetry-bump-version:
	poetry self add poetry-bumpversion==0.3.1

install-poetry-package:
	pip install poetry==1.6.1

install-pre-commit:
	${RUN} pre-commit install

install-minimal-poetry: install-poetry-package

install-poetry: install-poetry-package install-poetry-bump-version

install-dev: install-poetry install-env-dev install-pre-commit

install-env-dev:
	poetry install --only main,dev,test

install-test: install-poetry
	poetry install --only main,test

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

prepare-code: check-typing run-format run-linter run-unit-tests

check-typing:
	${RUN} mypy ${PACKAGE_PATH}

run-format:
	${RUN} black ${PACKAGE_PATH}

run-linter:
	${RUN} ruff ${PACKAGE_PATH} --fix

run-unit-tests: ## run tests quickly with the default Python
	${RUN} python -m pytest ${TEST_PATH}/unit_tests --cov=${PACKAGE_PATH} --cov-report term --cov-report xml:coverage.xml

run-functional-tests: ## run functional tests quickly with the default Python
	${RUN} python -m pytest ${TEST_PATH}/functional_tests

build-image:
	${DOCKER_COMPOSE} build

push-image:
	${DOCKER_COMPOSE} push

build-push-image:  build-image push-image

start-container:
	${DOCKER_COMPOSE} up -d

down-container:
	${DOCKER_COMPOSE} down

show-container-logs:
	${DOCKER_COMPOSE} logs

exec-container:
	${DOCKER_COMPOSE} exec -it ${SERVICE_NAME} bash

show-container:
	${DOCKER_COMPOSE} ps

install:
	${HELM} install --wait ${CHART_NAME} ${CHAR_DIR} -n ${NAMESPACE} -f helm/override_values_${NAMESPACE}.yaml

delete:
	${HELM} delete ${CHART_NAME} -n ${NAMESPACE}

upgrade:
	${HELM} upgrade --install --wait ${CHART_NAME} ${CHAR_DIR} -n ${NAMESPACE} -f helm/override_values_${NAMESPACE}.yaml

redeploy: delete install

start-server:
	${RUN} python3 start_server.py

show-package-version:
	poetry version --short

%: # When don't find rule -> use with arg
   # We have to do this to avoid makefile error because of arguments
	@: # do nothing
