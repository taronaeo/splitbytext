#! /usr/bin/env bash

if [[ "$OSTYPE" =~ ^msys ]]; then
  py -3 setup.py build
else
  python3 setup.py build
fi
