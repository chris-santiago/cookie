#!/bin/bash

error_trap() {
  local parent_lineno="$(caller)"
  local message="$2"
  local code="${3:-1}"
  if [[ -n "$message" ]] ; then
    echo "Error on or near line ${parent_lineno}: ${message}; exiting with status ${code}"
  else
    echo "Error on or near line ${parent_lineno}; exiting with status ${code}"
  fi
  exit "${code}"
}
trap error_trap ERR

####################################################################################################

conda env create -f environment.yml &&
source activate {{cookiecutter.project_slug}} &&
# assumes that PDM is installed via Homebrew
# https://pdm.fming.dev/latest/#recommended-installation-method
# Uncomment this line to have PDM installed in virtual environment via pip
# pip install pdm &&
pdm install &&
git init &&
pre-commit install
