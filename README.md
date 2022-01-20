DEPRECATED: DO NOT USE. 

ALTERNATIVES:
- you can fork one of the built-in hello world examples to your own app. See [here](https://docs.jina.ai/get-started/hello-world/#fork-one-and-start-building)

# cookiecutter-jina

[![Jina](https://github.com/jina-ai/jina/blob/master/.github/badges/jina-badge.svg?raw=true  "We fully commit to open-source")](https://get.jina.ai)

Cookiecutter template for a Jina project

## Quick start


### Use with Jina (>=0.5.5)

```bash
pip install jina[devel]
jina hub new --type app
```

It will start a wizard in CLI to guide you to create your first app. The resulting file structure should look like:

```text
- MyAwesomeApp/
    |
    |- Dockerfile
    |- README.md
    |- requirements.txt
    |- app.py
    |- flows/
        |- index.yml
        |- query.yml
    |- pods/
        |- craft.yml
        |- chunk.yml
        |- doc.yml
        |- encode.yml
```

### Use without Jina

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher):

```bash
pip install -U cookiecutter
```

Generate a Jina project:

```bash
cookiecutter gh:jina-ai/cookiecutter-jina
```

Install Jina requirements:

```bash
cd MyAwesomeApp/
pip install .
```


## Exporting Environment Variables

Before running ```python app.py```, set environment variables like ```MAX_DOCS``` and ```JINA_DATA_PATH``` using export. For example:

```bash
export JINA_DATA_PATH='./data/startrek_tng.csv'
```

## Fork This / Create Your Own

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.
  
## Best Practices

Jina apps created with the methods above:

- Store their Pods in the `pods` directory
- Store their Flows in the `flows` directory

We highly encourage you to use these methods for your own apps, and especially if you're planning to create examples for Jina.
