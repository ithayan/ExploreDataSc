    import pandas as pd 
    import matplotlib
    import matplotlib.pyplot as plt

    apple= pd.read_csv('blackapple.csv')
    samsung = pd.read_csv('samsung_op1.csv')

    merged_df = pd.merge(apple, samsung, on='Date', how='inner', suffixes=('apple_', 'samsung_'))
    merged_df.plot.bar()