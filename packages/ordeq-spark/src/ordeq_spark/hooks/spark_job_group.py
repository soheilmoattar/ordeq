from ordeq import Node
from ordeq.framework.hook import NodeHook




def _set_job_group(name: str) -> None:







    Example usage:

    ```python
    >>> from ordeq.framework import node
    >>> from ordeq_spark import SparkHiveTable
    >>> from pyspark.sql import DataFrame
    >>> from ordeq.framework.runner import run

    >>> @node(
    ...     inputs=SparkHiveTable(table="tables.a"),
    ...     outputs=SparkHiveTable(table="tables.b"),
    ... )
    ... def append(a: DataFrame) -> DataFrame:
    ...     return a.union(a)

    >>> run(append, hooks=[SparkJobGroupHook()]) # doctest: +SKIP

    ```

    """

    def before_node_run(self, node: Node) -> None:
        """Sets the node name as the job group in the Spark context.
        This makes the history server a lot easier to use.








        _set_job_group(node.name)
