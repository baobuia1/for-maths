# Structure
`assets`: graphs (none for now)
`data.csv`: Not raw data. Encrypted from the decryption from raw data (Source: Trust me bro) (Need decryption file).
`data.json`: Processed, "beatified" version of `data.csv`. This file is easier to do analysis and code.
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
`result.md`: Result (ow we make this, results, what can we see about this, how can we improve this,...)
`presentation.pptx`: Slides