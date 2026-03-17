#!/bin/bash

python -m pydoc -w src.TruenumbersRestApi
python -m pydoc -w src.TruenumbersTriggerApi
python -m pydoc -w src.TruenumbersArtifactApi
mv *.html docs
python convert_pydoc_to_md.py