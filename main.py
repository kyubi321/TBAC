import pandas as pd


# Load your data
data = pd.read_csv("files/sec_pract.csv", sep=',')
#print(data.head())

# checking for if there is any missing value

#missing_value = data.isnull().sum()
#print(missing_value)

# so we found a row with missing value so we are going to drop it
#data = data.drop(data[data.eq(0).all(1)].index)
# another way to do it
data = data.dropna()
# now we need to select the relevant data for calculation of the trust score

selected_attributes = data[['Att1','Att2','BehInt1','BehInt3','Subj1','Subj2','SelfE2','SelfE3','SelfE4','PVul2','PVul3']]
# now we have to give the attribute weights for indicating the importance of each attributes
attribute_weight ={
    'Att1':0.09,
    'Att2':0.03,
    'BehInt1':0.05,
    'BehInt3':0.06,
    'Subj1':0.08,
    'Subj2':0.07,
    'SelfE2':0.11,
    'SelfE3':0.12,
    'SelfE4':0.2,
    'PVul2':0.09,
    'PVul3':0.1,
}
# now we calculate the trust score
data['trust_score'] = data.apply(lambda row:sum(row[attr]* attribute_weight[attr] for attr in selected_attributes.columns),axis=1)
# now we categorize employees based on trust scores

def categorize_trust(score):
    if score >= 4.6:
        return "High Trust"
    elif score >= 3 and score <4.6:
        return "Medium Trust"
    elif score>=2 and score<3:
        return "Low Trust"
    else:
        return "No trust"
data["trust_level"] = data['trust_score'].apply(categorize_trust)
#print(data)
# now saving this file for training the ml model
#file_path = "files/sec_pract_mod.csv"
#data.to_csv(file_path, index=False)


