import pandas as pd

df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")


df.dropna()
df = df.drop(columns=["customerID"])
df = df.drop(columns=["gender"])
df = df.drop(columns=["SeniorCitizen"])
df = df.drop(columns=["PaperlessBilling"])
df = df.drop(columns=["TotalCharges"])
df = df.drop(columns=["Partner"])
df = df.drop(columns=["Dependents"])
df["ClientesNuevos"] = df["tenure"] < 12
df["GastosClientes"] = pd.cut(
    df["MonthlyCharges"],
    bins=[0,35,70,120],
    labels=["Baja","Media","Alta"]
)

df.to_excel("datoslimpios.xlsx",index=False)