# C60 Cage Data

A webapp to explore the structures of all complexes and isolated cages constructed by Dr. Marcin Miklitz as part of his PhD. Original data at [https://data.hpc.imperial.ac.uk/resolve/?doi=6054](https://data.hpc.imperial.ac.uk/resolve/?doi=6054). Hosted on the [SupraShare platform](https://suprashare.rcs.ic.ac.uk).

## Development

This app is jointly developed by the [Jelfs Research Group](http://www.jelfs-group.org/) and the Imperial College [Research Software Engineering Team](https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/research-software-engineering/). This repository is based on the [SupraShare template](https://github.com/ImperialCollegeLondon/SupraShare).

### Editing the table

The data table is generated from the raw data `make_index_table.py`. This currently uses [pymatgen](https://pymatgen.org) to generate a formulas from the .xyz files and put these into a very simple table. This script can be adapted as needed to generate a more complex table with more useful columns.

### Data

The data at [https://data.hpc.imperial.ac.uk/resolve/?doi=6054](https://data.hpc.imperial.ac.uk/resolve/?doi=6054) must be extracted into `website/assets/data/` for the download links to work, and for the table to be regenerated using `make_index_table.py`.
