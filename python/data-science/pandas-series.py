import pandas as pd

# creating series (one-dimensional array)
simple_series = pd.Series([42, 55, 73], dtype='f8')
simple_series
# 0     42.0
# 1     55.0
# 2     73.0
# dtype: float64

# creating series with specified index
index_series = pd.Series([42, 55, 73], index=["electron", "proton", "neutron"], dtype='f8')
index_series
# electron      42.0
# proton        55.0
# neutron       73.0
# dtype: float64

# accessing value in series
index_series['electron']
# 42.0

# accessing multiple values in series (range)
index_series['electron':'neutron']
# electron      42.0
# proton        55.0
# neutron       73.0
# dtype: float64

# accessing multiple values in series using indexing
index_series[1:]
# proton        55.0
# neutron       73.0
# dtype: float64

# creating series from dictionary
dict_series = pd.Series({'electron': 6, 'neutron': 28, 'proton': 496, 'neutrino': 8128})
dict_series
# electron      6
# neutrino      8128
# neutron       28
# proton        496
# dtype: int64

# combining two series into one column
index_series + dict_series
# electron      48.0
# neutrino      NaN
# neutron       101.0
# proton        551.0
# dtype: float64

# combining two series as dataframe
combined_series = pd.DataFrame({'A': index_series, 'B': dict_series})
combined_series
#               A       B
# electron      42.0    6
# neutrino      NaN     8128
# neutron       73.0    28
# proton        55.0    496

# accessing columns (as series)
combined_series['A']
# electron      42.0
# neutrino      NaN
# neutron       73.0
# proton        55.0
# Name: A, dtype: float64

# add new row with index
append_series = combined_series.append(pd.DataFrame({'A': [-8128]}, index=['antineutrino']))
append_series
#               A       B
# electron      42.0    6.0
# neutrino      NaN     8128.0
# neutron       73.0    28.0
# proton        55.0    496.0
# antineutrino  -8128.0 NaN

# drop row
append_series = append_series.drop('neutron')
append_series
#               A       B
# electron      42.0    6.0
# neutrino      NaN     8128.0
# proton        55.0    496.0
# antineutrino  -8128.0 NaN

# transpose
combined_series.T
#       electron    neutrino    neutron     proton
# A     42.0        NaN         73.0        55.0
# B     6.0         8128.0      28.0        496.0

# masking
combined_series > 120
#               A       B
# electron      False   False
# neutrino      False   True
# neutron       False   False
# proton        False   True

# add masking as column (e.g. larger than 120)
combined_series['large'] = (combined_series['A'] > 120) | (combined_series['B'] > 120)
combined_series
#               A       B       large
# electron      42.0    6       False
# neutrino      NaN     8128    True
# neutron       73.0    28      False
# proton        55.0    496     True

# delete a column
del combined_series['large']
combined_series
#               A       B
# electron      42.0    6
# neutrino      NaN     8128
# neutron       73.0    28
# proton        55.0    496