import pandas as pd

# creating series (one-dimensional array)
simple_series = pd.Series([42, 55, 73], dtype='f8')
# 0     42.0
# 1     55.0
# 2     73.0
# dtype: float64

# creating series with specified index
index_series = pd.Series([42, 55, 73], index=["electron", "proton", "neutron"], dtype='f8')
# electron      42.0
# proton        55.0
# neutron       73.0
# dtype: float64

# accessing value in series
print(index_series["electron"])
# 42.0

# accessing multiple values in series (range)
print(index_series["electron":"neutron"])
# electron      42.0
# proton        55.0
# neutron       73.0
# dtype: float64

# accessing multiple values in series using indexing
print(index_series[1:])
# proton        55.0
# neutron       73.0
# dtype: float64

# creating series from dictionary
dict_series = pd.Series({ "electron": 6, "neutron": 28, "proton": 496, "neutrino": 8128 })
# electron      6
# neutrino      8128
# neutron       28
# proton        496
# dtype: int64

# combining two series into one column
print(index_series + dict_series)
# electron      48.0
# neutrino      NaN
# neutron       101.0
# proton        551.0
# dtype: float64

# combining two series as dataframe
combined_series = pd.DataFrame({ "A": index_series, "B": dict_series })
#               A       B
# electron      42.0    6
# neutrino      NaN     8128
# neutron       73.0    28
# proton        55.0    496

# accessing columns as series
print(combined_series["A"])
# electron      42.0
# neutrino      NaN
# neutron       73.0
# proton        55.0
# Name: A, dtype: float64

# add new row with index
append_series = combined_series._append(pd.DataFrame({ "A": [-8128] }, index=["antineutrino"]))
#               A       B
# electron      42.0    6.0
# neutrino      NaN     8128.0
# neutron       73.0    28.0
# proton        55.0    496.0
# antineutrino  -8128.0 NaN

# drop row
append_series = append_series.drop("neutron")
#               A       B
# electron      42.0    6.0
# neutrino      NaN     8128.0
# proton        55.0    496.0
# antineutrino  -8128.0 NaN

# transpose
print(combined_series.T)
#       electron    neutrino    neutron     proton
# A     42.0        NaN         73.0        55.0
# B     6.0         8128.0      28.0        496.0

# masking
print(combined_series > 120)
#               A       B
# electron      False   False
# neutrino      False   True
# neutron       False   False
# proton        False   True

# add masking as column (e.g. larger than 120)
combined_series["large"] = (combined_series["A"] > 120) | (combined_series["B"] > 120)
#               A       B       large
# electron      42.0    6       False
# neutrino      NaN     8128    True
# neutron       73.0    28      False
# proton        55.0    496     True

# delete a column
del combined_series["large"]
#               A       B
# electron      42.0    6
# neutrino      NaN     8128
# neutron       73.0    28
# proton        55.0    496