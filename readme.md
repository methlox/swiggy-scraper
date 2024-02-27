# Objective

Develop a Python script capable of extracting detailed menu data for a specific restaurant
from Swiggy. The script should utilise Swiggy's API to fetch this information and output the
data in a structured CSV format.

## API Endpoint

https://www.swiggy.com/dapi/menu/pl?page-type=REGULAR_MENU&complete-menu=true&lat=18.56&lng=73.95&restaurantId=<restaurant_id>

# Running the script

- Clone the repository in your local system
- Make sure all the user requirements are met
- Run the script

```bash
    git clone git@github.com:methlox/swiggy-scraper.git
    pip install requests
    pip install pandas
    py .\script.py
```

You'll see a `data.csv` file in your local file system after the script runs succesfully

# User Requirements

### Python Installed:

Ensure that Python is installed on the system. You can download and install Python from the official website: https://www.python.org/

### Package Installation:

Install the required packages (pandas and requests) using the following commands in the terminal or command prompt:

```bash
    pip install pandas
    pip install requests
```

### Internet Connection:

As your script is making API requests using the requests library, an active internet connection is required for the script to communicate with the specified URLs.

### Data for Pandas:

If you are working with data using pandas, ensure that the system has the necessary data files or data sources accessible. If you are reading from external files, make sure the file paths are correct.

### Text Editor or IDE:

You need a text editor or integrated development environment (IDE) to write and run your Python script. Examples include Visual Studio Code, PyCharm, Jupyter Notebook, or even a simple text editor like Notepad.

### Permissions:

Ensure that the user running the Python script has the necessary permissions to install packages and access the required resources.
Operating System Compatibility:

Python, pandas, and requests are compatible with various operating systems (Windows, macOS, Linux). Ensure that your operating system is supported.

### Firewall and Security Settings:

Check firewall and security settings to make sure they allow Python to access the internet and external resources.

### Python Environment Management (Optional):

If you are using virtual environments for Python, make sure to activate the appropriate environment before running the script.
Once these requirements are met, you should be able to run your Python script that utilizes pandas and requests without issues.
