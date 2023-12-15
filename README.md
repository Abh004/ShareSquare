# ShareSquare
-----------------------
# Dependencies:
>+ Python 3.12.0 
>+ PostgreSQL & pgAdmin4 to manage the database
>+ pip install all the modules mentioned below

# All the modules used:
>+ tkinter
>> GUI
>+ customtkinter
>> Modern widgets for GUI
>+ pillow
>> Add image manipulation capabilities 
>+ itertools
>> To create complex looping constructs
>+ matplotlib 
>> Plot pie charts
>+ reportlab
>> Export data to PDF
>+ csv 
>> Export data to CSV File
>+ psycopg2
>> PostgreSQL database connection for the application

# SQL commands to create the Database:
### 1. loginpage
```
CREATE TABLE public.loginpage
 (
    id bigserial NOT NULL,
    username character varying NOT NULL,
    name character varying NOT NULL,
    email character varying NOT NULL,
    password character varying NOT NULL,
    PRIMARY KEY (id)
 );

 ALTER TABLE IF EXISTS public.loginpage1
    OWNER to postgres;
```
### 2. groups1
```
CREATE TABLE public.groups1
(
    id bigserial NOT NULL,
    groupname character varying NOT NULL,
    leader character varying NOT NULL,
    members character varying NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.groups1
    OWNER to postgres;
```

### 3. bills1
```
CREATE TABLE public.bills1
(
    id bigserial NOT NULL,
    bill_leader character varying NOT NULL,
    amount character varying NOT NULL,
    debt character varying NOT NULL,
    group_name character varying NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.bills1
    OWNER to postgres;
```