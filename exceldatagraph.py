import pandas as pd
import matplotlib.pyplot as plot

data= pd.read_excel("Salesdata.xlsx");
df= pd.DataFrame(data)

#plot.plot(df['Name'],df['Amount'])
#df.plot(x='Name',y='Amount')
plot.pie(df['Amount'],labels=df['Name'])
plot.show()