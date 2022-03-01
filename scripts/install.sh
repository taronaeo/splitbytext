#! /usr/bin/env bash

if [[ "$OSTYPE" =~ ^msys ]]; then
  py -3 -m pip install --upgrade pip
  py -3 -m pip install -r requirements.txt
else
  python3 -m pip install --upgrade pip
  python3 -m pip install -r requirements.txt
fi