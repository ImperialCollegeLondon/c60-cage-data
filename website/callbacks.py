from pathlib import Path

import dash_bootstrap_components as dbc
from dash import callback
from dash.dependencies import Input, Output, State


@callback(
    Output("run-card", "children"),
    Input("add-button", "n_clicks"),
    State("run-card", "children"),
)
def add_row(n_clicks: int, children: list) -> list:
    """Adds a row to the card with the model results when "Add Row" button is clicked.

    Each object in the row is provided with a dictionary id so that they can be used
    correctly with pattern-matching callbacks.

    Args:
        n_clicks (int): Increments on a button click. The trigger for this callback.
        children (list): The children of the card. Contains dbc.Row or dbc.Form.

    Returns:
        list: The updated children. Equivalent to the input children plus a Form/Row
    """
    if n_clicks is None:
        n_clicks = 0

    form = dbc.Form(
        dbc.Row(
            [
                dbc.Col(
                    dbc.Input(type="text", id=dict(type="lk", index=n_clicks)),
                ),
                dbc.Col(
                    dbc.Input(type="text", id=dict(type="bb", index=n_clicks)),
                ),
                dbc.Col(
                    [
                        dbc.Select(
                            id=dict(type="model-dropdown", index=n_clicks),
                            value="amine2aldehyde3",
                            options=[
                                {"label": model.stem, "value": model.stem}
                                for model in Path("models").glob("*")
                            ],
                        ),
                    ]
                ),
                dbc.Col(
                    dbc.Button(
                        "Run Model \U0001F680",
                        id=dict(type="run-button", index=n_clicks),
                        color="primary",
                    ),
                    class_name="d-grid gap-2",
                ),
                dbc.Col(dbc.Spinner(dbc.Label(id=dict(type="result", index=n_clicks)))),
            ],
            align="center",
        )
    )
    return children + [form]
