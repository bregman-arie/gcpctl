# GCPctl

Google Cloud Platform (GCP) utils

## Installation

```
pip install -r requirements
pip install .
```

## Configuration

A configuration file is optional and can enhance part of your user experience with GCP.
Right now the only thing it support is "environments" - think of those as aliases for certain folders.

```
environments:
  test:
    - 19282017912   # Actual GCP folder
  prod:
    - 192820171241
    - 82819202212
  dev:
    - 192911991212
```

## Usage

### Folders

* List folders: `gcpctl get folders`
* List folders under a given a folder: `gcpctl get folders -i <FOLDER_ID>`

### Projects

* List projects: `gcpctl get projects`
* List projects from prod environment: `gcpctl get projects -e prod` (see configuration section for more info)
* List projects from prod and dev environments: `gcpctl get projects -e prod dev`
* List projects from a specific folder: `gpctl get projects -f 19282017912`
* List projects from prod environment and a specific folder: `gcpctl get projects -e prod -f 19282017912`

### GKE Clusters

* List clusters from a specific env: `gcpctl get gke-clusters -e prod` (see configuration section for more info)
