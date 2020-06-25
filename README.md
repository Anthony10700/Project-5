# Project-5
## For installation 
* Create a python environment : 
    * pip install virtualenv 
    * virtualenv -p python3 env 
    * activate env
* Install the requirements :
    * pip install -r requirements.txt
* Install mysql server (for now the version is 8.0)
* In main.py set a password to your mysql server
* Lunch api_off_import.py to create your database Openfoodfacts and import all products and categories
* Lunch main.py to run the program and select find a subtitle for you product !!! :)

## Functionality
 - Search for food in the Open Food Facts database.
 
 - If the user enters a character that is not a number, the program must repeat the question to him.
 
 - The search must be done on a MySql base.

## User interaction in the terminal.
 1. What food do you want to replace ?
    - 1.1 Select the category. (Several proposals associated with a number. The user enters the corresponding number and presses input)
    - 1.2 Select the food. (Several proposals associated with a number. The user enters the number corresponding to the chosen food and presses input)
    - 1.3 The program offers a substitute, description, store or purchase (if any) and a link to the Open Food Facts page regarding this food.
    - 1.4 The user then has the ability to record the result in the database.
    - 1.5 The user then has the possibility to restart the program.
    
 2. Find my substituted foods in database saved.
    - 2.1 The user then has the possibility to restart the program.