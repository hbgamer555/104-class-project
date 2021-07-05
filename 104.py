import pandas as pd
import statistics
df=pd.read_csv(r"C:\Users\ADMIN\Dropbox\My PC (DESKTOP-QH1TBQA)\Downloads\New folder (5)\Data-visualization-master\csv files\SOCR-HeightWeight.csv")
height=df["Height(Inches)"]
x=statistics.median(height)
print(x)
