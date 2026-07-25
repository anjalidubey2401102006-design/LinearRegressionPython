import kagglehub
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
def download_and_train():
  os.environ["Kaggle_username"]="anjalidubey25"
  os.environ["kaggle_key"]="74a0767a3b0d2afed02473df170c6c02"
  print("Connecting to kaggle and download dataset")
  path1= kagglehub.dataset_download("sharmajicoder/genn-z-college-admission-dataset")
  csv_file=os.path.join(path1,"genz_college_admission_prediction.csv")
  print("Dataset download successfully!")
  print("Dataset location:",csv_file)
  df=pd.read_csv(csv_file)
  print(df.head())
  sns.set_style("whitegrid")
  plt.figure(figsize=(8,5))
  sns.scatterplot(data=df,x="Family_Income",y="SST_Score")
  plt.title("Family Income Vs SAT Score")
  plt.show()
  print("\nFirst five rows of dataset:")
  print(df.head())
  plt.figure(figsize=(6,4))
  sns.heatmap(df.corr(numeric_only=True),annot=True,cmap="coolwarm")
  plt.title("Correlation Heatmap")
  plt.show()
  features=["Age","Family_Income","SAT_Score"]
  X=df[features]
  Y=df["SAT_Score"]
  X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=1)
  model=LinearRegression()
  model.fit(X_train,Y_train)
  y_pred=model.predict(X_test)
  plt.figure(figsize=(8,5))
  sns.scatterplot(X=Y_test,y=y_pred)
  plt.xlabel("Actual SAT Score")
  plt.ylabel("Predicted SAT Score")
  plt.title("Actual Vs Predicted SAT Score")
  plt.plot([Y_test.min(),Y_test.max()],[Y_test.min(),Y_test.max()],color="red")
  plt.show()
  print("\n==========MODEL PERFORMANCE=======")
  print("Mean Saquared Error:",mean_squared_error(Y_test,y_pred))
  print("R2 score:",r2_score(Y_test,y_pred))
  print("===================================================\n")
  print("----------Predict SAT Score----------")
  try:
    age=float(input("Enter Age:"))
    family_income=float(input("Enter Family-Income:"))
    sat_score=float(input("Enter SAT-Score:"))
    user_data=pd.DataFrame([[age,family_income,sat_score]],columns=features)
    prediction=model.predict(user_data)[0]
    prediction=max(0,min(100,prediction,2))
    print(f"\nPredicted Admission chance:{round(prediction*100,2)}%")
  except ValueError:
    print("Please enter valid numerical values")
if __name__=="__main__":
  download_and_train()