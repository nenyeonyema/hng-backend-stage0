# A Simple Public API for HNG Backend Internship Stage 0

## Project Description
This project is a simple public API built with Python Flask. It returns the following JSON response from the API call:
- My Registered email address
- Current datetime in ISO 8601 format (UTC).
- Github URL of this project codebase.

## API ENDPOINT
### `/GET`
** RESPONSE: **

```json
    {
        "email": "chinenyeonyema1@gmail.com",
        "current_datetime": "2025-01-30T12:42:18.213410Z",
        "github_url": "https://github.com/nenyeonyema/hng-backend-stage0"
    }
```

## Set Up Instructions
1. Clone the repository
`git clone https://github.com/nenyeonyema/hng-backend-stage0`

2. Navigate to the project directory
`cd hng-backend-stage0`

3. Install dependencies
`sudo pip install -r requirements.txt`

4. Run the project locally
`sudo python3 main.py`

5. Access the API endpoint
https://hng-backend-stage0-dun.vercel.app/

** Python Developers **
https://hng.tech/hire/python-developers
