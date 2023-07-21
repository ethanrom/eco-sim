import streamlit as st
import numpy as np
import plotly.graph_objects as go
from io import StringIO
import sys

def simulate_economy(monthly_income, monthly_expenses, start_month, start_year):
    num_months = len(monthly_income)
    current_month = start_month
    current_year = start_year
    insolvent_count = 0
    insolvent_months = []

    for i in range(num_months):
        income = monthly_income[i]
        expenses = monthly_expenses[i]

        if income < expenses:
            insolvent_count += 1
            insolvent_months.append(f"{current_month} {current_year}")

        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1

    return insolvent_count, insolvent_months

# Function to validate the monthly income inputs
def validate_monthly_income(mean, minimum, maximum, std_deviation):
    if minimum >= maximum:
        st.error("Error: The minimum income should be less than the maximum income.")
        return False
    if mean < minimum or mean > maximum:
        st.error("Error: The mean income should be within the range of minimum and maximum incomes.")
        return False
    return True

# Function to validate the monthly expenses inputs
def validate_monthly_expenses(monthly_expenses):
    if len(monthly_expenses) != 12:
        st.error("Error: Please provide expenses for all 12 months.")
        return False
    return True

# Function to get user inputs for monthly individual expenses
def get_user_expenses_input(start_month, start_year):
    monthly_individual_expenses = []
    for month in range(start_month, start_month + 12):
        monthly_expense = st.number_input(f"{month} {start_year}", value=0)
        monthly_individual_expenses.append(monthly_expense)
    return monthly_individual_expenses

# Set page title and description
st.title("Economic Simulator")
st.markdown(
    "Welcome to the Economic Simulator app! This app allows you to simulate the financial "
    "condition of families over time based on monthly individual income and expenses."
)

# Section: Monthly Individual Income
st.header("Monthly Individual Income")
st.markdown(
    "Enter the parameters for monthly individual income below. The simulator will generate "
    "random income data based on the provided parameters."
)

# Create columns for input fields
col1, col2, col3 = st.columns(3)

with col1:
    mean = st.number_input("Mean", value=4000)
with col2:
    minimum = st.number_input("Minimum", value=1200)
with col3:
    maximum = st.number_input("Maximum", value=15000)

std_deviation = st.number_input("Standard Deviation", value=2000)

# Input validation for monthly individual income
if validate_monthly_income(mean, minimum, maximum, std_deviation):

    # Section: Monthly Individual Expenses
    st.header("Monthly Individual Expenses")
    st.markdown(
        "Enter the monthly individual expenses for each of the next 12 months below. "
        "Start by selecting the start month and year."
    )

    # Create columns for input fields
    start_month = st.select_slider("Start Month", options=list(range(1, 13)), value=1)
    start_year = st.number_input("Start Year", value=2021)

    # Get user inputs for monthly individual expenses
    monthly_individual_expenses = get_user_expenses_input(start_month, start_year)

    # Input validation for monthly individual expenses
    if validate_monthly_expenses(monthly_individual_expenses):

        # Section: Simulation Results
        st.header("Simulation Results")
        st.markdown(
            "Click the 'Run Simulation' button to perform the simulation based on the provided "
            "inputs. The simulator will calculate the number of families living beyond their means."
        )

        # Create a single column for the "Run Simulation" button
        col_simulation = st.columns(1)[0]
        if col_simulation.button("Run Simulation"):
            insolvent_count, insolvent_months = simulate_economy(
                np.random.normal(loc=mean, scale=std_deviation, size=12),
                monthly_individual_expenses,
                start_month,
                start_year
            )

            st.subheader("Families living beyond their means (insolvent)")
            st.write(f"Number of Insolvent Families: {insolvent_count}")
            st.write("Insolvent Months:", ", ".join(insolvent_months))

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=[f"{month} {start_year}" for month in range(start_month, start_month + 12)],
                                     y=monthly_individual_expenses,
                                     mode='lines',
                                     name='Expenses'))
            fig.update_layout(title='Monthly Individual Expenses',
                              xaxis_title='Month',
                              yaxis_title='Expenses')
            st.plotly_chart(fig)

        # Section: Output
        st.header("Output")
        st.markdown(
            "In the following section, you can enter Python code and click 'Run Code' to execute it. "
            "The output will be displayed below."
        )

        # Create columns for the code input and "Run Code" button
        col_code_input, col_run_code = st.columns(2)

        with col_code_input:
            code_input = st.text_area("Enter Python code", value='', height=200)

        with col_run_code:
            if st.button("Run Code"):
                stdout = sys.stdout
                sys.stdout = StringIO()

                try:
                    exec(code_input)
                except Exception as e:
                    st.error(f"Error: {str(e)}")

                output = sys.stdout.getvalue()
                sys.stdout = stdout

                if output:
                    st.code(output)
