import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

matrix = np.random.rand(5,5)

data=pd.DataFrame(
    {
        'age':[10,20.30,40,50,500]
    }
)

plt.subplot(1, 2, 1)
plt.boxplot(data=data)

plt.subplot(1, 2, 2)
plt.violinplot(data=matrix)

plt.title("HeatMap example")
plt.show()


