#!/bin/bash
set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
export PYTHONPATH="${ROOT}/src${PYTHONPATH:+:$PYTHONPATH}"

python -m pydoc -w truenumbers_python_lib
python -m pydoc -w truenumbers_python_lib.TruenumbersRestApi
python -m pydoc -w truenumbers_python_lib.TruenumbersTriggerApi
python -m pydoc -w truenumbers_python_lib.TruenumbersArtifactApi
mv *.html docs
mv docs/truenumbers_python_lib.html docs/index.html
python prepare_html_docs.py
