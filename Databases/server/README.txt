Pre-requisites:
- NodeJS and npm installed on your machine: https://nodejs.org/en/

Packages Used:
- express: framework for the backend
- pg: used for connection to the database
- cors: used to bypass CORS policy
- cookie-parser: help with accessing cookies

Instructions to run program:
1. Navigate to server > database > config folder and open password.txt
2. Enter your server username on first line and server password on second line and save file 
3. Open terminal (either in command prompt or VSCode)
4. Navigate via terminal to where you saved the server folder
5. Type "npm install" and click enter
6. Type "npm start" and click enter to start the server
7. Navigate to http://localhost:5000 on web browser
8. To shut down the server press Ctrl+C

Demonstration Video (in case video takes too long to load or doesn't load at all, download locally for playback instead):
https://drive.google.com/file/d/1gBQOpX-bDZAr7MNq5qiYYu76HSRqzGfz/view

Additional Notes:
- All transaction and queries performed during your session are stored in server > database > sql > transaction.sql / queries/sql
- You can restart the database (if permissions are granted) by manually running the create_tables.sql followed with seed.sql files found in server > database > sql directory.
    Use the following commands after SSH into your UH Linux account and logging into postgres:

    set schema 'gam8r0';
    \i ~/<your linux directory to the downloaded sql files>/create_tables.sql
    \i ~/<your linux directory to the downloaded sql files>/seed.sql
 

