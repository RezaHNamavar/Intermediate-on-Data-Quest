
# coding: utf-8

# In[1]:


import csv
f = open("guns.csv", "r")
csvreader = csv.reader(f)


# In[2]:


data = list(csvreader)


# In[3]:


print(data[1:6])


# In[4]:


headers = data[0]
cleandata = data[1:]
print(cleandata[0:5])


# In[5]:


years = []
for year in cleandata:
    years.append(year[1]) 
year_counts = {}
for year in years:
    if year in year_counts:
        year_counts[year] = year_counts[year] + 1        
    else:
        year_counts[year] = 1
print(year_counts)


# In[6]:


import datetime
dates = []
for time in cleandata:
    years = int(time[1])
    months = int(time[2])
    days = 1
    times = datetime.datetime(year = years, month = months, day = days)    
    dates.append(times)
print(dates[0:5])        


# In[7]:


date_counts = {}
for date in dates:
    if date in date_counts:
        date_counts[date] = date_counts[date] + 1
    else: 
        date_counts[date] = 1
print(date_counts)


# In[8]:


sex_counts = {}
for sex in cleandata:
    if sex[5] in sex_counts:
        sex_counts[sex[5]] = sex_counts[sex[5]] + 1
    else:
        sex_counts[sex[5]] = 1
race_counts = {}
for race in cleandata:
    if race[7] in race_counts:
        race_counts[race[7]] = race_counts[race[7]] + 1
    else:
        race_counts[race[7]] = 1
print(sex_counts)
print(race_counts)


# We should look at how the data rveals on a population and a percentage basis

# In[9]:


g = open("census.csv", "r")
census = list(csv.reader(g))
print(census)


# In[10]:


mapping = {"Asian/Pacific Islander": 15159516 + 674625, 
           "Black": 40250635,
           "Native American/Native Alaskan": 3739506,
           "Hispanic": 44618105,
           "White": 197318956}
race_per_hundredk = {}
for race in race_counts: 
    race_per_hundredk[race] = race_counts[race] / mapping[race] * 100000
    
print(race_per_hundredk)
    


# In[17]:


intents = []
for inten in data:
    intents.append(inten[3])
races = []
for rac in data:
    races.append(rac[7])
homicide_race_counts = {}
for c, v in enumerate(races):
    i = c
    race = v
    if intents[i] == "Homicide":
        if race in homicide_race_counts:
            homicide_race_counts[race] = homicide_race_counts[race]  + 1
        else:
            homicide_race_counts[race] = 1
for race in homicide_race_counts:
    homicide_race_counts[race] = homicide_race_counts[race] / mapping[race] * 100000
print(homicide_race_counts)
    


# Black homicides are significantly higher than any other group. Why?
