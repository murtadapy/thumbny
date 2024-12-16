from typing import Union
from typing import get_type_hints
from typing import get_origin
from typing import get_args


def _is_optional(field_type) -> bool:
    origin = get_origin(field_type)
    if origin is Union:
        return type(None) in get_args(field_type)
    return True


def check_required_fields(instance):
    annotations = get_type_hints(instance.__class__)

    for field_name, field_type in annotations.items():
        if (not _is_optional(field_type)
                and getattr(instance, field_name) is None):
            raise ValueError(f"Field '{field_name}' cannot be None.")
