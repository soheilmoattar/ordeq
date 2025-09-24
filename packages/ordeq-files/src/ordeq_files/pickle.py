import pickle






@dataclass(frozen=True, kw_only=True)
class Pickle(IO[T]):




    ```python
    >>> from ordeq_files import Pickle
    >>> from pathlib import Path
    >>> MyPickle = Pickle(
    ...     path=Path("path/to.pkl")
    ... )

    ```


    path: PathLike


        with self.path.open("rb") as fh:
            return pickle.load(fh)


        with self.path.open("wb") as fh:

