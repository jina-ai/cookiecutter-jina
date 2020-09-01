__version__ = '{{ cookiecutter.version }}'

import os
import sys

from jina.flow import Flow

num_docs = os.environ.get('MAX_DOCS', 500)

def config():
    parallel = {{cookiecutter.parallel}} if sys.argv[1] == 'index' else 1
    shards = {{cookiecutter.shards}}

    os.environ['PARALLEL'] = str(parallel)
    os.environ['SHARDS'] = str(shards)
    os.environ['WORKDIR'] = './workspace'
    os.makedirs(os.environ['WORKDIR'], exist_ok=True)
    os.environ['JINA_PORT'] = os.environ.get('JINA_PORT', str({{cookiecutter.public_port}}))


# for index
def index():
    f = Flow.load_config('flows/index.yml')

    with f:
        {%- if cookiecutter.index_type | lower == 'files' %}
        f.index_files('data/**/*.png', batch_size=8, read_mode='rb', size=num_docs)
        {%- endif %}
        {%- if cookiecutter.index_type | lower == 'strings' %}
        data_path = os.environ.get('DATA_PATH', None)
        if data_path:
            f.index_lines(filepath=data_path, batch_size=16, read_mode='r', size=num_docs)
        else:
            f.index_lines(lines=['abc', 'cde', 'efg'], batch_size=16, read_mode='r', size=num_docs)
        {%- endif %}
        {%- if cookiecutter.index_type | lower == 'ndarray' %}
        import numpy as np
        f.index_numpy(np.random.random([100, 512]), batch_size=64, size=num_docs)
        {%- endif %}
        {%- if cookiecutter.index_type | lower == 'customized' %}

        def input_fn():
            with open('README.md') as fp:
                for v in fp:
                    yield v

        f.index(input_fn, batch_size=8, read_mode='rb', size=num_docs)
        {%- endif %}

    # for search
def search():
    f = Flow.load_config('flows/query.yml')

    with f:
        f.block()


# for test before put into docker
def dryrun():
    f = Flow.load_config('flows/query.yml')

    with f:
        pass


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('choose between "index/search/dryrun" mode')
        exit(1)
    if sys.argv[1] == 'index':
        config()
        index()
    elif sys.argv[1] == 'search':
        config()
        search()
    elif sys.argv[1] == 'dryrun':
        config()
        dryrun()
    else:
        raise NotImplementedError(f'unsupported mode {sys.argv[1]}')
