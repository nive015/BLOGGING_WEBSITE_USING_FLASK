from flask import Flask, request, render_template, redirect, url_for,session
from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename
import os
from bson.objectid import ObjectId  # Import ObjectId to handle MongoDB IDs

app = Flask(__name__)
app.secret_key = 'ss@1234'  # Change this to a random string in production

# MongoDB Configuration (Updated database name)
app.config['MONGO_URI'] = "mongodb://127.0.0.1:27017/food_blog_database"  # Updated to new database name
mongo = PyMongo(app)

# Define the directory to store uploaded images
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'uploads')  # Using forward slashes to avoid unicode errors

# Check if the directory exists before creating it
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)  # Create the upload folder if it doesn't exist

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extensions for image uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

# Blogs page route
@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Logic to authenticate the user goes here
        user = mongo.db.users.find_one({"username": username})
        if user and user['password'] == password:  # Use hashed passwords in production
            # Log in the user (set session)
            session['user_id'] = str(user['_id'])  # Store the user ID in session
            return redirect(url_for('user_blogs'))  # Redirect to user blogs

        else:
            error_message = "Invalid credentials. Please register yourself first!"
            return render_template('login.html', error=error_message)

    return render_template('login.html')



#registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('username')

        # Check if the user already exists
        existing_user = mongo.db.users.find_one({"email": email})
        if existing_user:
            return render_template('register.html', error="Username already exists.")

        # Register the new user
        user_id = mongo.db.users.insert_one({
            "email": email,
            "username": username,
            "password": password  # Use hashed passwords in production
        }).inserted_id  # Get the new user's ID

        session['user_id'] = str(user_id)  # Store user ID in session

        return redirect(url_for('user_blogs'))  # Redirect to user blogs after registration

    return render_template('register.html')



#displaying user blogs
@app.route('/user_blogs', methods=['GET'])
def user_blogs():
    user_id = session.get('user_id')
    if user_id is None:
        return redirect(url_for('login'))  # Redirect to login if user is not logged in

    # Retrieve blogs for the logged-in user
    blogs = mongo.db.blogs.find({"user_id": user_id})
    return render_template('user_blogs.html', blogs=blogs)


@app.route('/delete_blog/<blog_id>', methods=['POST'])
def delete_blog(blog_id):
    user_id = session.get('user_id')  # Ensure only the logged-in user's blogs can be deleted
    if user_id:
        # Delete the blog with the provided blog_id and user_id to ensure ownership
        mongo.db.blogs.delete_one({"_id": ObjectId(blog_id), "user_id": user_id})
    return redirect(url_for('user_blogs'))


@app.route('/add_blog', methods=['GET', 'POST'])
def add_blog():
    if request.method == 'POST':
        user_id = session.get('user_id')  # Retrieve the user ID from the session
        if user_id is None:
            return redirect(url_for('login'))  # Redirect to login if user is not logged in

        title = request.form.get('title')
        content = request.form.get('content')
        category = request.form.get('category')
        file = request.files['image']
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(image_path)

            # Save blog to MongoDB
            mongo.db.blogs.insert_one({
                'user_id': user_id,
                'title': title,
                'content': content,
                'category': category,
                'image': filename,
                'view_count': 0
            })

            return redirect(url_for('user_blogs', user_id=user_id))  # Redirect to user blogs after adding

    return render_template('add_blog.html')  # Render the add blog page



@app.route('/contact')
def contact():
    return render_template('contact.html')

# Food blog route
@app.route('/foodblog', methods=['GET', 'POST'])
def food():
    
    # Retrieve all food blogs from MongoDB and pass them to the template
    blogs = mongo.db.blogs.find({"category": "food"})
    
    # Convert ObjectId to string for all blogs before passing to template
    blogs_list = []
    for blog in blogs:
        blog['_id'] = str(blog['_id'])
        blogs_list.append(blog)
    
    return render_template('foodblog.html', blogs=blogs_list)

# Sports blog route
@app.route('/sportsblog', methods=['GET', 'POST'])
def sports():    
    # Retrieve all food blogs from MongoDB and pass them to the template
    blogs = mongo.db.blogs.find({"category": "sports"})
    
    # Convert ObjectId to string for all blogs before passing to template
    blogs_list = []
    for blog in blogs:
        blog['_id'] = str(blog['_id'])
        blogs_list.append(blog)
    
    return render_template('sportsblog.html', blogs=blogs_list)

# Fashion blog route
@app.route('/fashionblog', methods=['GET', 'POST'])
def fashion():
    # Retrieve all food blogs from MongoDB and pass them to the template
    blogs = mongo.db.blogs.find({"category": "fashion"})
    
    # Convert ObjectId to string for all blogs before passing to template
    blogs_list = []
    for blog in blogs:
        blog['_id'] = str(blog['_id'])
        blogs_list.append(blog)
    
    return render_template('fashionblog.html', blogs=blogs_list)



# Route to view a specific blog and increment the view count
@app.route('/view_blog/<blog_id>')
def view_blog(blog_id):
    # Increment the view count for the specific blog
    mongo.db.blogs.update_one({'_id': ObjectId(blog_id)}, {'$inc': {'view_count': 1}})
    
    # Retrieve the updated blog post
    blog = mongo.db.blogs.find_one({'_id': ObjectId(blog_id)})
    
    # Render the detailed blog view
    return render_template('view_blog.html', blog=blog)

if __name__ == '__main__':
    app.run(debug=True)
