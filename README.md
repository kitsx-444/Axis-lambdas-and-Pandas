# Forex Sentiment Consolidator

This program reads two CSV files and returns a tabulated and scored signal based on the CSV's data. For example, if the pips are greater than 0 and the sentiment is bullish, under a newly created column named signal, on the row of the Bullish row a 'Buy' signal will be printed out.

### What I learned:
1. pd.merge() function.
2. apply() function and using it in accordance with lambda.
3. axis. axis=1 tells Python parse over rows, axis=0 tells Python parse over columns. I used axis=1 because I wanted the lambda function to iterate over my data frames rows.

### Future goals:
Getting closer to creating a fundamental scorer.
