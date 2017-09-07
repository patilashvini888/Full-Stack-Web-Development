**Log Analysis Project**

This project is a reporting tool to answer the below three questions
based on database named “news” in Postgresql and programmed in Python
2.7.9

-   What are the most popular three articles of all time?

-   Who are the most popular article authors of all time?

-   On which days did more than 1% of requests lead to errors?

**What is included?**

-   log\_analysis.py

-   README.txt

-   example\_output.txt

**How to install**

-   Install Vagrant and VirtualBox as per the instructions provided in
    Udacity course

-   Download the VM Configuration here
    <https://github.com/udacity/fullstack-nanodegree-vm>

-   Download newsdata.sql file and copy in the vagrant folder in within
    FSND-Virtual-Machine

-   Create a folder named news in vagrant folder and copy all the above
    three project files in it.

**Required SQL Views to create**

1.  create view total\_views as select date(time) as day, count(\*) as
    view\_count from log group by day order by view\_count desc;

2.  create view failed\_views as select date(time) as day, count(\*) as
    view\_count from log where status='404 NOT FOUND' group by day order
    by view\_count desc;

3.  create view error\_percentage as select
    total\_views.day, round((100.0\*failed\_views.view\_count)/total\_views.view\_count,2)
    as error\_perc from total\_views, failed\_views where
    failed\_views.day=total\_views.day;

**How to run**

-   Have Python 2.7.9 installed and make sure python was added to the
    windows path

-   Navigate to ***cd \\vagrant*** in the VM

-   Now navigate to ***cd \\news*** folder within vagrant

-   Load the newsdata.sql by using the command ***psql –d news –f
    newsdata.sql***

-   Connect to news database using command ***psql news***

-   Create the three listed views above

-   Exit psql

-   Now execute the file using ***python log\_analysis.py***

-   You should see the output as mentioned in the
    example\_output.txt file.


