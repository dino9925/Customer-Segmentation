import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import os
from fpdf import FPDF
import google.generativeai as genai
import dask.dataframe as dd
import smtplib
import random
import string
import plotly.express as px

USERS_FILE = "users.csv"
Mall_Customer_file = "Mall_Customers.csv"
Customer_file = "Customer Data.csv"

def load_users():
    if os.path.exists(USERS_FILE):
        users_df = pd.read_csv(USERS_FILE, dtype={"username": str, "password": str})
        return users_df
    else:
        return pd.DataFrame(columns=["username", "password"])


def save_user(username, password):
    users_df = load_users()
    new_user = pd.DataFrame({"username": [username], "password": [password]})
    users_df = pd.concat([users_df, new_user], ignore_index=True)
    users_df.to_csv(USERS_FILE, index=False)


query_params = st.query_params

if "authenticated" not in st.session_state:
    st.session_state.authenticated = query_params.get("authenticated", "false") == "true"
if "current_user" not in st.session_state:
    st.session_state.current_user = query_params.get("current_user", "")
if "current_page" not in st.session_state:
    st.session_state.current_page = query_params.get("page", "Log-in")  

def auth_menu():
    with st.sidebar:
        return option_menu(
            "Main", ["Log-in", "Sign-Up"],
            default_index=0, menu_icon="house",
            icons=["lock", "unlock"], orientation="vertical"
        )


def navigation_menu():
    with st.sidebar:
        return option_menu(
            "Navigation", ["Dashboard", "Projects", "Dataset", "Analytics", "Chatbot", "Logout"],
            default_index=["Dashboard", "Projects", "Dataset", "Analytics", "Chatbot", "Logout"].index(
                st.session_state.current_page),
            menu_icon="menu-button-wide",
            icons=["grid", "briefcase", "table", "bar-chart", "chat", "box-arrow-right"], orientation="vertical"
        )


def login():
    with st.form("login_form"):
        st.subheader("Log In")
        username = st.text_input("Enter Your Username").lower().strip()
        password = st.text_input("Enter Your Password", type="password").strip()
        submit = st.form_submit_button("Submit")

        if submit:
            users_df = load_users()
            users_df["username"] = users_df["username"].astype(str).str.lower().str.strip()
            users_df["password"] = users_df["password"].astype(str).str.strip()

            user = users_df[(users_df["username"] == username) & (users_df["password"] == password)]

            if not user.empty:
                st.session_state.authenticated = True
                st.session_state.current_user = username
                st.session_state.current_page = "Dashboard"  

                query_params.update(authenticated="true", current_user=username, page="Dashboard")

                st.success(f"Login successful! Welcome, {username.capitalize()}!")
                st.rerun()
            else:
                st.error("Invalid username or password")


def register():
    with st.form("register_form"):
        st.subheader("📝 Sign-Up")
        new_username = st.text_input("New Username").lower().strip()
        new_password = st.text_input("New Password", type="password").strip()
        submit = st.form_submit_button("Register")

        if submit:
            users_df = load_users()
            if new_username in users_df["username"].astype(str).str.lower().str.strip().values:
                st.error("Username already exists! Choose a different username.")
            elif new_username == "" or new_password == "":
                st.error("All fields are required!")
            else:
                save_user(new_username, new_password)
                st.success("Registration successful! Please log in.")


def export_to_excel(df, filename):
    """Exports the given dataframe to an Excel file."""
    df.to_excel(filename, index=False)


