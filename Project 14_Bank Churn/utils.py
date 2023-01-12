import pickle,os

folder_path = 'model'


def prediction(RowNumber, CreditScore, Geography, Gender, Age, Tenure,
       Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary):
    
    rf_cls = pickle.load(open(f"{folder_path}/rf_pickle.pkl", "rb"))
    
    pred = rf_cls.predict([[RowNumber, CreditScore, Geography, Gender, Age, Tenure,
       Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary]])
    return pred[0]