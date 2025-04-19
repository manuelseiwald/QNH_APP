import streamlit as st

def qfe_to_qnh(qfe, temp_c, height_m=550):
    t_kelvin = temp_c + 273.15
    return qfe * (1 - (0.0065 * height_m) / t_kelvin) ** -5.255

st.title("QNH-Rechner – Großgmain (550 m Höhe)")

st.write("Gib den aktuellen QFE (Barometerwert) und die Temperatur ein, um den QNH zu berechnen.")

qfe = st.number_input("QFE in hPa", min_value=800.0, max_value=1100.0, value=950.0)
temp = st.number_input("Temperatur in °C", min_value=-50.0, max_value=50.0, value=15.0)

if st.button("QNH berechnen"):
    qnh = qfe_to_qnh(qfe, temp)
    st.success(f"Berechneter QNH: {qnh:.1f} hPa")