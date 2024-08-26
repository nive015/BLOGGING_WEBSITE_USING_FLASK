import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from PIL import Image
st.set_page_config(
    page_icon="robo.jfif",
    layout="wide",
    initial_sidebar_state="auto",
    )
st.markdown("""
    <style>
        .main {
            background-color: black;
            color:white; /* bg for main area*/
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
st.markdown('<h1 style="color:red;font-family:Algerian;font-size:+2;">Classification Algorithms</h1><hr>', unsafe_allow_html=True)
#sidebar image
i_path = "robo.jfif"
image = Image.open(i_path)
st.sidebar.image(image, caption="", use_column_width=True)

# File uploader
st.write("Accepted File Formats: csv, xlsx.")
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])

if uploaded_file is not None:
    df = None

    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file format. Please upload a CSV or XLSX file.")

        # 1. Data Cleaning and Preprocessing
        st.markdown("""<h2 class="h2tags">Data Cleaning and Preprocessing</h2>""",unsafe_allow_html=True)
        # Handling missing values
        if st.checkbox(label="Fill missing values"):
            numeric_cols = df.select_dtypes(include=['number']).columns
            non_numeric_cols = df.select_dtypes(exclude=['number']).columns
            
            # Handle missing values
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
            for column in non_numeric_cols:
                df[column] = df[column].fillna(df[column].mode()[0])

            # Convert non-numeric data to numeric using Label Encoding
            label_encoders = {}
            for column in non_numeric_cols:
                try:
                    label_encoders[column] = LabelEncoder()
                    df[column] = label_encoders[column].fit_transform(df[column])
                except Exception as e:
                    st.error(f"Error encoding {column}: {e}")
        st.markdown("""<h2 class="h2tags">Data After Preprocessing</h2>""",unsafe_allow_html=True)
        st.write(df.head(40))

        # Split data into features and target
        target_column = st.selectbox("Select", df.columns)
        X = df.drop(columns=target_column)
        y = df[target_column]
            
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # 2. Model Training and Evaluation
        st.markdown("""<h2 class="h2tags">Model Training and Evaluation</h2>""",unsafe_allow_html=True)

        options = ["Decision Tree", "Random Forest Tree", "K-Nearest Neighbor",
                   "Logistic Regression", "Support Vector Machine", "Naive Bayes"]
        
        selected_option = st.selectbox("Choose an option:", options)
        st.write(f"You selected: {selected_option}")

        model = None
        if selected_option == "Decision Tree":
            model = DecisionTreeClassifier()
        elif selected_option == "Random Forest Tree":
            model = RandomForestClassifier(n_estimators=100)
        elif selected_option == "K-Nearest Neighbor":
            k = st.slider("Select the value of k:", min_value=1, max_value=20, value=5)
            model = KNeighborsClassifier(n_neighbors=k)
        elif selected_option == "Logistic Regression":
            model = LogisticRegression()
        elif selected_option == "Support Vector Machine":
            model = SVC(kernel='linear')
        elif selected_option == "Naive Bayes":
            model = GaussianNB()

        # Train the model
        if model is not None:
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            # Evaluate the model
            accuracy = accuracy_score(y_test, y_pred)
            st.write(f"Model Accuracy: {accuracy:.2f}")
            st.write("Confusion Matrix:")
            st.write(confusion_matrix(y_test, y_pred))
            st.write("Classification Report:")
            st.write(classification_report(y_test, y_pred))

            # Plotting options
            st.markdown("""<h2 class="h2tags">Visualization</h2>""",unsafe_allow_html=True)

            plot_option = st.selectbox("Choose a plot to visualize:", ["None", "Decision Boundary", "Scatter Plot", "Bar Chart", "Line Plot", "Histogram"])

            if plot_option == "Decision Boundary":
                if X.shape[1] == 2:  # Decision boundary plot only works with 2 features
                    h = .02  # Step size in the mesh
                    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
                    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
                    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
                    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
                    Z = Z.reshape(xx.shape)
                    
                    fig, ax = plt.subplots(figsize=(10, 6))
                    ax.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.coolwarm)
                    ax.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', marker='o', cmap=plt.cm.coolwarm)
                    ax.set_xlabel('Feature 1')
                    ax.set_ylabel('Feature 2')
                    ax.set_title('Decision Boundary')
                    st.pyplot(fig)
                else:
                    st.warning("Decision boundary plot is only available for datasets with exactly 2 features.")

            elif plot_option == "Scatter Plot":
                if X.shape[1] >= 2:  # Scatter plot requires at least 2 features
                    fig, ax = plt.subplots(figsize=(10, 6))
                    sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y, palette='viridis', ax=ax)
                    ax.set_xlabel('Feature 1')
                    ax.set_ylabel('Feature 2')
                    ax.set_title('Scatter Plot of Features')
                    ax.legend(title='Target')
                    st.pyplot(fig)
                else:
                    st.warning("Scatter plot requires at least 2 features.")

            elif plot_option == "Bar Chart":
                bar_column = st.selectbox("Select column for bar chart:", df.columns)
                fig, ax = plt.subplots(figsize=(10, 6))
                df[bar_column].value_counts().plot(kind='bar', ax=ax)
                ax.set_xlabel(bar_column)
                ax.set_ylabel('Count')
                ax.set_title(f'Bar Chart of {bar_column}')
                ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
                st.pyplot(fig)

            elif plot_option == "Line Plot":
                x_column = st.selectbox("Select x column for line plot:", df.columns)
                y_column = st.selectbox("Select y column for line plot:", df.columns)
                if x_column and y_column:
                    fig, ax = plt.subplots(figsize=(10, 6))
                    df.plot(kind='line', x=x_column, y=y_column, ax=ax)
                    ax.set_xlabel(x_column)
                    ax.set_ylabel(y_column)
                    ax.set_title(f'Line Plot of {y_column} vs {x_column}')
                    st.pyplot(fig)
                else:
                    st.warning("Select at least two columns for the line plot.")

            elif plot_option == "Histogram":
                hist_column = st.selectbox("Select column for histogram:", df.columns)
                fig, ax = plt.subplots(figsize=(10, 6))
                df[hist_column].plot(kind='hist', bins=30, ax=ax)
                ax.set_xlabel(hist_column)
                ax.set_ylabel('Frequency')
                ax.set_title(f'Histogram of {hist_column}')
                st.pyplot(fig)

        else:
            st.write("Model is none")

    except Exception as e:
        st.error(f"An error occurred: {e}")

else:
    st.warning(f"The File {uploaded_file.name} is not in mentioned format!!\nUpload a file which is in csv format!")