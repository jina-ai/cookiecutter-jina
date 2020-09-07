# cookiecutter-jina

[![Jina](https://github.com/jina-ai/jina/blob/master/.github/badges/jina-badge.svg?raw=true  "We fully commit to open-source")](https://get.jina.ai)

Cookiecutter template for a Jina project

## Quick start


### Use with Jina (>=0.5.4)

```bash
pip install jina[devel]
jina hub new --type app
```

### Use without Jina

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

```bash
pip install -U cookiecutter
```

Generate a Jina project:

```bash
cookiecutter gh:jina-ai/cookiecutter-jina
```

Install Jina Requirements

```bash
cd myprojects/
pip install .
```


## Exporting Environment Variables

Before running ```python app.py```, set environment variables like ```MAX_DOCS``` and ```DATA_PATH``` using export:

For instance: ```export DATA_PATH='./data/startrek_tng.csv'```

## Fork This / Create Your Own

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.
