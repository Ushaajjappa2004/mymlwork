from sklearn.linear_model import LinearRegression
import pandas as pd
data={"hours":[2,4,6,8],"marks":[35,45,55,90]}
df=pd.DataFrame(data)
X=df[["hours"]]
y=df["marks"]
model=LinearRegression()
model.fit(X,y)
prediction=model.predict([[2]])
print("predicted_marks",prediction)

