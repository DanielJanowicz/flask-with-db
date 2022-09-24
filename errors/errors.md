# Errors relating to displaying data from db

I was able to sucessfully create and connect the database; however, I ran into an issue when running the flask application.   The database was connecting because it was printing the column names, however it wasn't displaying the data within the rows.  

![Index html](\errors\NoDataDisplayed1.png)
- This image was taken from index.html, where I tried to change the actual display of the data according to this [resource](https://stackoverflow.com/questions/39816944/cannot-get-html-to-display-sqlite3-data-with-python-flask)
- This was one way of trying to testing if this error could be fixed.

![Patients html](\errors\NoDataDisplayed2.png)
- This image was taken from patients.html, where I left everything the same from the 504 example from github, with the addition of new column names that were added.  

![Terminal Error](\errors\NDDTerminal.png)
- This image was taken from the terminal when running local host and connecting to the page.  This could be useful for deciphering the problem.