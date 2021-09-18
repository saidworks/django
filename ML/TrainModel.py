# Import all dependencies
import joblib
import numpy as np
import pandas as pd
# import seaborn as sns
from scipy import constants
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Load dataset
df = pd.read_csv("weight-height.csv")
df.head()

df['Weight'] = np.around(df['Weight'] * constants.pound, 1)
df['Height'] = np.around(df['Height'] * constants.inch * 100)
df['Height'] = df['Height'].astype(np.int64, errors='ignore') 
df.head()

df['Gender'].value_counts()

# sns.scatterplot('Height','Weight',data=df,hue='Gender')

df.Gender = df.Gender.map({"Male" : 0, "Female" : 1})
df.sample(n=10)

X = df[ ["Gender", "Height"] ]
y = df[ ["Weight"] ]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

lin_reg.score(X_test, y_test)

np.round(lin_reg.predict([[0, 180]])[0][0],1)

# Save the model
joblib_file = "WeightPredictionLinRegModel.joblib"
joblib.dump(lin_reg, joblib_file) 