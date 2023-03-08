from typing import Union
import pandas as pd, numpy as np

# We think this does not need comments. It is understandable. 

def accuracy(y_hat: pd.Series, y: pd.Series) -> float:
    """
    Function to calculate the accuracy
    """

    """
    The following assert checks if sizes of y_hat and y are equal.
    Students are required to add appropriate assert checks at places to
    ensure that the function does not fail in corner cases.
    """
    assert (y_hat.size == y.size); 
    n=y.size; assert (n!=0); tru=0; 
    
    for i in range(n):
        if(y_hat.iat[i]==y.iat[i]): tru+=1; 
    
    return (tru/n); 


def precision(y_hat: pd.Series, y: pd.Series, claass: Union[int, str]) -> float:
    """
    Function to calculate the precision
    """
    assert (y_hat.size==y.size); 
    n=y_hat.size; assert (n!=0); 

    TP=0; TP_FP=0; 
    for i in range(n):
        if(y_hat.iat[i]==claass):
            TP_FP+=1; 
            if(y_hat.iat[i]==y.iat[i]): TP+=1; 
    
    if(TP_FP==0): return 0
    return (TP/TP_FP); 


def recall(y_hat: pd.Series, y: pd.Series, claass: Union[int, str]) -> float:
    """
    Function to calculate the recall
    """
    assert (y_hat.size==y.size); 
    n=y_hat.size; assert (n!=0); 

    TP=0; TP_TN=0; 
    for i in range(n):
        if(y.iat[i]==claass):
            TP_TN+=1; 
            if(y_hat.iat[i]==y.iat[i]): TP+=1; 
    
    return (TP/TP_TN); 


def rmse(y_hat: pd.Series, y: pd.Series) -> float:
    """
    Function to calculate the root-mean-squared-error(rmse)
    """
    assert (y_hat.size==y.size); assert (y_hat.size!=0); 
    return np.sqrt(np.mean((y_hat-y)**2)); 


def mae(y_hat: pd.Series, y: pd.Series) -> float:
    """
    Function to calculate the mean-absolute-error(mae)
    """
    assert (y_hat.size==y.size); assert (y_hat.size!=0); 
    return np.mean(abs(y_hat-y)); 
