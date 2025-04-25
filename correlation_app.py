import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("📉 Negative Correlation Risk Diversification Calculator")

st.markdown("""
This app helps you understand the **correlation between two assets** to assess diversification potential.
""")

# User inputs
st.header("Input Returns")
returns1 = st.text_area("Enter returns for Asset A (comma-separated)", "5, 6, 7, 8, 10")
returns2 = st.text_area("Enter returns for Asset B (comma-separated)", "10, 9, 8, 7, 6")

try:
    asset_a = np.array([float(x.strip()) for x in returns1.split(",")])
    asset_b = np.array([float(x.strip()) for x in returns2.split(",")])
    
    if len(asset_a) != len(asset_b):
        st.error("Both return lists must have the same length.")
    else:
        # Correlation calculation
        correlation = np.corrcoef(asset_a, asset_b)[0, 1]
        st.subheader(f"📊 Correlation Coefficient: `{correlation:.2f}`")

        # Interpretation
        if correlation < -0.5:
            st.success("🟢 Strong Negative Correlation – Good for Diversification")
        elif -0.5 <= correlation < 0:
            st.info("🟡 Weak Negative Correlation – Some Diversification Benefit")
        elif 0 <= correlation < 0.5:
            st.warning("🟠 Weak Positive Correlation – Limited Diversification")
        else:
            st.error("🔴 Strong Positive Correlation – Poor Diversification")

        # Scatter plot
        fig, ax = plt.subplots()
        ax.scatter(asset_a, asset_b)
        ax.set_xlabel("Asset A Returns")
        ax.set_ylabel("Asset B Returns")
        ax.set_title("Scatter Plot of Returns")
        st.pyplot(fig)
except:
    st.warning("⚠️ Please enter valid numeric values.")
