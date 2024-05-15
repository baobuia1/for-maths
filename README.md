# Structure
`assets`: graphs (none for now)

`data.csv`: Not raw data. Encrypted from the decryption from raw data (Source: Trust me bro) (Need decryption file).

`data.json`: Processed, "beautified" version of `data.csv`. This file is easier to do analysis and code.

`extractor.py`: Turn `data.csv` to `data.json` (DO NOT TOUCH).

`main.py`: do analysis (TO DO).

# Data structure
`data.json`:
```json
[
    {
        "SBD": [literature_score, maths_score, language_score]
    }
]
```
In this case: `literature_score`, `maths_score`, `language_score` are all float numbers.

# TO DO
`main.py`: Statistic

`draw.py`: Graphs
