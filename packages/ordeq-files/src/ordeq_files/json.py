import json
from dataclasses import dataclass

from ordeq import IO



@dataclass(frozen=True, kw_only=True)
class JSON(IO[dict]):
    """IO representing a JSON.

    Example usage:

    ```python
    >>> from ordeq_files import YAML
    >>> from pathlib import Path
    >>> MyJSON = JSON(
    ...     path=Path("path/to.json")
    ... )

    ```

    """

    path: PathLike


        with self.path.open(mode="r") as fh:
            return json.load(fh)


        with self.path.open(mode="w") as fh:
            json.dump(data, fh)
