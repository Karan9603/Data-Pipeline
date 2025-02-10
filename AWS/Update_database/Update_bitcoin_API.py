import psycopg
import os
import datetime as dt

def add_to_DB (event, context):
    print (event)
    response = event["responsePayload"]
    
    response[0] = dt.datetime.strptime(response[0], '%Y-%m-%d')
    
    dbconn = os.getenv("DBCONN")
    conn = psycopg.connect(dbconn)
    # Create Cursor
    Cur = conn.cursor()

    
    Cur.execute(
        '''
        INSERT INTO "Bitcoin_Data"("Date", "Open", "High", "Low", "Close", "Volumn")
        VALUES (%s, %s, %s, %s, %s, %s);    
        ''',
        (response[0], response[1], response[2], response[3], response[4], response[5])    
        )
        
        
    # commit to all executed queries

    conn.commit ()

    # close the cursor and server Connection
    Cur.close()
    conn.close()

add_to_DB ()

