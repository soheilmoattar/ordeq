







from ordeq_viz.graph import IOData, NodeData, _gather_graph














































































def _generate_nodes(nodes: list[NodeData], datasets: list[IOData]):


















def _generate_main(nodes: list[NodeData], datasets: list[IOData]):































































        datasets: dict of name and `ordeq.framework.IO`







    ```python
    >>> from pathlib import Path
    >>> from ordeq_viz import (
    ...     gather_ios_from_module,
    ...     gather_nodes_from_registry,
    ...     pipeline_to_kedro_viz
    ... )

    >>> import catalog as catalog_module  # doctest: +SKIP
    >>> import nodes as nodes_module  # doctest: +SKIP

    >>> # Gather all nodes in your project:
    >>> nodes = gather_nodes_from_registry()
    >>> # Find all objects of type "IO" in catalog.py
    >>> datasets = gather_ios_from_module(catalog_module)  # doctest: +SKIP

    >>> pipeline_to_kedro_viz(
    ...    nodes,
    ...    datasets,
    ...    output_directory=Path("kedro-pipeline-example/")
    ... )  # doctest: +SKIP

    ```

    Run with:

    ```shell
    export KEDRO_DISABLE_TELEMETRY=true
    kedro viz run --load-file kedro-pipeline-example
    ```





























