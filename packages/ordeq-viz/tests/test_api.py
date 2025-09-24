from pathlib import Path
from unittest.mock import MagicMock, patch



from ordeq_viz.api import viz


def test_viz_main_mermaid(tmp_path: Path) -> None:
    output_file = tmp_path / "output.mermaid"

    assert output_file.exists()
    output_file_content = output_file.read_text("utf8")
    assert "graph TB" in output_file_content


































def test_viz_main_kedro(tmp_path: Path) -> None:
    output_folder = tmp_path / "kedro_output"

    assert output_folder.exists()
    assert (output_folder / "api" / "main").exists()


@patch("ordeq_viz.api.pipeline_to_mermaid", return_value="mermaid content")
def test_viz_to_mermaid_call(
    patched_pipeline_to_mermaid: MagicMock,
    tmp_path: Path,
    expected_example_node_objects,
    expected_example_ios,
) -> None:
    output_file = tmp_path / "output.mermaid"

    patched_pipeline_to_mermaid.assert_called_once_with(
        expected_example_node_objects, expected_example_ios
    )


@patch("ordeq_viz.api.pipeline_to_kedro_viz")
def test_viz_to_kedro_call(
    patched_pipeline_to_kedro: MagicMock,
    tmp_path: Path,
    expected_example_node_objects,
    expected_example_ios,
) -> None:
    output_folder = tmp_path / "kedro_output"

    patched_pipeline_to_kedro.assert_called_once_with(
        expected_example_node_objects,
        expected_example_ios,
        output_directory=output_folder,
    )
