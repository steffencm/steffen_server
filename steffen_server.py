
from flask import (Flask, request, session, g, redirect, url_for, abort,
        render_template, flash, _app_ctx_stack, make_response)


DEBUG=True

app = Flask(__name__)
app.config.from_object(__name__)


navigation_links = [
        ('/', 'home', 'Home'),
        ('/projects', 'projects', 'My Projects'),
        ('/mcserver', 'mc_server', 'MineCraft Server'),
        ('/about', 'about', 'About'),
        ('/contact', 'contact', 'Contact')
    ]


@app.route('/')
def home_page():
    return render_template('home_page.html', navigation_links=navigation_links,
            active_page='home')


@app.route('/projects')
def projects():
    return render_template('projects.html', navigation_links=navigation_links,
            active_page='projects')


@app.route('/mcserver')
def mc_server():
    return render_template('mc_server.html', navigation_links=navigation_links,
            active_page='mc_server')


@app.route('/about')
def about():
    return render_template('about.html', navigation_links=navigation_links,
            active_page='about')


@app.route('/contact')
def contact():
    return render_template('contact.html', navigation_links=navigation_links,
            active_page='contact')


if __name__=='__main__':
    app.run("0.0.0.0")
