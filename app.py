from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', active_page='home')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', active_page='portfolio')

@app.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact')

@app.route('/signin')
def signin():
    return render_template('signin.html')

# Define route for the Sign Up page
@app.route('/signup')
def signup():
    return render_template('signup.html')

# Define route for the Privacy Policy page
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

# Define route for the Cookie Policy page
@app.route('/cookie')
def cookie():
    return render_template('cookie.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

if __name__ == '__main__':
    app.run(debug=True)