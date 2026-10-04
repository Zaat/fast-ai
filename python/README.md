# Python history

This directory preserves the Python side of the TREE(3) code-golf experiment.

The numbered files show the progression from a relatively readable reference implementation toward increasingly golfed versions. Filenames contain the measured source length at that stage.

Key files:

- `01_763_tree_readable.py` — readable starting point.
- `02_491_tree_golf.py` and later numbered files — progressively shorter variants.
- `15_349_s348.py` — final preserved historical step in the numbered sequence.
- `tree3.py` — current Python entry.
- `shortest_code.py` — helper used during character-count exploration.

The Python history was useful both as an independent conceptual reference and as a source of test data for the C implementation.

The C and Python golf tracks should not be compared only by raw character count: Python and C have very different syntax and runtime assumptions. The point of preserving both is to document the representations and ideas explored during the project.
