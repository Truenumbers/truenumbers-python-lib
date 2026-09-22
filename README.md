# Truenumbers Python Libraries

Distribution name (pip): **`truenumbers-python-lib`**

Import package: **`truenumbers_python_lib`** (hyphens cannot appear in Python
import paths; this is the conventional mapping).

Installation::

    pip install truenumbers-python-lib @ git+https://github.com/Truenumbers/truenumbers-python-lib

Usage::

    from truenumbers_python_lib import (
        TruenumbersRestApi,
        TruenumbersTriggerApi,
        TruenumbersArtifactApi,
    )

    tn = TruenumbersRestApi(
        base_url="https://your-host/truenumbers-rest-api",
        shared_headers={"Authorization": "Bearer ..."},
    )

# Updating and publishing next version

- Set next version in pyproject.toml
- run `./make_docs.sh`
- git commit changes
- git tag -a <next version> -m ">version changeset message>"
- git push origin --tags
