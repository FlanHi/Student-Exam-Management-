# Student Exam Management

This project is meant to help a teacher manage his or her classroom better. Rather than record students' exam results on pieces of paper every time, the project seeks to automate this task for the teacher.

### Table Of Contents

- [Technologies Used](#technologies-used)
- [Demo](#demo)
- [Testing The Application Locally](#testing-the-application-locally)


## Technologies Used

- Flask microframework
- Python for programming
- HTML for data presentation on a browser
- Bootstrap for styling and responosiveness


## Demo

- Website design: 
- See the live app: [Live app]()


## Testing The Application Locally

- Clone this repository:

    ```python
    $ git clone git@github.com:FlanHi/Student-Exam-Management-.git
    ```

- Change directory to the cloned folder:

    ```python
    $ cd Student-Exam-Management-
    ```

- Activate your virtual environment:

    ```python
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```

- Install project dependancies:

    ```python
    (venv)$ pip3 install -r requirements.txt
    ```

- Start the flask server:

    ```python
    (venv)$ flask run
    ```

- See the application on our browser:
    - Paste http://127.0.0.1:5000 on your favourite browser


# STUDENT EXAM MANAGEMENT 

| Prototype | Database Design | Live link |
| --------- | --------------- | --------- |
|  [Figma]( https://www.figma.com/proto/ssYZL3bmdSY5Fwi3stWqXx/Student-exam-management-app?type=design&node-id=4-2&t=WxoCtQW1dlOr3iDC-1&scaling=min-zoom&page-id=0%3A1&mode=design )|     [DrawSQL](https://drawsql.app/teams/dylans-useless-team/diagrams/studentexammanagement) | [Render]()|

## Roles

### Dylan:

- Create templates
    - Landing page
    - Register Page
    - Login page
    - Exam results

- Create Database
    - User
    - Exam

- Handling errors
    - 404 page
    - 500 page

### Harrison:

- Create Auhentication
    - Can register
    - Can login
    - Can reset password