# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 17:02:35 2021

@author: Vadim Azhmyakov
"""

import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)