from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Request
from datetime import datetime

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

@app.route('/requests', methods=['GET', 'POST'])
def view_requests():
    if request.method == 'POST':
        filter_status = request.form.get('status')
        filter_date = request.form.get('date')
        filter_employee = request.form.get('employee')

        query = Request.query

        if filter_status:
            query = query.filter_by(status=filter_status)
        if filter_date:
            query = query.filter(Request.timestamp >= datetime.strptime(filter_date, '%Y-%m-%d'))
        if filter_employee:
            query = query.filter_by(evaluator=filter_employee)
        
        requests = query.all()
    else:
        requests = Request.query.all()

    return render_template('requests.html', requests=requests)

@app.route('/evaluate/<int:id>', methods=['GET', 'POST'])
def evaluate(id):
    req = Request.query.get(id)
    if request.method == 'POST':
        req.status = request.form['status']
        req.evaluation_reason = request.form['reason']
        req.evaluator = request.form['evaluator']
        db.session.commit()
        return redirect(url_for('view_requests'))
    return render_template('evaluate.html', request=req)
