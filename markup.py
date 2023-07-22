def app_intro():
    return """
    <div style='text-align: left;'>
    <h2 style='text-align: center;'>Economic Simulator and Python Coding Tutor</h2>
    <h3 style='text-align: center;'>Introduction</h3>
            
    <p>This app allows you to run basic economic simulations with values plugged in as Python code snippets.</p>

    <h4>Information:</h4>
    <ul>
        <li><b>Try different simulations:</b> In this demo, you can easily try different simulations by modifying the Python code snippets for monthly individual income and expense.</li>
        <li><b>Calculate Results:</b> You can calculate the number of families living beyond their means, the number of families living paycheck to paycheck, and the average income per year based on the provided Python code snippets.</li>
    </ul>
    </div>          
    """

def how_use_intro():
    return """
    <div style='text-align: left;'>
    <h3 style='text-align: center;'>About this Demo</h3>
    <br>
    <h4>How to Use:</h4>
    <ul>
    <li><b>Testing:</b> To run a simulation, provide the Python code snippets for monthly individual income and expense in the text areas. Select the start month and year, and click the "Run Simulation" button. The app will display the simulation results in charts and provide code snippets for the calculations.</li>
    <li><b>Reverse Simulation:</b> You can perform a reverse simulation by checking the "Perform Reverse Simulation" box. This will allow you to input the desired number of families living beyond their means, number of families living paycheck to paycheck, and average income per year. The app will estimate the corresponding Python code snippets for monthly individual income and expense based on the provided results.</li>
    </ul>
    <br>
    </div>
    """