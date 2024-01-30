# coding: utf-8

"""
Custom type definitions and shorthands to simplify imports of types that are spread across multiple
packages.
"""

from __future__ import annotations

__all__: list[str] = []

import sys
from io import TextIOWrapper  # noqa
from collections.abc import KeysView, ValuesView, MappingView  # noqa
from types import ModuleType, GeneratorType, TracebackType  # noqa
from typing import (  # noqa
    Any, Union, Type, TypeVar, ClassVar, Sequence, Callable, Generator, TextIO, Iterable, Iterator,
    Hashable, MutableMapping, IO, Generic,
)
from contextlib import AbstractContextManager  # noqa

from typing_extensions import Annotated, _AnnotatedAlias as AnnotatedType  # noqa

# version dependent imports
if sys.version_info[:2] == (3, 7):
    from typing_extensions import Literal  # noqa
else:
    from typing import Literal  # noqa

if sys.version_info[:2] >= (3, 9):
    from types import GenericAlias  # noqa
else:
    GenericAlias = str


#: Generic type variables, more stringent than Any.
T = TypeVar("T")
T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")
K = TypeVar("K", bound=Hashable)
