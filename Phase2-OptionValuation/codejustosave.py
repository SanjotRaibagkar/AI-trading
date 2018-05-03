#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 17:54:27 2018

@author: sanjotraibagkar
"""

Out[67]: 
Strike Price
8500.0    368775
8550.0         0
8600.0    673725
8650.0         0
8700.0     29700
8750.0         0
8800.0     53850
8850.0         0
Name: CE, dtype: int64
e = c.iloc[:8]['Open Interest']['CE'].cumsum()

e
Out[69]: 
Strike Price
8500.0     368775
8550.0     368775
8600.0    1042500
8650.0    1042500
8700.0    1072200
8750.0    1072200
8800.0    1126050
8850.0    1126050
Name: CE, dtype: int64

e = c.iloc[:8]['Open Interest']['CE'].sum()

e
Out[71]: 1126050

c[8]

Traceback (most recent call last):

  File "<ipython-input-72-432f89af78e9>", line 1, in <module>
    c[8]

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/frame.py", line 1962, in __getitem__
    return self._getitem_multilevel(key)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/frame.py", line 2006, in _getitem_multilevel
    loc = self.columns.get_loc(key)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexes/multi.py", line 1980, in get_loc
    loc = self._get_level_indexer(key, level=0)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexes/multi.py", line 2243, in _get_level_indexer
    loc = level_index.get_loc(key)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexes/base.py", line 2444, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))

  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc (pandas/_libs/index.c:5280)

  File "pandas/_libs/index.pyx", line 154, in pandas._libs.index.IndexEngine.get_loc (pandas/_libs/index.c:5126)

  File "pandas/_libs/hashtable_class_helper.pxi", line 1210, in pandas._libs.hashtable.PyObjectHashTable.get_item (pandas/_libs/hashtable.c:20523)

  File "pandas/_libs/hashtable_class_helper.pxi", line 1218, in pandas._libs.hashtable.PyObjectHashTable.get_item (pandas/_libs/hashtable.c:20477)

KeyError: 8


c.iloc[8]
Out[73]: 
               Option Type
Open Interest  CE             37875
               PE             24300
callsum                           0
putsum                            0
Name: 8900.0, dtype: int64
c.iloc[8]['Open Interest']
Out[74]: 
Option Type
CE    37875
PE    24300
Name: 8900.0, dtype: int64
c.iloc[8]['Option Type']

Traceback (most recent call last):

  File "<ipython-input-75-a55300868ece>", line 1, in <module>
    c.iloc[8]['Option Type']

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/series.py", line 601, in __getitem__
    result = self.index.get_value(self, key)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexes/multi.py", line 835, in get_value
    raise e1

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexes/multi.py", line 819, in get_value
    return self._engine.get_value(s, k)

  File "pandas/_libs/index.pyx", line 98, in pandas._libs.index.IndexEngine.get_value (pandas/_libs/index.c:4404)

  File "pandas/_libs/index.pyx", line 106, in pandas._libs.index.IndexEngine.get_value (pandas/_libs/index.c:4087)

  File "pandas/_libs/index.pyx", line 574, in pandas._libs.index.MultiIndexObjectEngine.get_loc (pandas/_libs/index.c:12643)

  File "pandas/_libs/index.pyx", line 132, in pandas._libs.index.IndexEngine.get_loc (pandas/_libs/index.c:5280)

  File "pandas/_libs/index.pyx", line 154, in pandas._libs.index.IndexEngine.get_loc (pandas/_libs/index.c:5126)

  File "pandas/_libs/hashtable_class_helper.pxi", line 1210, in pandas._libs.hashtable.PyObjectHashTable.get_item (pandas/_libs/hashtable.c:20523)

  File "pandas/_libs/hashtable_class_helper.pxi", line 1218, in pandas._libs.hashtable.PyObjectHashTable.get_item (pandas/_libs/hashtable.c:20477)

KeyError: 'Option Type'


c.iloc[8]['Open Interest']
Out[76]: 
Option Type
CE    37875
PE    24300
Name: 8900.0, dtype: int64
c.iloc[8]['Open Interest']['Option Type']['CE']

Traceback (most recent call last):

  File "<ipython-input-77-4b818fe3349b>", line 1, in <module>
    c.iloc[8]['Open Interest']['Option Type']['CE']

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/series.py", line 601, in __getitem__
    result = self.index.get_value(self, key)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexes/base.py", line 2491, in get_value
    raise e1

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexes/base.py", line 2477, in get_value
    tz=getattr(series.dtype, 'tz', None))

  File "pandas/_libs/index.pyx", line 98, in pandas._libs.index.IndexEngine.get_value (pandas/_libs/index.c:4404)

  File "pandas/_libs/index.pyx", line 106, in pandas._libs.index.IndexEngine.get_value (pandas/_libs/index.c:4087)

  File "pandas/_libs/index.pyx", line 154, in pandas._libs.index.IndexEngine.get_loc (pandas/_libs/index.c:5126)

  File "pandas/_libs/hashtable_class_helper.pxi", line 1210, in pandas._libs.hashtable.PyObjectHashTable.get_item (pandas/_libs/hashtable.c:20523)

  File "pandas/_libs/hashtable_class_helper.pxi", line 1218, in pandas._libs.hashtable.PyObjectHashTable.get_item (pandas/_libs/hashtable.c:20477)

KeyError: 'Option Type'


c.iloc[8]['Open Interest']['CE']
Out[78]: 37875
c.iloc[8]['Open Interest']['callsum']

Traceback (most recent call last):

  File "<ipython-input-79-4a909172b155>", line 1, in <module>
    c.iloc[8]['Open Interest']['callsum']

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/series.py", line 601, in __getitem__
    result = self.index.get_value(self, key)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexes/base.py", line 2491, in get_value
    raise e1

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexes/base.py", line 2477, in get_value
    tz=getattr(series.dtype, 'tz', None))

  File "pandas/_libs/index.pyx", line 98, in pandas._libs.index.IndexEngine.get_value (pandas/_libs/index.c:4404)

  File "pandas/_libs/index.pyx", line 106, in pandas._libs.index.IndexEngine.get_value (pandas/_libs/index.c:4087)

  File "pandas/_libs/index.pyx", line 154, in pandas._libs.index.IndexEngine.get_loc (pandas/_libs/index.c:5126)

  File "pandas/_libs/hashtable_class_helper.pxi", line 1210, in pandas._libs.hashtable.PyObjectHashTable.get_item (pandas/_libs/hashtable.c:20523)

  File "pandas/_libs/hashtable_class_helper.pxi", line 1218, in pandas._libs.hashtable.PyObjectHashTable.get_item (pandas/_libs/hashtable.c:20477)

KeyError: 'callsum'


c
Out[80]: 
             Open Interest          callsum putsum
Option Type             CE       PE               
Strike Price                                      
8500.0              368775   192150       0      0
8550.0                   0        0       0      0
8600.0              673725   152850       0      0
8650.0                   0        0       0      0
8700.0               29700    16725       0      0
8750.0                   0        0       0      0
8800.0               53850    20175       0      0
8850.0                   0        0       0      0
8900.0               37875    24300       0      0
8950.0                   0     1950       0      0
9000.0             2009100  1593525       0      0
9050.0                   0        0       0      0
9100.0                9225   219600       0      0
9150.0                   0        0       0      0
9200.0               69225   223800       0      0
9250.0                   0        0       0      0
9300.0               60975   274800       0      0
9350.0                   0        0       0      0
9400.0              114375   140100       0      0
9450.0                   0        0       0      0
9500.0              711225  1053225       0      0
9550.0                   0        0       0      0
9600.0              127575  1224900       0      0
9650.0                   0      225       0      0
9700.0               83025  1527825       0      0
9750.0                   0       75       0      0
9800.0              105825   862725       0      0
9850.0                   0      150       0      0
9900.0               82875   909375       0      0
9950.0                   0     9975       0      0
                   ...      ...     ...    ...
10750.0             142950   123300       0      0
10800.0            3155100   949950       0      0
10850.0              87375     9450       0      0
10900.0            2589825   704175       0      0
10950.0              77400        0       0      0
11000.0            5683875  1122150       0      0
11050.0              74400        0       0      0
11100.0            1208325   101475       0      0
11150.0              38250        0       0      0
11200.0             961575   235950       0      0
11250.0               8850        0       0      0
11300.0             556800   186000       0      0
11350.0                  0        0       0      0
11400.0             188250    56550       0      0
11450.0                  0        0       0      0
11500.0             946575   654150       0      0
11550.0                  0        0       0      0
11600.0              33375     2475       0      0
11650.0                  0        0       0      0
11700.0               4650     1275       0      0
11750.0                675        0       0      0
11800.0              14850      975       0      0
11850.0                 75        0       0      0
11900.0               5025      975       0      0
11950.0                  0        0       0      0
12000.0             859650  1493775       0      0
12050.0                  0        0       0      0
12100.0              39225    47325       0      0
12150.0                  0        0       0      0
12200.0               2325     1050       0      0

[75 rows x 4 columns]

c.iloc[8]
Out[81]: 
               Option Type
Open Interest  CE             37875
               PE             24300
callsum                           0
putsum                            0
Name: 8900.0, dtype: int64
c.iloc[8]['callsum']
Out[82]: 
Option Type
    0
Name: 8900.0, dtype: int64
c.iloc[8]['callsum'] = e
__main__:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy

c.iloc[8]['callsum'] 
Out[84]: 
Option Type
    0
Name: 8900.0, dtype: int64

e
Out[85]: 1126050

c.iloc[8:'callsum']

Traceback (most recent call last):

  File "<ipython-input-86-5d04e9490268>", line 1, in <module>
    c.iloc[8:'callsum']

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1328, in __getitem__
    return self._getitem_axis(key, axis=0)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1724, in _getitem_axis
    return self._get_slice_axis(key, axis=axis)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1695, in _get_slice_axis
    slice_obj = self._convert_slice_indexer(slice_obj, axis)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 241, in _convert_slice_indexer
    return ax._convert_slice_indexer(key, kind=self.name)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexes/numeric.py", line 299, in _convert_slice_indexer
    kind=kind)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexes/base.py", line 1362, in _convert_slice_indexer
    self._validate_indexer('slice', key.stop, kind),

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexes/base.py", line 3388, in _validate_indexer
    self._invalid_indexer(form, key)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexes/base.py", line 1519, in _invalid_indexer
    kind=type(key)))

TypeError: cannot do slice indexing on <class 'pandas.core.indexes.numeric.Float64Index'> with these indexers [callsum] of <class 'str'>


c.iloc[8:('callsum')]

Traceback (most recent call last):

  File "<ipython-input-87-21cc39132e53>", line 1, in <module>
    c.iloc[8:('callsum')]

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1328, in __getitem__
    return self._getitem_axis(key, axis=0)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1724, in _getitem_axis
    return self._get_slice_axis(key, axis=axis)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1695, in _get_slice_axis
    slice_obj = self._convert_slice_indexer(slice_obj, axis)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 241, in _convert_slice_indexer
    return ax._convert_slice_indexer(key, kind=self.name)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexes/numeric.py", line 299, in _convert_slice_indexer
    kind=kind)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexes/base.py", line 1362, in _convert_slice_indexer
    self._validate_indexer('slice', key.stop, kind),

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexes/base.py", line 3388, in _validate_indexer
    self._invalid_indexer(form, key)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexes/base.py", line 1519, in _invalid_indexer
    kind=type(key)))

TypeError: cannot do slice indexing on <class 'pandas.core.indexes.numeric.Float64Index'> with these indexers [callsum] of <class 'str'>


c.iloc[8:,('callsum')]

Traceback (most recent call last):

  File "<ipython-input-88-2c8d3787ed1b>", line 1, in <module>
    c.iloc[8:,('callsum')]

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1325, in __getitem__
    return self._getitem_tuple(key)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1662, in _getitem_tuple
    self._has_valid_tuple(tup)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 191, in _has_valid_tuple
    "types" % self._valid_types)

ValueError: Location based indexing can only have [integer, integer slice (START point is INCLUDED, END point is EXCLUDED), listlike of integers, boolean array] types


c.iloc[:,(8,'callsum')]

Traceback (most recent call last):

  File "<ipython-input-89-d7aafa261d8a>", line 1, in <module>
    c.iloc[:,(8,'callsum')]

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1325, in __getitem__
    return self._getitem_tuple(key)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1662, in _getitem_tuple
    self._has_valid_tuple(tup)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 189, in _has_valid_tuple
    if not self._has_valid_type(k, i):

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1599, in _has_valid_type
    return self._is_valid_list_like(key, axis)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1648, in _is_valid_list_like
    raise IndexingError('Too many indexers')

IndexingError: Too many indexers


c.iloc[:,(8,4)]

Traceback (most recent call last):

  File "<ipython-input-90-d39a4ef131e1>", line 1, in <module>
    c.iloc[:,(8,4)]

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1325, in __getitem__
    return self._getitem_tuple(key)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1662, in _getitem_tuple
    self._has_valid_tuple(tup)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 189, in _has_valid_tuple
    if not self._has_valid_type(k, i):

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1599, in _has_valid_type
    return self._is_valid_list_like(key, axis)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1648, in _is_valid_list_like
    raise IndexingError('Too many indexers')

IndexingError: Too many indexers


c.iloc[:,(8,2)]

Traceback (most recent call last):

  File "<ipython-input-91-a935b8c51fce>", line 1, in <module>
    c.iloc[:,(8,2)]

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1325, in __getitem__
    return self._getitem_tuple(key)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1662, in _getitem_tuple
    self._has_valid_tuple(tup)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 189, in _has_valid_tuple
    if not self._has_valid_type(k, i):

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1599, in _has_valid_type
    return self._is_valid_list_like(key, axis)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1648, in _is_valid_list_like
    raise IndexingError('Too many indexers')

IndexingError: Too many indexers


c.iloc[:,(8)]

Traceback (most recent call last):

  File "<ipython-input-92-7dbc63816064>", line 1, in <module>
    c.iloc[:,(8)]

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1325, in __getitem__
    return self._getitem_tuple(key)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1662, in _getitem_tuple
    self._has_valid_tuple(tup)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 189, in _has_valid_tuple
    if not self._has_valid_type(k, i):

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1597, in _has_valid_type
    return self._is_valid_integer(key, axis)

  File "/Users/sanjotraibagkar/anaconda/lib/python3.5/site-packages/pandas/core/indexing.py", line 1638, in _is_valid_integer
    raise IndexError("single positional indexer is out-of-bounds")

IndexError: single positional indexer is out-of-bounds


c.iloc[8]
Out[93]: 
               Option Type
Open Interest  CE             37875
               PE             24300
callsum                           0
putsum                            0
Name: 8900.0, dtype: int64
c.iloc[8].cumsum
Out[94]: 
<bound method Series.cumsum of                Option Type
Open Interest  CE             37875
               PE             24300
callsum                           0
putsum                            0
Name: 8900.0, dtype: int64>

c.iloc[8].cumsum = 9

c.iloc[8]
Out[96]: 
               Option Type
Open Interest  CE             37875
               PE             24300
callsum                           0
putsum                            0
Name: 8900.0, dtype: int64
c.iloc[8].cumsum = e

c.iloc[8].cumsum
Out[98]: 
<bound method Series.cumsum of                Option Type
Open Interest  CE             37875
               PE             24300
callsum                           0
putsum                            0
Name: 8900.0, dtype: int64>
