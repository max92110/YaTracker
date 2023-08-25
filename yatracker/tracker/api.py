from __future__ import annotations

import logging

from .base import BaseTracker
from .categories import (
    Comments,
    Issues,
    Priorities,
)

logger = logging.getLogger(__name__)


class YaTracker(
    Issues,
    Comments,
    Priorities,
    BaseTracker,
):
    """Represents Yandex Tracker API client.

    API docs: https://cloud.yandex.com/en/docs/tracker/about-api

    Attention!
        All 'self' properties renamed to 'link' because it's incompatible with Python.
        All camelCase properties renamed to pythonic_case.
        Methods named by author, cause Yandex API has no clear method names.
        For help you to recognize method names full description is attached.

    """
