Question 

This problem has some SQL and coding involved and I like to ask if in person where I can interact with the candidate. 
Here's how I (Keoki) form the question.

We have a table with 5 dimensions (each with 10 unique values) and 1 metric (# of unique users).  
We need to insert pre-calculated 'overall' rows for the dashboard to use since we can't sum(unique users).

1. If I wanted to count distinct users over d1-d5 all possible d? columns, how many rows would I get?

Answer: 10^5
2. Write the query that calculates distinct users

SELECT d1, d2, d3, d4, d5, count(distinct userid) from table group by d1, d2, d3, d4, d5
Then I explain that distinct users is tricky because it does not sum across dimensions. To solve this 
I tell the candidate that we often add a column in the aggregate level table called ‘aggregation’ 
and explain what it means i.e.: (‘d1,d3’ means grouping by d1,d3, and ‘overall’ should be the rest of the column names). 
I also tell them about ‘overall’ and what it means.

3. Then I ask them to write the code to generate this SQL given an array of aggregation levels of the form
['d1', 'd1,d3', 'overall', 'd2,d3,d5']. I tell them that the aggregation levels are ordered (but my solution below does not 
assume that they are).

Code
agg_levels = ['overall', 'd2', 'd1,d2', 'd1,d3,d4,d5']

def get_query(agg_levels):
    all_dims = ['d1', 'd2', 'd3', 'd4', 'd5']
    base_query = """
    SELECT {cols}, COUNT(DISTINCT userid) AS users from table {groupby}
    """
    queries = []
    for agg in agg_levels:
        if agg == 'overall':
            groupby = []
        else:
            groupby = agg.split(',')
        cols = []
        for col in all_dims:
            cols += [col] if col in groupby else ["'overall' AS %s" % col]

        cols = ",".join(cols)
        if len(groupby) > 0:
            groupby = "GROUP BY " + ",".join(groupby)
        else:
            groupby = ""
        queries += [base_query.format(**locals())]

    return "\nUNION ALL\n".join(queries)


## output
> print(get_query(agg_levels))

    SELECT 'overall' AS d1,'overall' AS d2,'overall' AS d3,'overall' AS d4,'overall' AS d5, COUNT(DISTINCT userid) AS users from table

UNION ALL

    SELECT 'overall' AS d1,d2,'overall' AS d3,'overall' AS d4,'overall' AS d5, COUNT(DISTINCT userid) AS users from table GROUP BY d2

UNION ALL

    SELECT d1,d2,'overall' AS d3,'overall' AS d4,'overall' AS d5, COUNT(DISTINCT userid) AS users from table GROUP BY d1,d2

UNION ALL

    SELECT d1,'overall' AS d2,d3,d4,d5, COUNT(DISTINCT userid) AS users from table GROUP BY d1,d3,d4,d5
above code is a solution for without the aggregation column. It's a little trickier to get the aggregation column in but shouldn't be much after they get the first part.
Good candidates will build a template and replace the values in the template for each aggregation level. Often candidates will write the code for the select statement and forget about the group by. 
Also watch for the 'overall' special case. It does not have a group by and needs to be handled separately.
