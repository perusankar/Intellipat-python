import numpy as np
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

matrix = np.random.rand(5,5)

sns.heatmap(matrix,annot=True)


plt.title("HeatMap example")
plt.show()

