# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 18:22:57 2024

@author: charl
"""

import mysql.connector
from mysql.connector import Error
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
pw = os.getenv('SQLROOTPASS')

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection



def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
        
        
        
connection = create_server_connection("localhost", "root", pw)
