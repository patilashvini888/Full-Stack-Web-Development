#! /usr/bin/env python

import psycopg2

DBNAME = "news"


# method to connect to database and return results based on the query parameter
def connectdb(query):
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        results = c.fetchall()
        db.close()
        return results
    except BaseException as e:
        print(e)
        exit(1)

# Queries defined to pass to different methods to solve all three questions
query1 = """select title, count(log.id) as views from articles,
         log where log.path=concat('/article/',articles.slug) and
         log.status='200 OK' group by articles.title order by views
         desc limit 3;"""
query2 = """select authors.name, count(log.status) as view_count from authors,
         articles, log where authors.id = articles.author and
         log.path=concat('/article/',articles.slug) and log.status='200 OK'
         group by authors.name order by view_count desc;"""
query3 = """select to_char(day,'Mon DD,YYYY') as date, error_perc from
         error_percentage where error_perc>1.0;"""


# Methods defined to print answers to all three questions
# Question 1: What are the most popular three articles of all time?
def most_popular_articles():
    top_three_articles = connectdb(query1)
    print("----- The three most popular articles of all time are -----")
    for i in top_three_articles:
        print('"' + i[0] + '" -- ' + str(i[1]) + " views")


# Question 2: Who are the most popular article authors of all time?
def most_popular_authors():
    poupular_authors = connectdb(query2)
    print("----- The most popular article authors of all time are -----")
    for i in poupular_authors:
        print(i[0] + ' -- ' + str(i[1]) + ' views')


# Question 3: On which days did more than 1% of requests lead to errors?
def maximum_errors():
    max_errors = connectdb(query3)
    print("----- The days on which more than 1% of requests lead to errors"
          " are -----")
    for date, error_perc in max_errors:
        print("%s -- %.2f%%" % (date, error_perc) + " errors")

# Calls all three funtions upon execution of this file
if __name__ == '__main__':
    print("\n")
    print("***** Generating Results *****")
    print("\n")
    most_popular_articles()
    print("\n")
    most_popular_authors()
    print("\n")
    maximum_errors()
    print("\n")
