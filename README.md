# GCPctl

Work In Progress

## Installation

```
pip install -r requirements
pip install .
```

## Configuration

gcpctl can be used with or without a configuration file.
A configuration file can be used to set up environments - you can think of them as aliases for folders, projects, etc.

```
environments:
  test:
    - folder: 19282017912
  prod:
    - project: some-project
    - folder: 82819202212
  dev:
    - folder: 192911991212
```

## Usage

### Folders

* List folders under a given a folder: `gcpctl get folders -i <FOLDER_ID>`
