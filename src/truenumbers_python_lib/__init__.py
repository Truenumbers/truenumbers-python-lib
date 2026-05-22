"""
Truenumbers Python library: clients for REST, Trigger, and Artifact APIs.

Examples::

    from truenumbers_python_lib import TruenumbersRestApi, TruenumbersTriggerApi
    from truenumbers_python_lib import TruenumbersArtifactApi

Submodules remain importable::

    from truenumbers_python_lib.TruenumbersRestApi import TruenumbersRestApi
"""

import re
from pathlib import Path

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


def _version_from_matching_pyproject():
    """
    When developing from a git checkout, prefer [project].version from a nearby
    pyproject.toml so tools like pydoc match the edited file — not stale install
    metadata from the last pip install.
    """
    name_pat = re.compile(r'name\s*=\s*["\']truenumbers-python-lib["\']')
    ver_pat = re.compile(r"(?m)^version\s*=\s*[\"']([^\"']+)[\"']\s*$")
    here = Path(__file__).resolve()
    for d in here.parents:
        candidate = d / "pyproject.toml"
        if not candidate.is_file():
            continue
        try:
            text = candidate.read_text(encoding="utf-8")
        except OSError:
            continue
        if name_pat.search(text) is None:
            continue
        m = ver_pat.search(text)
        if m:
            return m.group(1)
    return None


__version__ = _version_from_matching_pyproject() or _read_dist_version()

from .TruenumbersArtifactApi import TruenumbersArtifactApi
from .TruenumbersRestApi import TruenumbersRestApi
from .TruenumbersTriggerApi import TruenumbersTriggerApi

__all__ = [
    "__version__",
    "TruenumbersArtifactApi",
    "TruenumbersRestApi",
    "TruenumbersTriggerApi",
]
