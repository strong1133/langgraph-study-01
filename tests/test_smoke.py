import runpy
from pathlib import Path

from langgraph.graph import StateGraph


def test_langgraph_is_available() -> None:
    assert StateGraph is not None


def test_main(capsys) -> None:
    main_path = Path(__file__).parents[1] / "main.py"
    runpy.run_path(str(main_path), run_name="__main__")
    assert capsys.readouterr().out == "Hello from langgraph-study-01!\n"
