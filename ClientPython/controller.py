from flask import Flask, render_template, flash, url_for, redirect
from flask_bootstrap import Bootstrap
from ClientPython.requester import Requester
from ClientPython.static.Forms.AddListing import AddListingForm
from random import *
from werkzeug.utils import secure_filename
import json
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'super secret key'

client = Requester()

server_url = 'http://localhost:5000/'
pictures_path = 'static/Images/'


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
        picture = form.photo.data
        filename = secure_filename(picture.filename)
        picture.save(os.path.join(pictures_path, filename))
        item = dict(item_id=randint(1, 100000000), seller=randint(1, 100000000), name=form.title.data,
                    price=form.price.data, img=pictures_path + filename, description=form.description.data, ingredients=["string"],
                    lat=0, lng=0)
        try:
            client.post_item(item)
        except Exception as e:
            flash('Oops....Something Went Wrong Creating {}.'.format(form.title.data))
            print("Error Creating Item ", json.dumps(item), "Exception: ", e)
            return render_template('add_listing.html', form=form, title='Add Listing')
        flash('Created Listing for {}'.format(form.title.data))
    return render_template('add_listing.html', form=form, title='Add Listing')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
