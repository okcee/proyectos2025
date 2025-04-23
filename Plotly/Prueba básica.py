import pandas as pd
import numpy as np
import cufflinks as cf
from plotly.offline import init_notebook_mode

init_notebook_mode(connected=True)
cf.go_offline()

df_test = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})
df_test.iplot()