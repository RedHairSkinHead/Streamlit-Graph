#pip install streamlit
import streamlit as st
import pandas as pd
import numpy as np
# Set the title of your web app
st.title("Streamlit Graph Example")

# Generate some sample data
data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})

# Create a scatter plot
st.write("Scatter Plot")
st.write(data)

st.scatter_chart(data)
