from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    item = request.form['item']
    description = request.form['description']
    new_request = Request(item=item, description=description)
    db.session.add(new_request)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/requests')
def view_requests():
    requests = Request.query.all()
    return render_template('requests.html', requests=requests)

@app.route('/approve/<int:id>', methods=['POST'])
def approve(id):
    req = Request.query.get(id)
    req.status = 'Approved'
    db.session.commit()
    return redirect(url_for('view_requests'))

