from flask import Flask, render_template, request, redirect, url_for, flash
import string
import random
from models import db, URLMapping

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url_shortener.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Replace with your own secret key

db.init_app(app)

# Function to generate a random short URL
def generate_short_url(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        short_url = ''.join(random.choice(characters) for _ in range(length))
        if not URLMapping.query.filter_by(short_url=short_url).first():
            return short_url

def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        if long_url:
            url_mapping = URLMapping.query.filter_by(long_url=long_url).first()
            if url_mapping:
                short_url = url_mapping.short_url
            else:
                short_url = generate_short_url()
                new_mapping = URLMapping(long_url=long_url, short_url=short_url)
                db.session.add(new_mapping)
                db.session.commit()
                
            flash(f'Short URL: {request.url_root}{short_url}', 'success')
            return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    url_mapping = URLMapping.query.filter_by(short_url=short_url).first()
    if url_mapping:
        return redirect(url_mapping.long_url)
    else:
        flash('URL not found!', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
