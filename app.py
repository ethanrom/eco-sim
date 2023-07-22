import streamlit as st
import plotly.graph_objects as go
import json
import numpy as np
from streamlit_option_menu import option_menu
from markup import app_intro, how_use_intro

PASSWORD = 'Ethan101'

def authenticate(password):
    return password == PASSWORD

def tab1():
    st.header("Economic Simulator and Python Coding Tutor")  
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("image.jpg", use_column_width=True)
    with col2:
        st.markdown(app_intro(), unsafe_allow_html=True)
    st.markdown(how_use_intro(),unsafe_allow_html=True) 


    github_link = '[<img src="https://badgen.net/badge/icon/github?icon=github&label">](https://github.com/ethanrom)'
    huggingface_link = '[<img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue">](https://huggingface.co/ethanrom)'

    st.write(github_link + '&nbsp;&nbsp;&nbsp;' + huggingface_link, unsafe_allow_html=True)

def simulate_economy(monthly_individual_income, monthly_individual_expense, start_month, start_year, num_months=12):
    income_params = json.loads(monthly_individual_income)
    expense_params = json.loads(monthly_individual_expense)

    # Simulate economic data
    np.random.seed(42)
    monthly_income = np.random.normal(loc=income_params["mean"], scale=income_params["standarddeviation"], size=num_months)
    monthly_income = np.clip(monthly_income, income_params["min"], income_params["max"])
    
    monthly_expense = np.random.normal(loc=expense_params["mean"], scale=expense_params["standarddeviation"], size=num_months)
    monthly_expense = np.clip(monthly_expense, expense_params["min"], expense_params["max"])

    total_income_per_year = np.sum(monthly_income) * 12
    average_income_per_year = np.mean(monthly_income) * 12

    families_beyond_means = np.sum(monthly_income < monthly_expense)
    families_paycheck_to_paycheck = np.sum(monthly_income >= monthly_expense)

    return families_beyond_means, families_paycheck_to_paycheck, average_income_per_year, monthly_income, monthly_expense

def plot_line_chart(data, x_label, y_label, title):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(range(len(data))), y=data, mode='lines', name=title))
    fig.update_layout(title=title, xaxis_title=x_label, yaxis_title=y_label)
    return fig

def tab2():

    password_input = st.text_input('Enter Password', type='password')
    if authenticate(password_input):

        st.header("User Inputs")
        monthly_individual_income = st.text_area("Monthly Individual Income (Python code snippet)", value='''{
        "mean": 4000,
        "min": 1200,
        "max": 15000,
        "standarddeviation": 2000
        }''')
        monthly_individual_expense = st.text_area("Monthly Individual Expense (Python code snippet)", value='''{
        "mean": 4000,
        "min": 1200,
        "max": 15000,
        "standarddeviation": 2000
        }''')
        start_month = st.selectbox("Start Month", ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
        start_year = st.number_input("Start Year", min_value=1900, max_value=2100, value=2021)

        if st.button("Run Simulation"):
            try:
                num_months = 12
                families_beyond_means, families_paycheck_to_paycheck, average_income_per_year, monthly_income, monthly_expense = simulate_economy(monthly_individual_income, monthly_individual_expense, start_month, start_year, num_months)
                st.header("Simulation Results")
                st.write(f"Number of families living beyond their means: {families_beyond_means}")
                st.write(f"Number of families living paycheck to paycheck: {families_paycheck_to_paycheck}")
                st.write(f"Average income per year: ${average_income_per_year:.2f}")

                st.header("Monthly Income and Expense")
                income_chart = plot_line_chart(monthly_income, "Month", "Income", "Monthly Individual Income")
                st.plotly_chart(income_chart)

                expense_chart = plot_line_chart(monthly_expense, "Month", "Expense", "Monthly Individual Expense")
                st.plotly_chart(expense_chart)

                st.header("Code Snippets")
                st.subheader("Calculation of Number of Families living beyond their means")
                st.code("""
import numpy as np

# Assuming monthly_income and monthly_expense are numpy arrays
families_beyond_means = np.sum(monthly_income < monthly_expense)
                """, language="python")

                st.subheader("Calculation of Number of Families living paycheck to paycheck")
                st.code("""
import numpy as np

# Assuming monthly_income and monthly_expense are numpy arrays
families_paycheck_to_paycheck = np.sum(monthly_income >= monthly_expense)
                """, language="python")

                st.subheader("Calculation of Average income per year")
                st.code(f"""
# Assuming monthly_income is a numpy array
average_income_per_year = np.mean(monthly_income) * 12
                """, language="python")
            except Exception as e:
                st.error(f"An error occurred: {e}")

    else:
        # Password is incorrect, show an error message
        st.error('Invalid password. Access denied.')


def main():
    st.set_page_config(page_title="Economic Simulator and Python Coding Tutor", page_icon=":memo:", layout="wide")
    tabs = ["Intro", "Simulate"]

    with st.sidebar:

        current_tab = option_menu("Select a Tab", tabs, menu_icon="cast")

    tab_functions = {
    "Intro": tab1,
    "Simulate": tab2,
    }

    if current_tab in tab_functions:
        tab_functions[current_tab]()

if __name__ == "__main__":
    main()