


































































def _nodes(edges: EdgesType) -> set[Node]:
    """Returns the set of all nodes.

    Args:
        edges: the graph

    Returns:
        set of all nodes
    """

    return set(edges.keys())


























    @property
    def sink_nodes(self) -> set[Node]:







    @property
    def nodes(self) -> set[Node]:
        """Returns the set of all nodes in this graph.

        Returns:
            all nodes in this graph
        """

        return _nodes(self.edges)









