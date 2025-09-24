import importlib
from pathlib import Path











from ordeq_viz.to_kedro_viz import pipeline_to_kedro_viz
from ordeq_viz.to_mermaid import pipeline_to_mermaid



def viz(












) -> None:


    Args:

        fmt: Format of the output visualization, ("kedro" or "mermaid").
        output: output file or directory where the viz will be saved.



    """






















        )
    match fmt:
        case "kedro":
            pipeline_to_kedro_viz(nodes, ios, output_directory=output)
        case "mermaid":
            result = pipeline_to_mermaid(nodes, ios)
            output.write_text(result, encoding="utf8")
