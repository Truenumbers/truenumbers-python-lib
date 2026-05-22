"""
Truenumbers Python library: clients for REST, Trigger, and Artifact APIs.

Examples::

    from truenumbers_python_lib import TruenumbersRestApi, TruenumbersTriggerApi
    from truenumbers_python_lib import TruenumbersArtifactApi

Submodules remain importable::

    from truenumbers_python_lib.TruenumbersRestApi import TruenumbersRestApi
"""

try:
    from importlib.metadata import version as _pkg_version_fn
except ImportError:
    _pkg_version_fn = None


def _read_dist_version():
    if _pkg_version_fn is None:
        return None
    try:
        return _pkg_version_fn("truenumbers-python-lib")
    except Exception:
        return None


__version__ = _read_dist_version()

from .TruenumbersArtifactApi import TruenumbersArtifactApi
from .TruenumbersRestApi import TruenumbersRestApi
from .TruenumbersTriggerApi import TruenumbersTriggerApi

__all__ = [
    "__version__",
    "TruenumbersArtifactApi",
    "TruenumbersRestApi",
    "TruenumbersTriggerApi",
]
