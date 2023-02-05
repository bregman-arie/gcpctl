#!/bin/bash

set -eu

flake8 .
pylint gcpctl
