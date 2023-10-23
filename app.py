from flask import Flask, render_template
import os

app = Flask(__name__)

# Define a function to render and save HTML pages as static files
def render_and_save_template(template_name, filename):
    with app.app_context():
        template = render_template(template_name)
        with open(os.path.join('docs', filename), 'w', encoding='utf-8') as file:
            file.write(template)

@app.route('/')
def home():
    render_and_save_template('index.html', 'index.html')
    return render_template('index.html', active_page='home')

@app.route('/about.html')
def about():
    render_and_save_template('about.html', 'about.html')
    return render_template('about.html', active_page='about')

@app.route('/portfolio.html')
def portfolio():
    render_and_save_template('portfolio.html', 'portfolio.html')
    return render_template('portfolio.html', active_page='portfolio')

@app.route('/contact.html')
def contact():
    render_and_save_template('contact.html', 'contact.html')
    return render_template('contact.html', active_page='contact')

@app.route('/signin.html')
def signin():
    render_and_save_template('signin.html', 'signin.html')
    return render_template('signin.html')

# Define route for the Sign Up page
@app.route('/signup.html')
def signup():
    render_and_save_template('signup.html', 'signup.html')
    return render_template('signup.html')

# Define route for the Privacy Policy page
@app.route('/privacy.html')
def privacy():
    render_and_save_template('privacy.html', 'privacy.html')
    return render_template('privacy.html')

# Define route for the Cookie Policy page
@app.route('/cookie.html')
def cookie():
    render_and_save_template('cookie.html', 'cookie.html')
    return render_template('cookie.html')

@app.route('/terms.html')
def terms():
    render_and_save_template('terms.html', 'terms.html')
    return render_template('terms.html')

if __name__ == '__main__':
    app.run(debug=True)
