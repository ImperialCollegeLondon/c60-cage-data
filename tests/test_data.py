def test_load_data_table():
    from pathlib import Path

    from website.components import data_table

    table = data_table(table_path=Path("data/data_table.csv"))
    assert [i["name"] for i in table.columns] == [
        "entry",
        "cage molecular formula",
        "cage file",
        "complex file",
    ]
