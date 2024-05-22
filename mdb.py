import csv
import mariadb
import sys
from nl_model import get_query
import re

def get_query_results(query):
    try:
        connection = mariadb.connect(
            user="root",
            password="your_password",
            host="your_host",
            port=3306,
            database="your_database"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    cursor = connection.cursor()

    try:
        cursor.execute(query)
    except mariadb.Error as e:
        print("Query failed",e)
        return None

    rows = cursor.fetchall()
    print(rows)

    cursor.close()
    connection.close()


def extract_text_between_curly_braces(input_string):
    pattern = r'\{(.*?)\}'
    pattern2 =  r'\```(.*?)\```'
    matches = re.findall(pattern, input_string)
    matches2 = re.findall(pattern2, input_string)
    if matches!= []:
        return matches[0] 
    elif matches2!=[]:
        return matches2[0]
    else:
        return ""

while True:
    try:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            break
        
        query = get_query(user_input)
        if not query:
            print("Invalid query received from NL model.")
            continue
        
        query_without_backticks = extract_text_between_curly_braces(query)
        if query_without_backticks!="":
            # print(query_without_backticks)
            get_query_results(query_without_backticks)
        else:
            print(query)
            
    except Exception as e:
        print(f"An error occurred: {e}")
        continue
