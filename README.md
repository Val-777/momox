<div id="top"></div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project contains a small Flask application that connects to a SQLite database file and exposes REST endpoints.

This is a minimal project and does not contain any validation or tests.



### Built With

* [Flask](https://flask.palletsprojects.com/)
* [SQLite](https://www.sqlite.org)
* [SQLAlchemy](https://www.sqlalchemy.org//)
* [poetry](https://python-poetry.org/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->

### Installation

1. Unzip the zip file into a folder
2. Build the docker image
   ```sh
   docker build -t momox:latest .
   ``` 
3. Start the container
   ```sh
   docker run -d -p 5000:5000 momox
   ```
4. Server will be running at `http://127.0.0.1:5000`
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

- `POST` `/shelves`: creates a shelf
  - body:
    no body
- `POST` `/books`: creates a book, `price` and `shelf_id` are optional
  - body: 
    ```json
    {
    "price": 45,
    "name": "War and Peace",
    "shelf_id": 7
    }
    ```
- `GET` `shelf/<id>` & `GET` `book/<id>`: Get book / shelf by ID
- `PATCH` `book/<id>`: Change `name`, `price` and/or `shelf_id` of a book by ID
- `DELETE` `shelf/<id>` & `DELETE` `book/<id>`: Delete book / shelf by ID, deleting a shelf deletes the books it contains



<!-- CONTACT -->
## Contact

Val Melev: val.melev99@gmail.com

<p align="right">(<a href="#top">back to top</a>)</p>
