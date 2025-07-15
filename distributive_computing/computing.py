# How to distribute data (task) over different computer (smaller machines) for procesing

# This is a dataset of all Olympic Events that happened between 1896 - 2015
# we want to distribute them into 4 smaller computer 
# Computer A from 1896 - 1925
# Computer B from 1926 - 1955
# Computer C from 1956 - 1985
# Computer D from 1986 - 2015


#Example 1:
# Using Multiprocessing
import multiprocessing as pool

def athlete_avg_age(grouped_data):
    year, group = grouped_data
    return pd.DataFrame({"Age": group["Age"].mean()}, index = [year])

with pool(4) as p:
    athlete_avg = p.map(athlete_avg_age, df.groupby("year"))



#Example 2:
# Using Dask

import dask.dataframe as dd

## partitioning the data
athlete_df = dd.from_pandas(df, npartitions=4)

## computing the average age of all the athletes
result_df = athlete_df.groupby("Year").Age.mean().compute()

