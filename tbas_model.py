import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# let load the csv file
data = pd.read_csv("files/sec_pract_mod.csv")
# for dropping missing values
data = data.dropna()
# print(data)
# we split the data into x features and y targets
X = data.drop(columns=['trust_score', 'trust_level', 'id','username','password'])
y = data['trust_score']

# now we split our data into training data and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# scale the features
scaler = StandardScaler()
X_train_Scaled = scaler.fit_transform(X_train)
X_test_Scaled = scaler.transform(X_test)

# now we select our model
model = LinearRegression()

# now we train our model
model.fit(X_train_Scaled, y_train)


# now we test the model on the test data
y_predict = model.predict(X_test_Scaled)

# now we compare the accuracy of the model with the test data and predicted data
# mse and r2 score are used to calculate the accuracy.
mse = mean_squared_error(y_test, y_predict)
r2 = r2_score(y_test, y_predict)

# if we get the mse the least value as possible ,then it means that the model,
# The model fits close to the actual value.
# if the r2 value is 0.7 to 1.0 ,then it means the model is highly accurate

print("Mean Squared Error:", mse)
print("r2 score : ", r2)

# now we can check the models prediction with a scenario data
scenario_data = {
    'Att1': [4],'Att2': [4],'BehInt1': [3],'BehInt3': [3],'Subj1': [4],'Subj2': [4],'PVul2': [4],'PVul3': [4],'SelfE2': [5],'SelfE3': [5],'SelfE4': [4]
}
scenario_df = pd.DataFrame(scenario_data)
scenario_scaled = scaler.transform(scenario_df)
predicted_trust_score = model.predict(scenario_scaled)
print("Predicted trust score for the scenario:", predicted_trust_score[0])
