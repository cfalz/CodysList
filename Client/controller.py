from flask import Flask, render_template, flash, url_for, redirect
from flask_bootstrap import Bootstrap
from Client.requester import Requester
from Client.static.Forms.AddListing import AddListingForm
from random import *
import json

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'super secret key'

client = Requester()

server_url = 'http://localhost:5000/'


@app.route('/')
def index():
    return get_items()


@app.route('/listings')
def listings():
    return get_items()


def get_items():
    items_list = client.get_items()
    number_of_cols = 4
    items_with_sublists = [items_list[i:i + number_of_cols] for i in range(0, len(items_list), number_of_cols)]
    number_of_rows = len(items_with_sublists)
    return render_template('all_items.html', items=items_with_sublists, rows=number_of_rows)


@app.route('/item/<id>')
def item(id):
    return render_template('item.html', id=id)


@app.route('/add_listing', methods=['GET', 'POST'])
def add_listing():
    form = AddListingForm()
    if form.validate_on_submit():
        item = dict(item_id=randint(1, 100000000), seller=randint(1, 100000000), name=form.title.data,
                    price=form.price.data, img="string", description=form.description.data, ingredients=["string"],
                    lat=0, lng=0)
        try:
            client.post_item(item)
        except Exception as e:
            flash('Oops....Something Went Wrong Creating {}.'.format(form.title.data))
            print("Error Creating Item ", json.dumps(item), "Exception: ", e)
            return render_template('add_listing.html', form=form, title='Add Listing')
        flash('Ceated Listing for {}'.format(form.title.data))
        return redirect(url_for('index'))
    return render_template('add_listing.html', form=form, title='Add Listing')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
