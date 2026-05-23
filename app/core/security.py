from secrets import compare_digest


def constant_time_equals(left: str, right: str) -> bool:
    return compare_digest(left, right)
