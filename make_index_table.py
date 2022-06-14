"""
Simple script to generate a table from the cage data in the data directory.
NOTE: Pymatgen is required to read .xyz to Molecule objects and access their .formula
property, but this is not included in environment.yml as it's not required to run the
webapp. Any other library that can read .xyz files could be used.
"""

from pathlib import Path

import pandas as pd
from pymatgen.core import Molecule
from tqdm import tqdm

cage_path = Path("data/array_all_cage/")
complex_path = Path("data/array_all_comp/")

cage_data = []
for i in tqdm(range(0, 3870)):
    cage_mol = Molecule.from_file(cage_path / str(i) / f"{i}.xyz")
    cage_data.append(
        {
            "entry": i,
            "cage molecular formula": cage_mol.formula,
            "cage file": str(cage_path / str(i) / f"{i}.xyz"),
            "complex file": str(complex_path / str(i) / f"{i}.xyz"),
        }
    )

df = pd.DataFrame(cage_data)
df.to_csv("data/data_table.csv")
