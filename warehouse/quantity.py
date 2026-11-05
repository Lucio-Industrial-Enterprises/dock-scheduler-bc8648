"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Parse a quantity string and return a non-negative integer.

    Raises:
        ValueError: If the value cannot be parsed as an integer or is negative.
    """
    qty = int(value.strip())
    if qty < 0:
        raise ValueError(f"Quantity must be non-negative, got {qty}")
    return qty
