from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from Client.requester import Requester

app = Flask(__name__)
bootstrap = Bootstrap(app)

client = Requester()

@app.route('/')
def index(items_url="http://localhost:5001/items"):
    return render_template('index.html', items_url=items_url)

@app.route('/items')
def items():
    items_list = client.get_items()
    number_of_cols = 4
    items_with_sublists = [items_list[i:i+number_of_cols] for i in range(0,len(items_list), number_of_cols)]
    number_of_rows = len(items_with_sublists)
    return render_template('all_items.html', items=items_with_sublists, rows=number_of_rows)

@app.route('/item/<id>')
def item(id):
    return render_template('item.html', id=id)


if __name__ == '__main__':
    app.run(debug=True, port=5001)