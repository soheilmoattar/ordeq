


from ordeq.framework.io import Input




class Glob(Input[Generator[PathLike, None, None]]):
    """IO class that loads all paths provided a pattern.




    ```python
    >>> class LoadPartitions(Glob):
    ...     def load(self):
    ...         paths = super().load()
    ...         for path in paths:
    ...             yield my_load_func(path)

    ```







