# {{ cookiecutter.project_name }}

[![Jina](https://github.com/jina-ai/jina/blob/master/.github/badges/jina-badge.svg?raw=true  "We fully commit to open-source")](https://get.jina.ai)

{{ cookiecutter.project_short_description }}

## Features

## Install

```bash
pip install .
```

To install it in editable mode

```bash
pip install -e .
```

## Run

| Command                  | Description                  |
| :---                     | :---                         |
| ``python app.py index``  | To index files/data          |
| ``python app.py search`` | To run query on the index    |
| ``python app.py dryrun`` | Sanity check on the topology |

## Run as a Docker Container

To build the docker image
```bash
docker build -t jinaai/hub.app.{{ cookiecutter.project_slug }}:{{cookiecutter.version}} .
```

To mount local directory and run:
```bash
docker run -v "$(pwd)/j:/workspace" jinaai/hub.app.{{ cookiecutter.project_slug }}:{{cookiecutter.version}}
``` 

To query
```bash
docker run -p {{cookiecutter.public_port}}:{{cookiecutter.public_port}} -e "JINA_PORT=65481" jinaai/hub.app.{{ cookiecutter.project_slug }}:{{cookiecutter.version}} search
```

## License

Copyright (c) 2020 {{ cookiecutter.author_name }}. All rights reserved.


