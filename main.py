import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

# File uploader for CSV files
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    # Filtering data
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)

    # Getting unique values from the selected column for filtering
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    # Filter the DataFrame based on user selection
    filtered_df = df[df[selected_column] == selected_value]
    st.write("Filtered Data")
    st.write(filtered_df)

    # Plotting data
    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    # Check if the selected columns are different
    if x_column != y_column:
        if st.button("Generate Plot"):
            # Create a line plot of the filtered DataFrame
            plt.figure(figsize=(10, 5))
            plt.plot(filtered_df[x_column], filtered_df[y_column], marker='o')
            plt.title(f"Plot of {y_column} vs {x_column}")
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.grid()
            st.pyplot(plt)
    else:
        st.warning("Please select different columns for x and y axes.")
else:
    st.write("Waiting on file upload...")
