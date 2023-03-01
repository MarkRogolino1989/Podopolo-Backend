# Podopolo-Backend

1. Install the dependency libraries
   pip install -r requirements.txt
2. Open the SQL Shell(pssql) and input command:
   CREATE DATABASE Notes;
   CREATE USER postgres WITH PASSWORD postgres;
3. Run the command in windows cmd
   python manage.py migrate
    python manage.py runserver     
 
 Endpoints:
  POST http://localhost:8000/api/auth/login
 log in to an existing user account and receive an access token. 
 
  POST http://localhost:8000/api/auth/register
 create a new user account.
 
  GET http://localhost:8000/api/notes
 get a list of all notes for the authenticated user.
 
  GET http://localhost:8000/api/notes/id/
 get a note by ID for the authenticated user.
 
  POST http://localhost:8000/api/notes
 create a new note for the authenticated user.
  
  PUT http://localhost:8000/api/notes/id/
 update an existing note by ID for the authenticated user.
 
  DELETE http://localhost:8000/api/notes/id/
 delete a note by ID for the authenticated user.
 
  POST http://localhost:8000/api/notes/<int:pk>/share
 share a note with another user for the authenticated user.
 
  POST http://localhost:8000/api/search/
 search for notes based on keywords for the authenticated user.

  
