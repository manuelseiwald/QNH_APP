import streamlit as st

def qfe_to_qnh(qfe, temp_c, height_m):
    t_kelvin = temp_c + 273.15
    return qfe * (1 - (0.0065 * height_m) / t_kelvin) ** -5.255

def standard_qfe(height_m, qnh=1013.25):
    # Druckabnahme nach ICAO Standardatmosphäre
    temp_kelvin = 288.15  # Standardtemperatur auf Meereshöhe
    return qnh / (1 - (0.0065 * height_m) / temp_kelvin) ** 5.255

st.title("QNH-Rechner – Großgmain")

st.write("Berechnet den QNH aus QFE und Temperatur auf Ortshöhe. Zeigt auch den theoretischen Standard-QFE.")

# Eingabehöhe
height = st.number_input("Höhe über Meer (m)", min_value=0, max_value=3000, value=550)

# Eingabefelder
qfe = st.number_input("QFE in hPa", min_value=800.0, max_value=1100.0, value=950.0)
temp = st.number_input("Temperatur in °C", min_value=-50.0, max_value=50.0, value=15.0)

if st.button("QNH berechnen"):
    qnh = qfe_to_qnh(qfe, temp, height)
    st.success(f"Berechneter QNH: {qnh:.1f} hPa")

# Standard-QFE anzeigen
std_qfe = standard_qfe(height)
st.info(f"Standard-QFE auf {height:.0f} m bei QNH 1013,25 hPa: {std_qfe:.1f} hPa")