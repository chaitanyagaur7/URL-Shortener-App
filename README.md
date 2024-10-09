# URL Shortener App

This is a simple URL shortener web application built using Flask and SQLite. The app allows users to shorten long URLs into short, easy-to-remember links, and then redirects users from the short URL back to the original long URL.

## Features

- Shortens long URLs to custom 6-character short URLs.
- Redirects users from short URLs to the original long URLs.
- Uses SQLite as the database to store URL mappings.
- Simple and intuitive user interface.

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy

## Installation

1. Clone this repository:

```bash
git clone https://github.com/chaitanyagaur7/URL-Shortener-App.git
cd URL-Shortener-App
```
2. Create a virtual environment (optional but recommended):

  ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required dependencies:

  ```bash
   pip install -r requirements.txt
  ```

4. Set up the database: 
```bash
python app.py
```

## Usage 

Run the Flask development server:

```bash
   python app.py
```

Open your browser and go to http://127.0.0.1:5000/.

Enter a long URL in the input field and get a shortened version.

Use the generated short URL to be redirected to the original long URL.

## File Structure 

``` graphql
.
├── app.py                # Main application file
├── models.py             # Database model for URL mappings
├── templates/            # HTML templates
│   └── index.html        # Homepage template
├── url_shortener.db      # SQLite database file (auto-created)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Files

- app.py: Contains the Flask application logic, including routes for shortening URLs and redirecting from short URLs to long URLs.

- models.py: Defines the database model URLMapping, which stores long and short URLs.

- index.html: The homepage where users can input long URLs and receive short URLs.

## Database Schema

URLMapping:
 - id: Integer, primary key.
   
 - long_url: String (512), the original long URL.
   
 - short_url: String (6), the generated short URL.