def export_to_pdf(df, filename):
    """Exports the given dataframe to a PDF file."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for column in df.columns:
        pdf.cell(40, 10, column, border=1)
    pdf.ln()

    for _, row in df.iterrows():
        for item in row:
            pdf.cell(40, 10, str(item), border=1)
        pdf.ln()

    pdf.output(filename)


def query_gemini(user_query, df):
    """Send user query along with dataset context to Google Gemini."""
    GOOGLE_API_KEY = st.secrets["apikey"]  
    genai.configure(api_key=apikey)
    model = genai.GenerativeModel("gemini-1.5-flash")
    context = f"Given the dataset: {df.to_dict(orient='records')}, answer: {user_query}"
    response = model.generate_content(context)
    return response.text


def dashboard():
    menu = navigation_menu()

    st.session_state.current_page = menu
    query_params.update(page=menu)

    if menu == "Dashboard":
        st.title(f"Welcome, {st.session_state.current_user.capitalize()}!")
        st.title("Intelligent Customer Segmentation and Predictive Insights for B2C Growth")

    elif menu == "Projects":
        st.title("Projects")
        st.write("Here are your projects.")

    elif menu == "Dataset":

            df1 = pd.read_csv(Mall_Customer_file)
            df2 = pd.read_csv(Customer_file)
            st.write("### Mall Customers Dataset:")
            st.dataframe(df1)  
            st.write("### Customers Dataset:")
            st.dataframe(df2)  



    elif menu == "Analytics":
        st.title("Customer Analytics")
        st.header("Bar graph of Age Groups and Spending Scores")

        df = pd.read_csv(Mall_Customer_file)

        fig = px.bar(df, x="Age", y="Spending Score (1-100)", labels={"Age": "Customer Age", "Spending Score (1-100)": "Spending Score"},
                 title="Age vs Spending Score",
                 color="Spending Score (1-100)",
                 color_continuous_scale="Viridis")

        st.plotly_chart(fig)

        st.header("Bar graph of Gender and Spending Scores")

        fig = px.bar(df, x="Gender", y="Spending Score (1-100)", labels={"Gender": "Gender of Customer", "Spending Score (1-100)": "Spending Score"},
                     title="Age vs Spending Score",
                     color="Spending Score (1-100)")

        st.plotly_chart(fig)

        st.header("Scatter graph of Annual Income and Spending Scores")

        fig = px.scatter(df, x="Annual Income (k$)", y="Spending Score (1-100)", labels={"Annual Income (k$)" : "Annual Income of Customer", "Spending Score (1-100)": "Spending Score"},
                         title = "Annual Income and Spending Scores",
                         color="Annual Income (k$)",
                         color_continuous_scale="Viridis")

        st.plotly_chart(fig)

        st.header("Histogram of Age")

        fig = px.histogram(
            df,
            x="Age", 
            nbins=20,  
            title="Distribution of Customer Ages",
            labels={"Age": "Customer Age"},
        )

        fig.update_traces(
            marker_line_color="black",  
            marker_line_width=1.5  
        )

        st.plotly_chart(fig)



    elif menu == "Chatbot":

        st.title("AI Chatbot (Ask about customer data)")
        selected_file = st.selectbox("Select the Dataset", [Customer_file, Mall_Customer_file])

        user_query = st.text_input("Ask me anything about customer data!")
        if st.button("Ask"):
            if selected_file == Customer_file:
                df1 = pd.read_csv(Customer_file)
                if user_query:
                    answer1 = query_gemini(user_query, df1)
                    st.write("**AI Answer:**", answer1)
                else:
                    st.warning("Please enter a question!")

            elif selected_file == Mall_Customer_file:
                df2 = pd.read_csv(Mall_Customer_file)
                if user_query:
                    answer2 = query_gemini(user_query, df2)
                    st.write("**AI Answer:**", answer2)
                else:
                    st.warning("Please enter a question!")



    elif menu == "Logout":
        st.session_state.authenticated = False
        st.session_state.current_user = ""
        st.session_state.current_page = "Log-in"

        query_params.update(authenticated="false", current_user="", page="Log-in")

        st.success("Logged out successfully!")
        st.rerun()


if st.session_state.authenticated:
    dashboard()
else:
    user_choice = auth_menu()
    st.session_state.current_page = user_choice 
    query_params.update(page=user_choice)  

    if user_choice == "Log-in":
        login()
    elif user_choice == "Sign-Up":
        register()
