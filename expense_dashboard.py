import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

st.set_page_config(page_title="My Finance Dashboard", layout="wide")

def load_initial_data():
    """Initializes the session state with dummy data if it doesn't exist."""
    if 'expenses' not in st.session_state:
        initial_data = {
            "Date": [
                datetime.date(2023, 10, 1), 
                datetime.date(2023, 10, 2), 
                datetime.date(2023, 10, 3), 
                datetime.date(2023, 10, 5)
            ],
            "Item": ["Groceries", "Netflix", "Gas", "Dinner Out"],
            "Category": ["Food", "Entertainment", "Transport", "Food"],
            "Amount": [45.50, 15.00, 40.00, 60.00]
        }
        st.session_state.expenses = pd.DataFrame(initial_data)

load_initial_data()

st.title("Personal Expense Tracker")
st.text("Track your daily spending and analyze your budget.")

st.sidebar.header("Add New Expense")

with st.sidebar.form("expense_form", clear_on_submit=True):
    exp_date = st.date_input("Date", datetime.date.today())
    exp_item = st.text_input("Item Name (e.g., Coffee)")
    exp_category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Utilities", "Shopping", "Rent"])
    exp_amount = st.number_input("Amount ($)", min_value=0.0, format="%.2f")
    
    submitted = st.form_submit_button("Add Expense")
    
    if submitted:
        if exp_item and exp_amount > 0:
            new_expense = pd.DataFrame({
                "Date": [exp_date],
                "Item": [exp_item],
                "Category": [exp_category],
                "Amount": [exp_amount]
            })

            st.session_state.expenses = pd.concat(
                [st.session_state.expenses, new_expense], 
                ignore_index=True
            )
            st.sidebar.success("Added successfully!")
        else:
            st.sidebar.warning("Please enter an item name and amount.")

df = st.session_state.expenses

st.caption("Adjust your monthly budget goal to see how you are doing.")
budget_goal = st.slider("Monthly Budget Goal ($)", 100, 5000, 1000)

total_spent = df["Amount"].sum()
remaining_budget = budget_goal - total_spent

col1, col2, col3 = st.columns(3)
col1.metric("Total Spent", f"${total_spent:.2f}")
col2.metric("Budget Goal", f"${budget_goal}")

col3.metric(
    "Remaining", 
    f"${remaining_budget:.2f}", 
    delta_color="normal" if remaining_budget > 0 else "inverse"
)

st.divider()

c1, c2 = st.columns((2, 1))

with c1:
    st.subheader("Spending Trends")
    if not df.empty:
        daily_spending = df.groupby("Date")["Amount"].sum()
        st.line_chart(daily_spending)
    else:
        st.info("No data to display yet.")

with c2:
    st.subheader("Category Breakdown")
    if not df.empty:
        category_spending = df.groupby("Category")["Amount"].sum()
        fig, ax = plt.subplots()
        fig.patch.set_alpha(0)
        
        ax.pie(
            category_spending, 
            labels=category_spending.index, 
            autopct='%1.1f%%', 
            startangle=90,
            textprops={'color':"white"} if st.get_option("theme.base") == "dark" else None
        )
        ax.axis('equal') 
        st.pyplot(fig)

st.subheader("Recent Transactions")
st.dataframe(df, use_container_width=True)

st.divider()
st.subheader("Import Bank Statement")
uploaded_file = st.file_uploader("Upload CSV file (for demo purposes)", type=["csv"])

if uploaded_file is not None:
    st.write("Filename:", uploaded_file.name)
    try:
        uploaded_df = pd.read_csv(uploaded_file)
        st.write("Preview of uploaded data:")
        st.dataframe(uploaded_df.head())
    except Exception as e:
        st.error(f"Error reading file: {e}")