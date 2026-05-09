import streamlit as st
import pandas as pd
import io

# ---------- DATA LOADING ESTRATÉGICO ----------

@st.cache_data
def load_data():
    filename = '2026-05-09T09-42_export.csv'
    try:
        # Intenta cargar desde el archivo físico en GitHub
        df = pd.read_csv(filename)
    except FileNotFoundError:
        # FALLBACK: Si el archivo no está, cargamos los datos que proporcionaste
        # Esto garantiza que el Headhunter SIEMPRE vea contenido.
        csv_data = """scenario,accuracy_pct,warehouses,total_benefit,total_cost,roi_pct,payback_months,recovered_shrink,audit_savings,error_savings
A,98.62,1,"€62,805","€35,000",79.4%,6.7 months,"€38,929","€15,572","€8,305" """
        df = pd.read_csv(io.StringIO(csv_data))
    
    # Limpieza de datos (Data Engineering básico)
    # Quitamos '€', '%' y comas para poder operar numéricamente
    for col in ['total_benefit', 'total_cost', 'recovered_shrink', 'audit_savings', 'error_savings']:
        df[col] = df[col].replace(r'[€,]', '', regex=True).astype(float)
    
    return df

# Ejecutar carga
df_sim = load_data()

# ---------- UI LOGIC (PILOT SIMULATOR) ----------

# Supongamos que estamos en la pestaña del simulador
st.title("Investment Simulator")

# Extraemos la fila del escenario A (según tu archivo) 
res = df_sim.iloc[0]

c1, c2, c3 = st.columns(3)

# Mostramos métricas con formato moneda
c1.metric("Total Benefit", f"€{res['total_benefit']:,.0f}", 
          help="Annual projected savings")
c2.metric("ROI", f"{res['roi_pct']}", 
          delta="High Profitability")
c3.metric("Payback", res['payback_months'], 
          delta="< 1 Year")

st.divider()

# Sección de desglose de valor (Storytelling de PM)
col_left, col_right = st.columns(2)

with col_left:
    st.write("### Value Breakdown")
    st.write(f"**Recovered Shrink:** €{res['recovered_shrink']:,.0f}")
    st.write(f"**Audit Savings:** €{res['audit_savings']:,.0f}")
    st.write(f"**Error Reduction:** €{res['error_savings']:,.0f}")

with col_right:
    # Mostramos el impacto en la métrica reina
    st.info(f"Target Accuracy: **{res['accuracy_pct']}%**")
    st.write("By crossing sensor data with AI cleaning, we reach precision levels previously reserved for Tier 1 enterprises.")
