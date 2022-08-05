from pathlib import Path
from typing import Union

import pandas as pd
from dash import dash_table

PAGE_SIZE = 15


def return_link(row, col_name):
    return "[Download {} {}](assets/{})".format(
        col_name, row[col_name].split("/")[-2], row[col_name]
    )


def data_table(table_path: Union[Path, str]) -> dash_table:
    """
    Generate table
    """
    df = pd.read_csv(table_path).drop("Unnamed: 0", axis=1)

    df["cage file"] = df.apply(lambda row: return_link(row, "cage file"), axis=1)
    df["complex file"] = df.apply(lambda row: return_link(row, "complex file"), axis=1)

    table = dash_table.DataTable(
        id="datatable",
        columns=[{"name": i, "id": i, "presentation": "markdown"} for i in df.columns],
        data=df.to_dict("records"),
        page_size=PAGE_SIZE,
        page_current=0,
    )

    return table
