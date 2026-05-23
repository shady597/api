from collections.abc import Iterator
from contextlib import contextmanager


@contextmanager
def get_db_session() -> Iterator[None]:
    yield None
