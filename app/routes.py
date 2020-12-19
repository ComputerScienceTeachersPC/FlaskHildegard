from flask import render_template, request
from . import app
from .models.db import get_s_classes


@app.route("/")
@app.route("/index")
def homepage():
    data = get_s_classes() # returns empty array if error  
    return render_template("index.html", class_data = data) 
#end def    


@app.errorhandler(405)
def wrong_method_405(error):
    return render_template("error.html", error="You are a numpty. You appear to have tried to access a page that doesnt exist")
#end  def

@app.errorhandler(404)
def wrong_method_404(error):
    return render_template("error.html", error="You appear to have tried to access a page that doesnt exist. Try and use the navigation menu, rather than entering url's manually")
#end def