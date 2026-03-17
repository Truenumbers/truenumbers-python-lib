#!/bin/bash

python -m pydoc -w src
python -m pydoc -w src.TruenumbersRestApi
python -m pydoc -w src.TruenumbersTriggerApi
python -m pydoc -w src.TruenumbersArtifactApi
mv *.html docs
mv docs/src.html docs/index.html
python prepare_html_docs.py