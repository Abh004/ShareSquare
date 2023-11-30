# ShareSquare
-----------------------
# Modules used:
> + tkinter 
> + panda/numpy
> + matplotlib
> + pdfkit
> + csv 
> + PostgreSQL

# Schema of DB:
### 1. login 
> + id(pk)
> + name
> + email-id
> + password
### 2. groups
> + id(fk)
> + groupname
> + name
### 3. split
> + id(fk)
> + name
> + debt(pk)
> + payment status