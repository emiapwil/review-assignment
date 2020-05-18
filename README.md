# How to use

Put the constraints in `test.json` and simply run the following command

`python3 assign.py test.json`

Make sure you have `networkx` installed.

The output is a list of (reviewer, paper) mappings, separated by a comma.

# How to configure the constraints

The constraint file is a JSON file with three members:

- `reviewers`: a dictionary of reviewers. The key is the name and the value is a
  dictionary with only one member called `number-of-papers` which indicates the
  maximum number of papers this reviewer can accept.

- `papers`: a dictionary of papers. The key is the id of the paper and the value
  is a dictionary with only one member called `number-of-reviewers` which
  represents the maximum number of reviews this paper can receive.

- `conflicts`: a list of conflicting relations. If a paper Y marked reviewer X
  as conflict, an entry `[X, Y]` must be put into this list.

See `test.json` as an example.
