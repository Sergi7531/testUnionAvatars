# Union Avatars technical test:

## This technical test was exclusively made by Sergio Domínguez's for the Union Avatar job application:
##

#### 1. Install the dependencies:

- In case we don't have the python package installer, you can use the following command:

    `python3 install pip`

    `pip install django`


#### 2. Import the database data:

- In a terminal in the project folder, run the following command:

    `curl https://iptoasn.com/data/ip2asn-v4.tsv.gz >> dbdata.tsv`

- Next up, open SQLite: 
  
    `sqlite3 db.sqlite3`

- Now, import the database:<br>

    (This commands have no output, so you are good to go if you get no response at all)
    
    In the SQLite console, run the following command:<br>
    `.separator "\t"`

    If this doesn't work, try the following:<br>

    `.mode tabs`

- Last but not least, populate the table with this command:<br>

    `.import /path/to/dbdata.tsv asAPI_asinformation;`

    (replace `/path/to/dbdata.tsv` with the path to the file you just downloaded, of course)

    

    