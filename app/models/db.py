import os
import sqlite3 as sql
from flask import g
from .. import app
#---------------------------------------------------------------
# https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
#---------------------------------------------------------------

DATABASE = os.path.join(app.root_path, 'models', 'hildegard.db')


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect(DATABASE)
    #end if
    return db
#end def

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
    #end if
#end def

#---------------------------------------------------------------
# end of copied code
#---------------------------------------------------------------

def get_s_classes():
    try:
        con = get_db()
        con.row_factory = sql.Row
        cur = con.cursor()
        
        get_sclasses_query = """
        SELECT SClasses.id, Subjects.name, SClasses.reference from SClasses
        JOIN Subjects on Subjects.id = SClasses.subjectId
        """
        cur.execute(get_sclasses_query)
        data = cur.fetchall()
        cur.close()            
        return data        
    except:
        print("ERROR - Getting user from db")
        return []
    #end try
#end def