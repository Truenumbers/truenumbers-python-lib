#!/bin/bash

pydoc-markdown -I ./src/TruenumbersRestApi > docs/TruenumbersRestApi.md
pydoc-markdown -I ./src/TruenumbersTriggerApi > docs/TruenumbersTriggerApi.md
pydoc-markdown -I ./src/TruenumbersArtifactApi > docs/TruenumbersArtifactApi.md
