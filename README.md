# timelog-extract-python-REST-API

Our company has had a 20+ year partnership with a 3rd party vendor that uses a 3rd party project management software. But we are unable to get direct database access to export and analyze time spent on projects by tracking category.

I requested that my account be granted permission to access the platform via the REST API and an API key so that I could write a program that would: 
<br>1 - Authenticate my sessions
<br>2 - Collect time entry values filtered by date range
<br>3 - Convert the dictionary values into a Pandas Dataframe 
<br>4 - Write the data frame to a CSV that could be easily copied into a data warehouse where we could easily run SQL queries and create dashboards/visualizations.
