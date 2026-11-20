# Results (Vivi)

## RQ1: How do overdose death rates differ across WV counties?

Overdose rates are available for 45 of West Virginia's 55 counties. The average is 76.1 deaths per 100,000 people, the median is 63.5, and the standard deviation is 35.8, so the rates spread widely.

- Highest: McDowell (180.7), Logan (164.4), Raleigh (138.0), Cabell (131.8) and Wyoming (119.9).
- Lowest: Randolph (27.4), Upshur (34.9), Preston (36.3), Barbour (38.0) and Marshall (41.1).

Compared with the national reference rate of 31.3, 44 of the 45 counties are above it. Only Randolph falls below. In 24 counties the rate is more than double the national figure.

Caveat: 10 counties have no data because they recorded fewer than 10 deaths over three years. They are left out, so this picture may be biased. These counties likely have lower rates, which means the share of counties above the national rate is probably overstated.

## RQ3: Do the four factors help predict overdose rates?

I tested this by splitting the data into train and test sets 100 times and comparing the average test RMSE (prediction error). A simple baseline model scored 34.46. The model using all four factors scored 30.75, so it had the lower error.

The four-factor model beat the baseline in 81 of the 100 splits. The improvement is about 3.7 points, but the results vary a lot from split to split. The model helps a little, but it is not accurate enough to rely on for predictions.

Limitation: with only 45 counties (36 for training and 9 for testing), results can change a lot if one or two counties move between the train and test sets.