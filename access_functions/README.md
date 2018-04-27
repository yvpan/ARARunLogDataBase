# access_functions
Examples for how to query the database

## Code
- We have written a rudimentory class of accessor functions in `access_tools.py`.
- To use this class, just import it into your python code `import access_tools as tools`

## example1.py
- This will show you how to query the database to find out if a given run is good for a diffuse analysis.
- It is run like `python example1.py ARA04 3277`.
- But you can also just call `python example1.py` and the code will remind you of this.

## example2.py
- This will show you how to query the database to find all runs which are of a given "quality" (that is, roofpulse, etc.)
- It is run like `python example2.py ARA04 roofpulse`.
- But you can also just call `python example2.py` and the code will remind you of this.