from flask import render_template, request
from . import app
from .models.db import *


@app.route("/")
@app.route("/index")
def homepage():
    try:
        con = get_db()
        con.row_factory = sql.Row
        cur = con.cursor()
        
        get_user_query = """
        SELECT SClasses.id, Subjects.name, SClasses.reference from SClasses
        JOIN Subjects on Subjects.id = SClasses.subjectId
        """
        cur.execute(get_user_query)
        data = cur.fetchall()
        cur.close()            
        if data is not None:
            return render_template("index.html", class_data = data) 
        #end if         
    except:
        print("ERROR - Getting user from db")
        return render_template("index.html", class_data = [])
    #end try
#end def    


@app.errorhandler(405)
def wrong_method_405(error):
    return render_template("error.html", error="You are a numpty. You appear to have tried to access a page that doesnt exist")
#end  def

@app.errorhandler(404)
def wrong_method_404(error):
    return render_template("error.html", error="You appear to have tried to access a page that doesnt exist. Try and use the navigation menu, rather than entering url's manually")
#end def