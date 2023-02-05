#!/bin/bash

set -u

flake8 .
pylint gcpctl
