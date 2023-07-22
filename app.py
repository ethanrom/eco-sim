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


def tab3():
    st.header("Python Plotly Coding Tutor")

    password_input = st.text_input('Enter Password', type='password')
    if authenticate(password_input):

        # Economy-related example data
        years = np.arange(2010, 2022)
        gdp = [12500, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000]
        unemployment_rate = [8.3, 7.9, 7.2, 6.8, 6.1, 5.6, 5.2, 4.8, 4.3, 4.1, 3.9, 3.7]

        st.subheader("Example: GDP over the Years")
        st.write("Below is a plot showing the GDP growth over the years.")
        
        # Plotting GDP over the years using Plotly
        fig_gdp = go.Figure()
        fig_gdp.add_trace(go.Scatter(x=years, y=gdp, mode='lines+markers', name='GDP'))
        fig_gdp.update_layout(title='GDP Growth Over the Years',
                            xaxis_title='Year',
                            yaxis_title='GDP (Billion USD)')

        # Display Python code and explanation
        st.write("Python code for GDP plot:")
        st.code("""
# Import necessary libraries
import plotly.graph_objects as go
import numpy as np

# Sample data for years and GDP
years = np.arange(2010, 2022)
gdp = [12500, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000]

# Create a Plotly figure object
fig_gdp = go.Figure()

# Add a line plot for GDP data
fig_gdp.add_trace(go.Scatter(x=years, y=gdp, mode='lines+markers', name='GDP'))

# Customize the plot layout
fig_gdp.update_layout(title='GDP Growth Over the Years',
                      xaxis_title='Year',
                      yaxis_title='GDP (Billion USD)')

# Display the plot
st.plotly_chart(fig_gdp)
    """)
        st.write("This code uses the Plotly library to create an interactive line plot showing the GDP growth over the years. First, we import the necessary libraries, including Plotly and NumPy (for generating sample data). Next, we define the data for the years and the corresponding GDP values. We then create a Plotly figure object (`fig_gdp`) and add a line plot to it using the `go.Scatter` function. The plot is customized with a title and axis labels using the `update_layout` method. Finally, we use `st.plotly_chart` to display the plot in the Streamlit app.")

        # Display the plot
        st.plotly_chart(fig_gdp)

        st.subheader("Example: Unemployment Rate over the Years")
        st.write("Below is a plot showing the unemployment rate over the years.")
        
        # Plotting unemployment rate over the years using Plotly
        fig_unemployment = go.Figure()
        fig_unemployment.add_trace(go.Scatter(x=years, y=unemployment_rate, mode='lines+markers', name='Unemployment Rate'))
        fig_unemployment.update_layout(title='Unemployment Rate Over the Years',
                                    xaxis_title='Year',
                                    yaxis_title='Unemployment Rate (%)')

        # Display Python code and explanation
        st.write("Python code for Unemployment Rate plot:")
        st.code("""
# Import necessary libraries
import plotly.graph_objects as go
import numpy as np

# Sample data for years and unemployment rate
years = np.arange(2010, 2022)
unemployment_rate = [8.3, 7.9, 7.2, 6.8, 6.1, 5.6, 5.2, 4.8, 4.3, 4.1, 3.9, 3.7]

# Create a Plotly figure object
fig_unemployment = go.Figure()

# Add a line plot for unemployment rate data
fig_unemployment.add_trace(go.Scatter(x=years, y=unemployment_rate, mode='lines+markers', name='Unemployment Rate'))

# Customize the plot layout
fig_unemployment.update_layout(title='Unemployment Rate Over the Years',
                               xaxis_title='Year',
                               yaxis_title='Unemployment Rate (%)')

# Display the plot
st.plotly_chart(fig_unemployment)
    """)
        st.write("This code uses the Plotly library to create an interactive line plot showing the unemployment rate over the years. Similar to the previous example, we import the necessary libraries and define the data for the years and the corresponding unemployment rate. We then create a Plotly figure object (`fig_unemployment`) and add a line plot to it using the `go.Scatter` function. The plot is customized with a title and axis labels using the `update_layout` method. Finally, we use `st.plotly_chart` to display the plot in the Streamlit app.")

        # Display the plot
        st.plotly_chart(fig_unemployment)

        st.subheader("Try Your Own Plotly Code!")
        st.write("You can type in your Plotly code below and click the 'Run Code' button to see your plot.")
        
        # Code input text area
        code_input = st.text_area("Type your Plotly code here:")

        # Run button
        if st.button("Run Code"):
            try:
                # Execute the user's code
                exec(code_input)
            except Exception as e:
                st.error(f"Error: {e}")

    else:
        # Password is incorrect, show an error message
        st.error('Invalid password. Access denied.')


