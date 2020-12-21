#!/bin/bash
set -e

bandit -r sampleapp/ -l -x tests.py
isort --check-only sampleapp/**/*.py
black --check --diff --exclude=/migrations/ sampleapp/
prospector -I "sampleapp/settings/*"
