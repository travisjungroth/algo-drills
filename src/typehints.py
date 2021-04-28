from collections.abc import Hashable
from dataclasses import dataclass
from typing import Optional, TypeVar

Node = TypeVar('Node', bound=Hashable)
T = TypeVar('T')


@dataclass
class BTNode:
    val: int
    left: Optional['BTNode']
    right: Optional['BTNode']
