# Union Avatars technical test:

## This technical test was exclusively made by Sergio Domínguez's for the Union Avatar job application:
##

### 1. Install the dependencies:

- In case we don't have the python package installer, you can use the following commands:
  
    `python3 install pip`

    `pip install django`


### 2. Download & Import the database data:

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

### 3. Run and test the Django project:

- First step is to run the server locally:

    `python3 manage.py runserver`

- Now, test the endpoints:

    - Given an AS number, return the AS information 

        Testing the first one with, for example, 28110:

        `http://127.0.0.1:8000/asinfowithasnum/28110/`

        The response should be the following:

        <details closed>
        <summary>See response</summary>

        ``` json
        
        [
            {
                "id": 87392,
                "range_start": "69.25.4.0",
                "range_end": "69.25.4.255",
                "as_number": "28110",
                "country_code": "CR",
                "as_description": "NAVEGALO S.A."
            },
            {
                "id": 206123,
                "range_start": "131.196.32.0",
                "range_end": "131.196.35.255",
                "as_number": "28110",
                "country_code": "CR",
                "as_description": "NAVEGALO S.A."
            },
            {
                "id": 211578,
                "range_start": "138.59.132.0",
                "range_end": "138.59.135.255",
                "as_number": "28110",
                "country_code": "CR",
                "as_description": "NAVEGALO S.A."
            },
            {
                "id": 277177,
                "range_start": "181.174.168.0",
                "range_end": "181.174.171.255",
                "as_number": "28110",
                "country_code": "CR",
                "as_description": "NAVEGALO S.A."
            },
            {
                "id": 315390,
                "range_start": "190.124.248.0",
                "range_end": "190.124.251.255",
                "as_number": "28110",
                "country_code": "CR",
                "as_description": "NAVEGALO S.A."
            },
            {
                "id": 315961,
                "range_start": "190.184.196.0",
                "range_end": "190.184.199.255",
                "as_number": "28110",
                "country_code": "CR",
                "as_description": "NAVEGALO S.A."
            },
            {
                "id": 325526,
                "range_start": "192.142.224.0",
                "range_end": "192.142.224.255",
                "as_number": "28110",
                "country_code": "CR",
                "as_description": "NAVEGALO S.A."
            }
        ]

        ```
        </details><br><br>

    - Given an IP address (v4 or v6), find the AS that owns the network that the IP belongs to, and return the AS information 

        We can test, for example, with the following URL:

        `http://127.0.0.1:8000/asinfowithip/130.192.30.0/`

        The response should be the following:

        <details closed>
        <summary>See response</summary>

        ``` json
        [
            {
                "id": 204080,
                "range_start": "130.192.0.0",
                "range_end": "130.192.255.255",
                "as_number": "137",
                "country_code": "IT",
                "as_description": "ASGARR Consortium GARR"
            }
        ]
        ```


