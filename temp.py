import os
from mysql import connector

PASSWORD = 'ysol1234'

try:
    with connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = PASSWORD
    ) as database: 
        print(f"Database object: {database}")
except connector.Error as e: 
    print(e)