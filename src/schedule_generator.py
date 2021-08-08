# Schedule Generator

import os
import config
import pandas as pd
import numpy as np
import warnings


# options




# load data
df = pd.read_csv( os.path.join(config.input_dir, 'Arrival_2020-01-01.csv'), index_col = 0)

date_range = pd.date_range('2020-01-01 00:00', '2020-01-02 00:00', freq = '1H')

for i in date_range:
    df['Arrival_SCH']