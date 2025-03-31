# BLOGGING_WEBSITE_USING_FLASK_MONGODB

# **Application Setup**
The app connects to **MongoDB** as its database and sets up a system for handling **image uploads**. It ensures:
- A dedicated folder exists to store uploaded images.
- Only **certain image formats** are allowed to prevent errors.
A **secret key** is used to manage user sessions, ensuring that authentication works properly.

**User Authentication System**
Your application has a **login and registration system** that allows users to create an account and sign in.
 **1. User Registration**
- New users can **sign up** using an email, username, and password.
- The system checks if the email is **already registered** before allowing a new account.
- Once registered, the user is **automatically logged in**, and their session begins.

**2. User Login**
- Users enter their **username and password** to log in.
- The system verifies the credentials **against MongoDB**.
- If correct, the user’s **session starts**, allowing them to access their personal blog dashboard.
- If incorrect, an **error message** is displayed.

**Blog Management System**
Users can **create, delete, and view their blogs** once logged in.

**1. Viewing User Blogs**
- Once logged in, users can see **all their previously written blogs**.
- The system fetches blogs based on the **logged-in user’s ID**, ensuring they only see their own content.

**2. Adding a New Blog**
- Users can **write new blog posts** with a title, content, and category.
- They can **upload an image**, which is stored securely.
- The blog is saved in MongoDB, and users are redirected to their list of blogs.

**3. Deleting Blogs**
- Users can **delete their own blogs**, but not anyone else's.
- The system verifies the logged-in user before allowing deletion.
- Once deleted, the blog is **removed from the database** permanently.

---

**Blog Categorization**
The app organizes blogs into **three categories**:  
- **Food**
- **Sports**
- **Fashion**

Each category has its own **dedicated page**, displaying all blogs related to that topic.

When a user visits a category, the system **fetches all blogs labeled under that category** from MongoDB.

**Viewing Blog Posts**
- Users can click on a blog post to **view its full content**.
- Each time a blog is viewed, its **view count is increased by one**, allowing users to track **which blogs are the most popular**.
- The blog details (title, content, image, and view count) are displayed on a separate page.

**Other Features**
**Home Page**
- Displays a general homepage when users visit the site.

**Contact Page**
- Provides a contact form for inquiries.


https://drive.google.com/file/d/1XVgEnmXsDgRwJaYHYPG5ovBrVuRWEtHu/view?usp=sharing    #blogging website using flask. Project name - project_blog
