import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


def countplot(dataframe, column, title):
    g = sns.countplot(data=dataframe, y=column, palette="rainbow", order=dataframe[column].value_counts().index);
    g.axes.set_ylim(10)
    g.set_title(title, fontdict={'fontsize': 20, 'verticalalignment': 'bottom'},weight='bold')
    sns.set(rc={"figure.figsize": (8, 5)})
