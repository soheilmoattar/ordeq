











) -> str:




        datasets: dict of name and `ordeq.framework.IO`










    ```python
    >>> from pathlib import Path
    >>> from ordeq_viz import (
    ...    gather_ios_from_module,
    ...    gather_nodes_from_registry,
    ...    pipeline_to_mermaid
    ... )

    >>> import catalog as catalog_module  # doctest: +SKIP
    >>> import pipeline as pipeline_module  # doctest: +SKIP

    ```

    Gather all nodes in your project:
    ```python
    >>> nodes = gather_nodes_from_registry()

    ```

    Find all objects of type "IO" in catalog.py:
    ```python
    >>> datasets = gather_ios_from_module(catalog_module)  # doctest: +SKIP
    >>> mermaid = pipeline_to_mermaid(nodes, datasets)  # doctest: +SKIP
    >>> Path("pipeline.mermaid").write_text(mermaid)  # doctest: +SKIP

    ```








            for attribute, values in dataset_.references.items():















































        data += "\t\t\tL1[(IO)]:::dataset\n"


            data += "\t\tsubgraph IO Types\n"






































