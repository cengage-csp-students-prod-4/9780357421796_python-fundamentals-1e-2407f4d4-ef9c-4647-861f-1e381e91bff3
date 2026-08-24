## Make it your own

Your implementation is up and running as expected, but as the data grows, TargetCRM needs a way to read and write the data in a more performatic way. Also, the manager will often need to generate reports from the users data, but aggregating values in our current architecture is very resource consuming.

In order to make a more stable solution to support future demand, (taking into account that the data grows in at a fast pace), you can take advantage of data analysis library solutions available in python. For this bonus project, you will be introduced to a very popular python data analysis package, called `pandas`.

`pandas` is a very commonly used python resource and has built-in data structures that are very easy to work with, such as `Series` and `Dataframes`, and several aggregations and analytical functions.

To really stand out in this code delivery, TargetCRM offered you a bonus if you figure out a way to implement a more robust and scalable way to read the raw csv data and return the number of users in the mailing list.

Below there is a general overview of this bonus project:

1. Install the `pandas` package using `pip`
2. Read the csv file into a `pandas` `dataframe`
3. Filter out the unsubscribed users
4. Return the number of active users (the remaining rows)
