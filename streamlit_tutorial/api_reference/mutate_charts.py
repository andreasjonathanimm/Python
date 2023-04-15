# Sometimes you display a chart or dataframe and want to modify live as the app runs (for example, in a loop). Depending on what you're looking for, there are 3 different ways to do this:

# 1. Using st.empty to replace a single element.
# 2. Using st.container or st.columns to replace multiple elements.
# 3. Using add_rows to append data to specific types of elements.

import streamlit as st
import pandas as pd
import numpy as np

df1 = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

my_table = st.table(df1)

df2 = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

my_table.add_rows(df2)
# Now the table shown in the Streamlit app contains the data for
# df1 followed by the data for df2.

# Assuming df1 and df2 from the example above still exist...
my_chart = st.line_chart(df1)
my_chart.add_rows(df2)
# Now the chart shown in the Streamlit app contains the data for
# df1 followed by the data for df2.

my_chart = st.vega_lite_chart({
    'mark': 'line',
    'encoding': {'x': 'a', 'y': 'b'},
    'datasets': {
      'some_fancy_name': df1,  # <-- named dataset
     },
    'data': {'name': 'some_fancy_name'},
}),
my_chart.add_rows(some_fancy_name=df2)  # <-- name used as keyword
