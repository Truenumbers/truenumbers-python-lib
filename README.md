Truenumbers Python Libraries
============================

Distribution name (pip): **`truenumbers-python-lib`**

Import package: **`truenumbers_python_lib`** (hyphens cannot appear in Python
import paths; this is the conventional mapping).

Installation::

    pip install truenumbers-python-lib

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
