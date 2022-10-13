#I do not have permission to access a pm tool database, but I do have a restfulAPI credential,
# so I'm trying to extract the data from the database via restful API and then import it into a local DB so I can run SQL queries on it.#


import pandas as pd
import datetime
from redminelib import Redmine
from IPython.display import display

#redmine API to give access to data #https://www.redmine.org/projects/redmine/wiki/Rest_api
redmine = Redmine('https://redmine.altimawebsystems.com/', key="hidden")

#time entry values filtered by date range - https://python-redmine.com/index.html - https://python-redmine.com/resources/time_entry.html
entries = redmine.time_entry.filter(from_date=datetime.date(2022,8,29), to_date=datetime.date(2022,10,1), limit=300).values()


#convert dictionary to pandas dataframe - https://stackoverflow.com/questions/64188284/how-to-convert-a-nested-dict-to-a-pandas-dataframe
df=pd.json_normalize(entries).sort_values(by='spent_on', ascending= True)

display(df)

#write df to csv
df.to_csv('sept-time_entry.csv')

#print dataframe summary
df.info(memory_usage="deep")



