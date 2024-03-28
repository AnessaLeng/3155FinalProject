from flask import Flask, redirect, render_template, request, url_for
from random import randint

app = Flask(__name__)
profile_info = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def show_profile():
    user_pic = "static/user_icon.png"
    username = "username here"
    bio = "bio here"
    followers = "###"
    following = "###"
    posts= ['static/placeholder.png', 'static/placeholder.png', 'static/placeholder.png', 'static/placeholder.png',
            'static/placeholder.png','static/placeholder.png','static/placeholder.png','static/placeholder.png']
    profile_info[username] = []
    profile_info[username].append(user_pic)
    profile_info[username].append(bio)
    profile_info[username].append(followers)
    profile_info[username].append(following)
    return render_template("profile.html", profile_info = profile_info, posts = posts)

users = {}

# Anessa's signup/login feature
@app.route('/')
def index():
    if request.method == 'GET' and request.form.get('signup'):
        return render_template('index.html', is_user=2)
    elif request.method == 'GET' and request.form.get('login'):
        return render_template('index.html', is_user=1, error=False)
    return render_template('index.html', is_user=0)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')
        email = request.form.get('email')
        dob = request.form.get('dob')
        profile_image = request.form.get('profile_image')
        #with open(profile_image, 'rb') as file:
        #    image_data = file.read()
        uid = randint(1, 9999)

        new_user = {
            "uid": uid,
            "first_name": first_name,
            "last_name": last_name,
            "password": password, 
            "email": email,
            "dob": dob,
            "profile_image": profile_image#image_data
        }

        users[uid] = new_user

        return redirect(url_for('profile'))
    return render_template('index.html', is_user=2)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        for uid, user in users.items():
            if user['email'] == email and user['password'] == password:
                return redirect(url_for('profile'))
        error_message = "Invalid email or password"
        return render_template('index.html', is_user=1, error=True, error_message=error_message)
    return render_template('index.html', is_user=1, error=False)

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    return render_template('profile.html')

# Cindy's create a post feature
@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        price = request.form.get('price')
        hashtags = request.form.get('hashtags')
        description = request.form.get('description')

        print("Title:", title)
        print("Price:", price)
        print("Hashtags:", hashtags)
        print("Description:", description)
        return "You have succesfully created a listing!"

    return render_template('create_post.html')
