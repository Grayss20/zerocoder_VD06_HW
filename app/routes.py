from flask import render_template, request, redirect, url_for
from app import app


@app.route('/', methods=['GET', 'POST'])
def questionary():
    if request.method == 'POST':
        questi = {
            'name': request.form['name'],
            'city': request.form['city'],
            'hobby': request.form['hobby'],
            'age': request.form['age']
        }
        return render_template('questionary.html', questi=questi)
    return render_template('questionary.html')
