# Given an input CSV transactional log file with the format illustrated below; write a function in the language of your choice (not SQL) that will take the name of the CSV file and that will print the number of queries per-day per-country.


# Input CSV file format:
# date, country, user_id, query
# YYYY-MM-DD, <two-letter-country-code>, <string-with-no-whitespace>, <string-with-no-whitespace>


# Output format (to screen):
# YYYY-MM-DD  <two-letter-country-code>  <integer>


# Example input from CSV (not necessarily sorted in anyway):
# date, country, user_id, query
# 2011-01-01, US, a123, orange
# 2011-01-01, US, b456, banana
# 2011-01-01, US, c789, apple
# 2011-01-01, UK, a789, banana
# 2011-01-02, US, a123, orange
# 2011-01-02, UK, b456, strawberry


# Expected output (to screen; not necessarily sorted in anyway):
# 2011-01-01  US  3
# 2011-01-01  UK  1
# 2011-01-02  US  1
# 2011-01-02  UK  1


import csv
# import collections

def w_file():
  with open('input.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(['2011-01-01', 'US', 'a123', 'orange'])
    spamwriter.writerow(['2011-01-01', 'US', 'b456', 'banana'])
    spamwriter.writerow(['2011-01-01', 'US', 'c789', 'apple'])
    spamwriter.writerow(['2011-01-01', 'UK', 'a789', 'banana'])
    spamwriter.writerow(['2011-01-02', 'US', 'a123', 'orange'])
    spamwriter.writerow(['2011-01-02', 'UK', 'b456', 'strawberry'])

def r_file():
  with open('input.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
      print(row)
      print(', '.join(row))
      
def print_query_counts():
  count={}
  with open('input.csv', "r") as csvfile:
    spamreader = csv.reader(csvfile)
    # Each row read from the csv file is returned as a list of strings.
    for row in spamreader:
      if (row[0], row[1]) not in count:
        count[(row[0], row[1])] = 1
      else:
        count[(row[0], row[1])] +=1
  return count

w_file()
r_file()
c=print_query_counts()
print(c)
for k, v in c.items():
  print(' '.join(k),v)
 
# Official, actually cannot run through in online python tool due to some obvious errors....   
# import collections
# import csv

# def print_query_counts(filename):

#     # Candidates might not remember collections.defaultdict (which is fine).
#     # Remind its existence if a candidate is stuck; but, otherwise, let her/him use dict().
#     data = collections.defaultdict(int)

#     # Candidates might not remember csv.DictReader (which is fine).
#     # Remind its existence if a candidate is stuck; but, otherwise, let her/him use csv.reader() or just open().
#     for row in csv.DictReader(open(filename, "r")):
#         data[row["date"], row["country"]] += 1

#     for (date, country), count  in data.iteritems():
#         print date, country, count


      
