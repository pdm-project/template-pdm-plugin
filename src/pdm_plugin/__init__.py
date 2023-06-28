"""
    pdm_plugin

    :Please add description here:
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pdm.core import Core


def plugin(core: Core) -> None:
    """Register pdm plugin to pdm-core."""
    pass
