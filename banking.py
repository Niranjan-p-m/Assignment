import pandas as pd
from statistics import *

df= pd.read_csv("H:\\bank\\bank.csv",sep=";")
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 320)
# print(df.columns)
#print(df.head(2))

#Average balance by age
avg_age= df.groupby('age',as_index=False).balance.mean()
print('---------- Average balance by age -------------')
print(avg_age)

#age with highest loans
df_loan=df[df['loan']=='yes']
high_loans= df_loan['age'].value_counts().idxmax()
print('----------- age with highest loans ------------')
print("Age with highest loans = ",high_loans)


# Counts by age group
bins=[0,20,40,60,80]
labels=['<20','20-40','40-60','>60']
df['agegroup']=pd.cut(df['age'],bins=bins,labels=labels)
count_age_group=df['agegroup'].value_counts()
print('---------- Counts by age group ---------------')
print(count_age_group)

#average balance by job category
avg_job= df.groupby('job',as_index=False).balance.mean()
print('------------- average balance by job category -------------')
print(avg_job)

#average balance by job,age category
avg_job_age= df.groupby(['job','age']).balance.mean()
print('----------- average balance by job,age category -------------')
print(avg_job_age)

# which age group has high impact for a campaign
campaign= df.groupby('age',as_index=False).campaign.sum()
campaign_sum=campaign.loc[campaign['campaign'].idxmax()]
print('------------- which age group has high impact for a campaign ------------')
print(campaign_sum['age'])

# which education background id high impact for a campaign
campaign_edu= df.groupby('education',as_index=False).campaign.sum()
campaign=campaign_edu.loc[campaign_edu['campaign'].idxmax()]
print('---------------- which education background id high impact for a campaign -----------------')
print(campaign['education'])