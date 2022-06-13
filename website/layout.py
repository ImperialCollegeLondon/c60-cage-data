from pathlib import Path

from dash import dcc

from .components import data_table


def content() -> list:
    """Generate the content for the webpage.

    Returns:
        list: A list of each component ordered from the top of the page to the bottom.
    """
    with open(Path(__file__).parent / "static" / "index.md", "r") as f:
        md = f.readlines()

    table = data_table(src=Path("data/data_table.csv"))

    return [dcc.Markdown(md), table]
