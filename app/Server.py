import os
from flask import Flask, render_template

template_dir = os.path.abspath('app/web/templates')
app = Flask(__name__,  static_folder=os.path.abspath('app/web/static/'),
            template_folder = template_dir)


@app.route('/')
def index():
    return render_template('public/index.html', title="Home")

@app.route('/about/')
def about():
    return render_template('public/about.html', title="About")

@app.route('/contact/')
def contact():
    return render_template('public/contact.html', title="Contact")

@app.route('/blog/')
def blog():
    return render_template('public/blog.html', title="Blog")

if __name__ == '__main__':
    app.run(debug=True, port=5003)
