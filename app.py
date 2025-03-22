from flask import Flask, render_template, request, redirect, url_for
from database import init_db, get_db
from models import Item

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        db = get_db()
        db.execute('INSERT INTO items (name, quantity) VALUES (?, ?)', (name, quantity))
        db.commit()
        return redirect(url_for('view_items'))
    return render_template('add_item.html')

@app.route('/items')
def view_items():
    db = get_db()
    items = db.execute('SELECT * FROM items').fetchall()
    return render_template('view_items.html', items=items)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
