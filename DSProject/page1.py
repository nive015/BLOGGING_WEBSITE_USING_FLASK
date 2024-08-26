import streamlit as st
from PIL import Image
st.set_page_config(
    page_icon="robo.jfif",
    layout="wide",
    initial_sidebar_state="auto",
    )
# Apply custom CSS styles
st.markdown("""
    <style>
        .main {
            background-color: black; 
           /* bg for main area*/
        }
       .st-emotion-cache-1gv3huu { 
            background-color: red;
            color: #FF0000; /*sidebar bg*/
        }
        .st-emotion-cache-12fmjuu ezrtsby2{
            background-color: red; /*deploy thing bg*/
        }
       .st-emotion-cache-6qob1r eczjsme11{
            color: white; /*sidebar-content*/
        }
        .h2tags {
            color: #00FFFF;
            font-weight: bold;
        }
        .h3tags {
            color: white;
            font-size: +2;
            text-align: center;
        }
        ."st-emotion-cache-j7qwjs eczjsme15{
            font-color:white;
        }
    </style>
    """, unsafe_allow_html=True)

# Main title
st.markdown('<h1 style="color:red;font-family:Algerian;font-size:+2;">Classification Algorithms</h1><hr>', unsafe_allow_html=True)
#st.markdown("""<span class="st-emotion-cache-1rtdyuf eczjsme13" style="color:red;">page1</span>""",unsafe_allow_html=True)
# Content
st.markdown("""
    <h2 class="h2tags">What is Classification?</h2><br><br>
    <h3 class="h3tags">Classification is a type of supervised learning in machine learning where the model learns to categorize data points into predefined classes.<br>
    The goal is to predict the category or class label of new data points based on the model's training on labeled data.</h3>
    <h2 class="h2tags">Types of Classification Algorithms</h2>
    <h3 class="h3tags">
       <div style="text-align:left;"> 1. Decision Tree:</div><br><div style="text-align:right;"> A Decision Tree Classifier is a supervised machine learning algorithm used for classification tasks. It works by recursively splitting the dataset into subsets based on the value of input features. The goal is to create a model that predicts the target variable by learning simple decision rules inferred from the data features.</div><br><br>
       <div style="text-align:left;"> 2. Random Forest:</div><br><div style="text-align:right;"> A Random Forest Classifier is an ensemble learning method used for classification tasks. It combines multiple decision trees to improve the robustness and accuracy of predictions. By aggregating the results from many individual trees, it reduces the risk of overfitting and increases the generalization capability of the model.</div><br><br>
       <div style="text-align:left;"> 3. K-Nearest Neighbors (KNN):</div><br><div style="text-align:right;"> K-Nearest Neighbors (KNN) is a straightforward and effective classification algorithm, particularly useful when the data is relatively small and low-dimensional. Its performance can be influenced by the choice of k and the distance metric, so proper tuning and validation are essential for optimal results.</div><br><br>
       <div style="text-align:left;"> 4. Logistic Regression:</div><br> <div style="text-align:right;">Logistic Regression is a widely used and simple classification algorithm. It is effective for binary classification problems and provides probabilistic predictions. It is particularly useful when you need a straightforward model with interpretable results.</div><br><br>
       <div style="text-align:left;"> 5. Support Vector Machine (SVM):</div> <br><div style="text-align:right;">Support Vector Machines (SVMs) are powerful classifiers that can handle both linear and non-linear data. By maximizing the margin between classes and utilizing different kernels, SVMs are versatile and effective for complex classification problems. Proper tuning of parameters is crucial for achieving the best performance.</div><br><br>
       <div style="text-align:left;"> 6. Naive Bayes:</div><br><div style="text-align:right;">Naive Bayes is a probabilistic classifier based on Bayes' Theorem with an assumption of independence between features. It is particularly effective for large datasets and works well with text classification problems.</div><br></h3>
    """, unsafe_allow_html=True)
# Sidebar image
i_path = "robo.jfif"
image = Image.open(i_path)
st.sidebar.image(image, caption="", use_column_width=True)

