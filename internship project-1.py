#NOTE:-  PLEASE REMOVE "#" FROM THE LINES YOU WANT TO RUN


#Performing Analysis of Meteorological Data

#Hypothesis to be tested : The Influence of Global Warming on temperature and humidity.


#Code:------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("weatherHistory.csv")
#print(data.head())
data.isna().sum()
new_data=data[['Formatted Date','Apparent Temperature (C)','Humidity']]
#print(new_data.head())
new_data['Formatted Date']=pd.to_datetime(new_data['Formatted Date'],utc=True)
new_data=new_data.set_index('Formatted Date')
data1=new_data[['Apparent Temperature (C)','Humidity']].resample('M').mean()
#print(data1)
#for all months:---------------------------------------------------
plt.plot(data1['Humidity'],label='Humidity',linestyle='dashed',color='green')
plt.plot(data1['Apparent Temperature (C)'],label='Apparent Temperature',color='red')
plt.title('Humidty vs Temperature(C) (all months)')
plt.xlabel('all months')
plt.legend()

#for may:--------------------------------------------------------------------------
#may=data1[data1.index.month==5]
#plt.plot(may.loc['2006-04-01':'2016-04-01','Apparent Temperature (C)'],marker='o',label='Apparent Temperature (C)')
#plt.plot(may.loc['2006-04-01':'2016-04-01','Humidity'],marker='o',label='Humidity',linestyle='dashed')
#plt.legend()
#plt.xlabel('may month')
#plt.title('humidity vs temperature (may)')
plt.show()

#Conclusion

#As we can analyze there isn’t any change in humidity in past 10 years(2006–2010) for the month of April. where as , temperature increases sharply in 2009 and drops in 2015 for rest of the years there isn’t any sharp change in the temperature.

#I am thankful to mentors at https://internship.suvenconsultants.com for providing awesome problem statements and giving many of us a Coding Internship Experience. Thank you www.suvenconsultants.com
