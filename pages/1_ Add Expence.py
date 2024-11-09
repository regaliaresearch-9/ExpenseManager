import streamlit as st
import sqlite3
import pandas as pd

if 'authentication_status' not in st.session_state or not st.session_state.authentication_status:
    st.info("Please login from the Home page and try again.")
    st.stop()

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('expenses.db')
    return conn


# Function to add an expense
def add_expense(amount, date, description, category,payment_method,payment_src):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO expenses (amount, date, description, category,paymentmethod,paymentsrc) VALUES (?, ?, ?, ?,?,?)",
              (amount, date, description, category,payment_method,payment_src))
    conn.commit()
    conn.close()


# Function to retrieve all expenses
def get_expenses():
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()
    return df


# Streamlit UI
st.title("Daily Expense Manager")



# Input fields for adding an expense
with st.form(key='expense_form'):
    date = st.date_input("Date")
    description = st.text_input("Description","Text")
    amount = st.number_input("Amount (INR)", min_value=0.0)

    category = st.selectbox("Category", ["Gas", "Petrol", "Food", "Bill", "Misc","Shoping"])
    paid_by = ['Cash','CC','Netbanking','UPI']
    paid_from = ['Cash','HDFC','IDBI','ICIC']
    payment_method = st.selectbox("Method", paid_by)
    payment_src = st.selectbox("Source", paid_from)

    submit_button = st.form_submit_button(label='Add Expense')

if submit_button:
        add_expense(amount, date.strftime("%Y-%m-%d"), description, category,payment_method,payment_src)
        st.success("Expense added successfully!")

# Displaying expenses
st.subheader("Expenses")
expenses_df = get_expenses()
st.dataframe(expenses_df)
