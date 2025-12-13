import pandas as pd  # For creating the DataFrame

def find_outliers(dX):
    dX = dX.copy()
    
    dX['mean'] = dX.groupby(['region', 'indicator_id'])['value'].transform('mean')
    dX['std']  = dX.groupby(['region', 'indicator_id'])['value'].transform('std')
    
    dX['z_score'] = (dX['value'] - dX['mean']) / dX['std']
    
    # Identify Outliers (Threshold > 3)
    dX['is_outlier'] = (dX['z_score'].abs() > 3).astype(int)
    
    return dX