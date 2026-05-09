import streamlit as st
import pandas as pd
import io

# 1. Configuración básica
st.set_page_config(page_title="NexLog | SME Intelligence", page_icon="📦", layout="wide")

# 2. Carga de datos con protección
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('2026-05-09T09-42_export.csv')
    except:
        csv_data = """scenario,accuracy_pct,warehouses,total_benefit,total_cost,roi_pct,payback_months,recovered_shrink,audit_savings,error_savings
A,98.62,1,"62805","35000",79.4%,6.7 months,"38929","15572","8305" """
        df = pd.read_csv(io.StringIO(csv_data))
    return df

df = load_data()
res = df.iloc[0]

# 3. Encabezado y Storytelling
st.title("📈 Strategic Impact: Pilot Simulation")
st.subheader("From Operational Chaos to Financial Certainty")

# Usamos triple comilla para permitir saltos de línea y comillas internas
st.markdown("""
### The Challenge
Industrial SMEs in Southern Europe (Pharma, Food, Chemicals) face a **'Competitive Gap'** due to manual, error-prone inventory audits. High-end sensor technology is often unaffordable, leading to **'Phantom Inventory'** and poor cash flow management.

### Our Solution
We developed an accessible, high-precision reconciliation platform to improve **Order Fulfillment** and reduce operational costs—delivering Tier-1 results without the million-euro price tag.

### Engineering Leadership
I engineered a multi-layered system that bridges the gap between hardware and business intelligence:
* **Data Pipeline:** Built a secure architecture to cross-reference disparate sensor data.
* **AI Data Cleaning:** Implemented a layer to homogenize 'noisy' industrial inputs into actionable, clean tables.
* **Financial Modeling:** Designed a simulation tool to visualize **Payback Periods** and **Shrinkage Recovery**, facilitating C-level decision-making in conservative markets.
""")

st.divider()

# 4. KPIs Principales
c1, c2, c3 = st.columns(3)
c1.metric("Total Annual Benefit", "€62,805")
c2.metric("ROI (First Year)", "79.4%")
c3.metric("Payback Period", "6.7 Months")

st.divider()

# 5. Pilares de Valor (Asegúrate de que estas líneas no tengan espacios al inicio)
st.subheader("The Three Pillars of Value")
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown("#### 📦 Recovered Shrink")
    st.write(f"**Impact:** €38,929")
    st.caption("Capital recovered from 'Phantom Inventory' through sensor cross-referencing.")

with col_b:
    st.markdown("#### ⏱️ Audit Efficiency")
    st.write(f"**Impact:** €15,572")
    st.caption("Reduction in manual labor hours by automating the reconciliation process.")

with col_c:
    st.markdown("#### 🎯 Error Reduction")
    st.write(f"**Impact:** €8,305")
    st.caption("Data homogenization eliminating costly shipping and labeling errors.")

st.divider()

# 6. Conclusión Estratégica (Todo en una sola línea para evitar errores de indentación)
text = f"Strategic Insight: With {res['accuracy_pct']}% accuracy, this system reaches Tier-1 standards. Payback: {res['payback_months']}."
st.info(text)
