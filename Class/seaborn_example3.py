import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#voilin plot
#kernel density plot
data=pd.DataFrame(
    {
        'age':[10,20.30,40,50,500]
    }
)

sns.violinplot(data=data)


plt.title("bar example")
plt.show()

