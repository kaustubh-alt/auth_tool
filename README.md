# Authentication Tool with Registration, Login, CAPTCHA, and Email Features

## Overview
This project is a comprehensive **authentication tool** built using **Python** and **Django**, designed to provide secure and user-friendly authentication functionalities. It includes user registration and login with **CAPTCHA** integration, email-based account activation, and a "Forgot Password" feature for password recovery.

## Features
- **User Registration & Login**: Users can register and log in securely.
- **CAPTCHA Integration**: Added to prevent automated bots from registering or logging in.
- **Email-Based Account Activation**: Users receive an activation email to verify their accounts.
- **Forgot Password**: Allows users to reset their password through an email-based recovery link.
- **Secure Password Handling**: Passwords are stored using robust hashing mechanisms.
- **Responsive Design**: Ensures a seamless experience across devices.

## Tech Stack
- **Backend**: Python, Django
- **Frontend**: HTML, CSS, Bootstrap (optional)
- **Database**: SQLite (default), can be configured for PostgreSQL or MySQL
- **Additional Libraries**: 
  - `django-simple-captcha` for CAPTCHA functionality
  - `django.core.mail` for email handling

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/username/authentication-tool.git
    cd authentication-tool
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the database**:
    Update `settings.py` to configure your database of choice.

5. **Run migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Start the server**:
    ```bash
    python manage.py runserver
    ```

## Usage
- Navigate to `http://127.0.0.1:8000/register/` to create a new account.
- Log in at `http://127.0.0.1:8000/login/`.
- Use the "Forgot Password" link to reset your password via email.
- An activation email is sent during registration to activate your account.



## Future Enhancements
- Implementing two-factor authentication (2FA).
- Adding social login options (Google, Facebook).
- Enhanced security features such as rate-limiting login attempts.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for new features or improvements.

## Contact
For any inquiries or feedback, reach out via [email@example.com](mailto:ss20if029@gmail.com).
