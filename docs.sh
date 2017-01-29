#!/bin/bash

setup() {
    mkdir -p docs/build/html && \
    mkdir -p docs/work && \
    mkdir -p docs/work/_static && \
        cp -r ./docs/source/ ./docs/work/
}

apidocs() {
    sphinx-apidoc --separate -o ./docs/work volume `find volume -name __int__.py`
}

build-html() ( # () means pwd is restored at exit
    cd docs/work && \
        sphinx-build -b html . ../build/html
)

setup && \
    apidocs && \
    build-html
