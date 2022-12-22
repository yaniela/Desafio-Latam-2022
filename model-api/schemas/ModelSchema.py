
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import joblib

class ModelSchema:

    def __init__(self,path:str):
        self.model=joblib.load('models/model_version_1_0_0.joblib')       
       
    def etl_input(self, input:dict, model_categories: list):        
        df = pd.DataFrame(input)
        df['Vlo-O']=df['Vlo-O'].astype(object)
        df['periodo_dia']=df['periodo_dia'].astype(object)
        df['Vlo-O']=df['Vlo-O'].astype(object)
        df['DIANOM']=df['DIANOM'].astype(object)
        df['SIGLADES']=df['SIGLADES'].astype(object)
        df['MES']=df['MES'].astype(object)

        object_cols = [col for col in df.columns if df[col].dtype == "object"]
        # Apply one-hot encoder to each column with categorical data
        transformerVectoriser = ColumnTransformer(transformers=[('Vector Cat',
        OneHotEncoder(handle_unknown='ignore', sparse=False, categories=model_categories), object_cols)])

        #OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
        OH_cols = pd.DataFrame(transformerVectoriser.fit_transform(df[object_cols]))

        # One-hot encoding removed index; put it back
        OH_cols.index = df.index

        # Remove categorical columns (will replace with one-hot encoding)
        num_X = df.drop(object_cols, axis=1)

        # Add one-hot encoded columns to numerical features
        OH_X = pd.concat([num_X, OH_cols], axis=1)

        return OH_X 
        
        
    def predict(self, input: dict, model_categories: list):
        
        df = self.etl_input(input, model_categories)
        df.columns = df.columns.astype(str)
        prediction = self.model.predict_proba(df)[:,1]
        
        return prediction