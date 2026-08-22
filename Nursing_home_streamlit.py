from turtle import color

import streamlit as st
import pandas as pd
from PIL import Image
import awswrangler as wr
import numpy as np
import plotly.express as px


# copy data from S3 bucket to a pandas dataframe using awswrangler

# Define your S3 bucket and file key
bucket_name = "health-care-metrics-oseikwadwo"
file_key1 = "curated/readmission-rates/run-1786969102641-part-r-00000"
file_key2 = "curated/hours-worked-by-nurses/run-1787153841843-part-r-00000"
file_key3 = "curated/healthdeficiencies/run-1787231426599-part-r-00000"


# Construct the S3 URI
s3_uri = f"s3://{bucket_name}/{file_key2}"

# Read the CSV directly into a DataFrame
df1 = pd.read_csv(s3_uri)
df_nurse = pd.read_csv(s3_uri)
df_nurse = pd.DataFrame(df_nurse, columns=['date_month', 'sum(total_hours)'])
df_deficiencies = pd.read_csv(s3_uri)

df_nurse = df_nurse.rename(columns={'sum(total_hours)': 'total_hours'})
df_nurse['date_month'] = pd.to_datetime(df_nurse['date_month'], format='%Y%m')



st.title("Nurse Hours Worked Dashboard")
fig =px.bar(df_nurse, x='date_month', y='total_hours', color='date_month', barmode="group") 
st.plotly_chart(fig)  # Display the Plotly chart in Streamlit

# fig = px.bar(df_deficiencies, x='state', y=['health_deficiency_count', 'fire_deficiency_count'], color='state', barmode="group", title="Total Health Deficiencies by State", labels={'state': 'State', 'total_deficiencies': 'Total Deficiencies'})
# st.plotly_chart(fig)



# visualize the data using Streamlit
# st.title("Healthcare Metrics Dashboard")
# st.subheader("Readmission Rates Over Time")
# st.line_chart(df1, x='city_town', y='average_score')
# st.area_chart(df1, x='city_town', y='average_score')
# st.bar_chart(df1, x='city_town', y='average_score')
# st.scatter_chart(df1, x='city_town', y='average_score')