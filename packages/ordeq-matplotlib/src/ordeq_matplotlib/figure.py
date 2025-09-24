



from ordeq.framework.io import Output




class MatplotlibFigure(Output[plt.Figure]):
    """IO to save matplotlib Figures.

    Example usage:

    ```python
    >>> from pathlib import Path
    >>> from ordeq_matplotlib import MatplotlibFigure
    >>> MyFigure = MatplotlibFigure(
    ...     path=Path("path/figure.pdf")
    ... )

    ```