def tab4():
    st.header("Customizable Plot with Plotly")

    password_input = st.text_input('Enter Password', type='password')
    if authenticate(password_input):

        example_x_values = [2010, 2011, 2012, 2013, 2014, 2015]
        example_y_values = [12500, 13000, 14000, 15000, 16000, 17000]

        st.subheader("Customize Your Plot:")
        col1, col2 = st.columns([1, 2])
        with col1:
            x_axis = st.text_input("Enter X-axis title:", "Years")
            y_axis = st.text_input("Enter Y-axis title:", "GDP")
            chart_type = st.selectbox("Choose Chart Type:", ["Scatter", "Line", "Bar"])
            line_mode = st.selectbox("Choose Line Mode:", ["lines", "lines+markers", "markers"])
            plot_color = st.color_picker("Choose Plot Color:", "#1f77b4")
        with col2:
            x_values = st.text_area("Enter X-axis values (comma-separated):", ", ".join(map(str, example_x_values)))
            y_values = st.text_area("Enter Y-axis values (comma-separated):", ", ".join(map(str, example_y_values)))

        try:
            x_values = [float(x.strip()) for x in x_values.split(",")]
            y_values = [float(y.strip()) for y in y_values.split(",")]
        except ValueError:
            st.error("Invalid input for x or y axis. Please enter valid numeric values.")

        fig_custom = go.Figure()

        if chart_type == "Scatter":
            fig_custom.add_trace(go.Scatter(x=x_values, y=y_values, mode=line_mode, name=y_axis, marker_color=plot_color))
        elif chart_type == "Line":
            fig_custom.add_trace(go.Line(x=x_values, y=y_values, mode=line_mode, name=y_axis, line_color=plot_color))
        elif chart_type == "Bar":
            fig_custom.add_trace(go.Bar(x=x_values, y=y_values, name=y_axis, marker_color=plot_color))

        fig_custom.update_layout(title=f"{y_axis} vs. {x_axis}",
                                xaxis_title=x_axis,
                                yaxis_title=y_axis)

        st.subheader("Customized Plot:")
        st.plotly_chart(fig_custom)

        st.subheader("Python Code to Create the Customized Plot:")
        code = f"""
import plotly.graph_objects as go

x_values = {x_values}
y_values = {y_values}

fig_custom = go.Figure()
"""

        if chart_type == "Scatter":
            code += f"""
fig_custom.add_trace(go.Scatter(x=x_values, y=y_values, mode='{line_mode}', name='{y_axis}', marker_color='{plot_color}'))
"""
        elif chart_type == "Line":
            code += f"""
fig_custom.add_trace(go.Line(x=x_values, y=y_values, mode='{line_mode}', name='{y_axis}', line_color='{plot_color}'))
"""
        elif chart_type == "Bar":
            code += f"""
fig_custom.add_trace(go.Bar(x=x_values, y=y_values, name='{y_axis}', marker_color='{plot_color}'))
"""

        code += f"""
fig_custom.update_layout(title='{y_axis} vs. {x_axis}',
                         xaxis_title='{x_axis}',
                         yaxis_title='{y_axis}')
"""

        st.code(code)

    else:
        # Password is incorrect, show an error message
        st.error('Invalid password. Access denied.')

def main():
    st.set_page_config(page_title="Economic Simulator and Python Coding Tutor", page_icon=":memo:", layout="wide")
    tabs = ["Intro", "Simulate", "Learn", "Customize"]

    with st.sidebar:

        current_tab = option_menu("Select a Tab", tabs, menu_icon="cast")

    tab_functions = {
    "Intro": tab1,
    "Simulate": tab2,
    "Learn": tab3,
    "Customize": tab4,
    }

    if current_tab in tab_functions:
        tab_functions[current_tab]()

if __name__ == "__main__":
    main()
