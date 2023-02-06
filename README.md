# ROBOT FRAMEWORK WITH SELENIUM AND PYTHON FOR AIRBNB

This is robot framework sample project with selenium and python. The goals of this project are:
1. Create a test scenario with robot framework, selenium and python
2. Enable CICD with `github actions` to run the test

### Prerequisite
Make sure you have installed these on your local machine :
* Python
* Pip
* Chrome

### Project Structure
This is my own code base, inspired by common code base on my golang and nodejs projects with clean architecture.
    .
    ├── requirements.txt        # File that contains all python libraries that we used in this project
    ├── Main.py                 # All configurations for this test project should define here 
    ├── helpers                 # Contains any helper function that we use within this project. eg: `discord`
    │   ├── Elements.py         # I used this helper to store functions that help me working with elements here
    │   └── ....                
    ├── test-cases              # This is where your store all of your test
    │   ├── SomeTest.robot       
    │   └── ....                 
    ├── modules                 # You can group your module inside this dir
    │   ├── SomeModule          # each module can usually come with 3 main files (custom your own)
    │   │   ├── Keywords.robot  # Define the keywords, it will be used on your test file
    │   │   ├── Constants.py    # Store element_id, xpath or any variables for your test 
    │   │   ├── Usecases.py     # I used this file to store business layer (custom your own)
    │   │   └── ....  
    │   └── ....                   
    ├── .github                 # This is the devops part. [Github Actions](https://docs.github.com/en/actions) `src`
    │   ├── workflows           
    │   │   ├── script.yml     
    │   └── ....            
    └── ....

### Usage

1. Install dependencies
    ```
    pip install -r requirements.txt
    ``` 
2. Running test scenario
    Run all test cases on dir `./test-cases`
    ```
    python -m robot test-cases
    ```
    Run specific test-case
    ```
    python -m robot test-cases/SomeTest.robot
    ```

Copyright (c) Lukman Hardian
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by:

* [Lukman Hardian](https://www.linkedin.com/in/lukman-h-b15659123/)