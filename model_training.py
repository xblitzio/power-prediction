import pandas
import sklearn
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

PowerData = pandas.read_csv("/home/ishan/Desktop/Projects/power_predictor/CCPP_data.csv")
PowerData.head(5)

X = PowerData[['AT', 'V', 'AP', 'RH']]
y = PowerData['PE']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
