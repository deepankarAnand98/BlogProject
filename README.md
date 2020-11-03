### Steps 
1. Download the zip file 
2. Unzip the items
3. `cd BlogProject`
4. Crate a pyhton environment using the following command: <br> `python -m venv env`
5. Install required libraries <br> `pip install -r requirements.txt`
6. Initiate Database <br> `flask db init`
7. Create migrations <br> `flask db migrate`
8. Upgrade database <br<> `flask db upgrade`
9. Run Application <br> `flask run`