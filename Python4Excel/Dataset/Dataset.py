import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

techno = pd.read_csv('Python4Excel/Dataset/The Impact of Electronic Gadget Uses with Academic Performance among University Students (Responses) - Form Responses 1.csv')
techno.head()

techno.shape

techno.columns = ['time', 'gender', 'study_year',
                  'department', 'num_of_gadget', 
                  'recent_grade', 'gpa_increase', 
                  'mean_hour', 'purpose']

techno.info()

techno.head()

techno['daily_hour'] = (techno['mean_hour'].str.split('-', expand = True)[0].astype(int) + techno['mean_hour'].str.split('-',expand = True)[1].astype(int))

pd.pivot_table(techno, index = 'gender', columns = 'gpa_increase',
               values = 'daily_hour', aggfunc = 'count').plot(kind = 'barh', figsize = (17,8))
plt.xlabel('Daily average hours spent on gadgets', fontsize = 14, labelpad = 13)
plt.grid()

# Males who spent time on gadgets got increase in gpa, and females were in reverse

purpose_freq = techno['purpose'].str.split(',', expand = True).stack().value_counts()
plt.figure(figsize = (10,10))
plt.pie(purpose_freq, autopct='%.2f', explode = (0.07,0.05,0.05,0.01,0.01,0.01,0.01), labels = purpose_freq.index)

# So most of the survvey participants chose Studies as the reason of using gadgets
# The next position goes to Entertainment.
# Surprisingly, Online class is the choice that have least votes, 
# maybe because students include this when they chose Studies

sns.displot(data = techno, x = 'num_of_gadget', bins  = [0,1,2,3,4,5,6]);

pd.pivot_table(techno, index = 'study_year', columns = 'gender', values = ['daily_hour']).plot(kind = 'bar', figsize = (14,7))
plt.ylabel('Daily hours spent on gadgets')

# So for the first year of study and advanced study years, 
# females tend to spend more time on gadgets while males during 2-4 years

techno[['department', 
        'num_of_gadget']].groupby('department').mean().round().sort_values('num_of_gadget', 
                                                                                         ascending = False)

# Business and technology departments tend to own more gadgets than other department students
techno.groupby('recent_grade').mean().round().plot(kind = 'barh', figsize = (15,5))
plt.grid()

# Those who have more gadgets tend to spent more time on those devices, 
# Also, those people showed lower overall gpa in their studies,
# highest grade holders have average two devices and spent 7 hours a day on screen