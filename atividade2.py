import pandas as pd
temp_max=pd.Series([38,30,40,35,25,26,32])
temp_min=pd.Series([16,13,14,8,9,17,10])
media = sum(temp_max) / len(temp_max)
