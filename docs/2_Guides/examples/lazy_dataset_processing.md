










```pycon
>>> from collections.abc import Iterable
>>> from pathlib import Path
>>>
>>> from ordeq import node
>>> from ordeq_common import Iterate
>>> from ordeq_files import JSON, Text
>>> paths = [Path("hello.txt"), Path("world.txt")]
>>> text_dataset = Iterate(tuple(Text(path=path) for path in paths))
>>> json_dataset = Iterate(
...     tuple(JSON(path=path.with_suffix(".json")) for path in paths)
... )
>>> @node(inputs=text_dataset, outputs=json_dataset)
... def generate_json_contents(
...     contents: Iterable[str],
... ) -> Iterable[dict[str, str]]:
...     """Wrap the text-contents in a JSON structure."""
...     for content in contents:
...         yield {"content": content}



