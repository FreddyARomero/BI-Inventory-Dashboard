import streamlit as st
import pandas as pd
import io

def show_storytelling_section(res):
    st.header("The ROI Story: Why this investment makes sense")
    
    # Hero Section for the Headhunter
    st.markdown(f"""
    ### Bridging the SME Competitive Gap
    This simulation represents a **single warehouse scenario**  where we achieved a 
    **{res['roi_pct']} ROI**. For an SME, this isn't just a dashboard; 
    it's a liquidity engine.
    """)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📦 Recovered Capital")
        st.write(f"**€{res['recovered_shrink']:,.0f}**") [cite: 1]
        st.caption("Previously lost to 'Phantom Inventory' and misplacements.")

    with col2:
        st.subheader("⏱️ Operational Savings")
        st.write(f"**€{res['audit_savings']:,.0f}**") [cite: 1]
        st.caption("Drastic reduction in manual audit labor costs.")

    with col3:
        st.subheader("🎯 Precision Gain")
        st.write(f"**{res['accuracy_pct']}%**") [cite: 1]
        st.caption("Order Fulfillment rate, protecting your B2B reputation.")

    st.info(f"**Strategic Insight:** The system pays for itself in just **{res['payback_months']}**, 
             making it a 'low-risk, high-impact' decision for SME owners in Southern Europe.")
