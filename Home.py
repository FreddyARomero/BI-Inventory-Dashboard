import streamlit as st
import pandas as pd

# Configuración de página con estilo profesional
st.set_page_config(
    page_title="NexLog | Inventory Intelligence for SMEs",
    page_icon="📦",
    layout="wide"
)

# Custom CSS para un look "Enterprise Modern"
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    .hero-text { font-size: 50px; font-weight: 700; color: #ffffff; margin-bottom: 0px; }
    .sub-hero { font-size: 20px; color: #8b949e; margin-bottom: 30px; }
    .highlight { color: #58a6ff; }
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2897/2897832.png", width=80) # Icono representativo
st.sidebar.title("NexLog Intelligence")
st.sidebar.info("Focus: Industrial SMEs (Chemical, Food, Pharma)")

menu = st.sidebar.radio("Product Journey", ["The Problem", "The Solution", "Pilot Simulator (ROI)"])

# ---------- DATA LOADING ----------
# Cargamos tu CSV para usarlo en el simulador
@st.cache_data
def load_data():
    # Asumiendo que el archivo se llama export.csv en el repo
    df = pd.read_csv('2026-05-09T09-42_export.csv')
    return df

df_sim = load_data()

# ---------- CONTENT ----------

if menu == "The Problem":
    st.markdown('<p class="hero-text">The <span class="highlight">SME</span> Inventory Gap</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Why Southern European SMEs are losing the race:
        Manual audits are **expensive, slow, and prone to human error**. While giants invest millions in proprietary sensor grids, SMEs are left with:
        
        * **Phantom Inventory:** Products that exist on paper but not on the shelf.
        * **Cash Flow Drag:** Capital locked in misplaced or damaged stock.
        * **Fulfillment Failure:** Inability to meet demand due to data inaccuracy.
        
        **Our Mission:** Democratize high-precision logistics through an affordable synergy of Sensors, Data Architecture, and AI.
        """)
        st.metric(label="Average Accuracy in Manual Audits", value="< 85%", delta="-15% vs Industry Standard", delta_color="inverse")

if menu == "The Solution":
    st.title("Beyond AI: A Logistics Engine")
    
    tab1, tab2, tab3 = st.tabs(["Data Homogenization", "Hardware Agnostic Grid", "Actionable Outputs"])
    
    with tab1:
        st.subheader("Cleaning the Noise")
        st.write("Our AI doesn't make decisions; it cleans the chaos. It homogenizes disparate sensor data into a single source of truth.")
        st.image("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&q=80&w=1000", caption="From Raw Sensor Data to BI-Ready Tables")

    with tab2:
        st.subheader("Cybersecure Architecture")
        st.write("Built for industrial environments (Food, Pharma, Chemicals) where data integrity and cybersecurity are non-negotiable.")

    with tab3:
        st.subheader("North Star: Order Fulfillment")
        st.write("We pinpoint the **exact position** of defective items or mislabeled tags, allowing a 10x faster manual intervention.")

if menu == "Pilot Simulator (ROI)":
    st.title("Investment Simulator")
    st.markdown("Estimate your savings based on your warehouse scale and sensor precision.")

    # Slider interactivo basado en tus lógicas
    warehouses = st.slider("Number of Warehouses", 1, 10, 1)
    
    # Mostramos datos del CSV según la selección (esto es un ejemplo, puedes filtrar el DF)
    # Aquí podrías usar los datos de tu CSV directamente
    st.dataframe(df_sim, use_container_width=True)

    st.divider()
    
    # KPI Cards
    res = df_sim.iloc[0] # Tomamos la fila A como ejemplo
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Benefit", res['total_benefit'], help="Projected savings in 12 months")
    c2.metric("ROI", res['roi_pct'], delta="High Profitability")
    c3.metric("Payback", res['payback_months'], delta="-2 months vs competitors")

    st.success(f"Targeting **{res['accuracy_pct']}% Order Fulfillment** with this configuration.")
