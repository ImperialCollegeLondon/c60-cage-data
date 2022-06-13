from pathlib import Path

import pandas as pd
from dash import dcc
from dash import dash_table

PAGE_SIZE = 15


def return_link(row, col_name):
    return "[Download](assets/{})".format(row[col_name])


def content() -> list:
    """Generate the content for the webpage.

    Returns:
        list: A list of each component ordered from the top of the page to the bottom.
    """
    with open(Path(__file__).parent / "static" / "index.md", "r") as f:
        md = f.readlines()

    table_index_path = Path("data/data_table.csv")
    df = pd.read_csv(table_index_path).drop("Unnamed: 0", axis=1)

    df["cage file"] = df.apply(lambda row: return_link(row, "cage file"), axis=1)
    df["complex file"] = df.apply(lambda row: return_link(row, "complex file"), axis=1)

    table = dash_table.DataTable(
        id="datatable",
        columns=[{"name": i, "id": i, "presentation": "markdown"} for i in df.columns],
        data=df.to_dict("records"),
        page_size=PAGE_SIZE,
        page_current=0,
    )

    return [dcc.Markdown(md), table]
