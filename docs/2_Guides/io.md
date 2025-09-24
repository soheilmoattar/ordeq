





















```pycon
>>> from dataclasses import dataclass
>>> from pathlib import Path
>>> import faiss
>>> from ordeq.framework.io import IO
>>> @dataclass(frozen=True, kw_only=True)
... class FaissIndex(IO[faiss.Index]):
...     path: Path
...
...     def load(self) -> faiss.Index:
...         return faiss.read_index(str(self.path))
...
...     def save(self, index: faiss.Index) -> None:
...         faiss.write_index(index, str(self.path))











```pycon
>>> from dataclasses import dataclass
>>> from pathlib import Path
>>> from ordeq.framework.io import IO
>>> @dataclass(frozen=True, kw_only=True)
... class CustomIO(IO):
...     path: Path
...
...     def load(self):
...         pass
...
...     def save(self, data):
...         pass





This method should contain the logic for loading your data.
For example:

```pycon







This method should contain the logic for saving your data.
For example:

```pycon











```pycon
>>> from dataclasses import dataclass
>>> from pathlib import Path
>>> from ordeq.framework.io import IO
>>> @dataclass(frozen=True, kw_only=True)
... class CustomIO(IO):
...     path: Path
...
...     def load(self):
...         return self.path.read_text()
...
...     def save(self, data, newline: str = "\n"):
...         self.path.write_text(data, newline=newline)





Below is an example of this for a Pandas CSV IO class:

```pycon
>>> from dataclasses import dataclass
>>> from pathlib import Path
>>> import pandas as pd
>>> from ordeq.framework.io import IO
>>> @dataclass(frozen=True, kw_only=True)
... class PandasCSV(IO[pd.DataFrame]):
...     path: Path
...
...     def load(self, **load_args) -> pd.DataFrame:
...        return pd.read_csv(self.path, **load_args)
...
...     def save(self, data: pd.DataFrame, **save_args):
...         data.write_csv(self.path, **save_args)





We can provide the `str` argument to `IO` to indicate that `CustomIO` class loads and saves strings.
This type should match the return type of the `load` method and the first parameter of the `save` method.

```pycon
>>> from dataclasses import dataclass
>>> from pathlib import Path
>>> from ordeq.framework.io import IO
>>> @dataclass(frozen=True, kw_only=True)
... class CustomIO(IO[str]):  # IO operates on type `str`
...     path: Path
...
...     def load(self) -> str:  # and thus returns a `str` on load
...         return self.path.read_text()
...
...     def save(self, data: str) -> None:  # and takes a `str` as first argument to `save`
...         self.path.write_text(data)


















```pycon
>>> import random
>>> from dataclasses import dataclass
>>> from typing import Any
>>> from ordeq.framework.io import Input
>>> @dataclass(frozen=True, kw_only=True)
... class SensorDataGenerator(Input[dict[str, Any]]):
...     """Example Input class to generate synthetic sensor data
...
...     Examples:
...     >>> generator = SensorDataGenerator(sensor_id="sensor_3")
...     >>> data = generator.load()
...     {'sensor_id': 'sensor_3', 'temperature': 22.001252691230633, 'humidity': 35.2674852725557}
...     """
...
...     sensor_id: str
...
...     def load(self) -> dict[str, Any]:
...         """Simulate reading data from a sensor"""
...         return {
...             "sensor_id": self.sensor_id,
...             "temperature": random.uniform(20.0, 30.0),
...             "humidity": random.uniform(30.0, 50.0)
...         }







