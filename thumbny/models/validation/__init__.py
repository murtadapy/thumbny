from typing import get_type_hints
from typing import get_origin
from typing import get_args
from typing import Union
from typing import Any

import re
from dataclasses import dataclass


HEX_REGEX = r'^#[0-9a-fA-F]{6}$'


def _is_optional(field_type: Any) -> bool:
    """Helper to check the field if optional
    based on the annotations

    Args:
        field_type (field type): field type

    Returns:
        bool: True if optional, otherwise False
    """
    origin = get_origin(field_type)
    if origin is Union:
        return type(None) in get_args(field_type)
    return False


def check_required_fields(instance: dataclass) -> None:
    """Check required fields of the given instance

    Args:
        instance (dataclass): dataclass model

    Raises:
        ValueError: value error if required field was not given
    """
    annotations = get_type_hints(instance.__class__)
    for field_name, field_type in annotations.items():
        if (not _is_optional(field_type)
                and getattr(instance, field_name) is None):
            raise ValueError(f"Field '{field_name}' cannot be None.")


def check_spaces(field_name: str, field_value: Any) -> None:
    """Check spaces if exist

    Args:
        field_name (str): field name
        field_value (Any): field value

    Raises:
        ValueError: value error if spaces are exist
    """
    if field_value.count(" "):
        raise ValueError(f"{field_name} cannot contain spaces")


def check_hex_color(field_name: str, field_value: Any) -> None:
    """Check hex color value

    Args:
        field_name (str): field name
        field_value (Any): field value

    Raises:
        ValueError: value error if hex was not correct
    """
    if not re.match(HEX_REGEX, str(field_value)):
        raise ValueError(f"{field_name} isn't correct. "
                         "Should follow this format: #FFFFFF "
                         f"Given ({field_value})")
