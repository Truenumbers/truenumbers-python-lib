#!/bin/bash

python -m pydoc -w src
# python -m pydoc -w src.TruenumbersRestApi
# python -m pydoc -w src.TruenumbersTriggerApi
# python -m pydoc -w src.TruenumbersArtifactApi
mv *.html docs
mv docs/src.html docs/index.html
# python convert_pydoc_to_md.py