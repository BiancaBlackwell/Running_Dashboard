import sqlite3
from sqlite3 import Error
import fitbit
import os
import math
from datetime import datetime, timedelta
from fitbit import gather_keys_oauth2 as Oauth2
# Had to copy/paste the gather_keys_oauth2.py from orcasgit/python-fitbit into the fitbit folder
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def fitbitAuthorize():
    # Check: Do we need to do this every time we run, or when?
    server = Oauth2.OAuth2Server(cid_fb, secret_fb)
    server.browser_authorize()
    ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
    REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
    auth2_client = fitbit.Fitbit(cid_fb, secret_fb, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)
    return auth2_client

def fitbitWeekData(auth2_client):
    #WIP: Figure out calling the activities list API properly
    #Collect Activity Data from the Last Week
    endDate = datetime.now()
    startDate = endDate + timedelta(days=-7)
    print(endDate, startDate)

    print(auth2_client.activities_list(beforeDate=endDate, afterDate=startDate, sort='asc', limit=100, offset=0))

if __name__ == '__main__':
    # create_connection(r"..\sqlite\test.db")
    print("Collecting Data from Fitbit API...")
    # TODO authenticate for fitbit API access
    # Collect Full Fitbit HR & Exercise Data from last Week
    auth2_client = fitbitAuthorize()
    fitbitWeekData(auth2_client)
    # TODO update DB with any new events
    # TODO Define table for staistics
    # TODO Update table for statistics
    # TODO generate graphics with latest statistics
