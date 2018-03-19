import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__) # create the application instance
app.config.from_object(__name__) # load config from this file , visort.py
app.config.from_envvar('VISORT_SETTINGS', silent=True)

@app.route('/')
def enter_list():
    return render_template('enter_list.html')