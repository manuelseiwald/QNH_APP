import streamlit as st
import requests

def qfe_to_qnh(qfe, temp_c, height_m):
    t_kelvin = temp_c + 273.15
    return qfe * (1 - (0.0065 * height_m) / t_kelvin) ** -5.255

def standard_qfe(height_m, qnh=1013.25):
    temp_kelvin = 288.15
    return qnh * (1 - (0.0065 * height_m) / temp_kelvin) ** 5.255

def get_metar(icao="LOWS"):
    try:
        url = f"https://tgftp.nws.noaa.gov/data/observations/metar/stations/{icao}.TXT"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        lines = response.text.strip().split('\n')
        if len(lines) >= 2:
            timestamp = lines[0]
            metar = lines[1]
            return f"{timestamp}\n{metar}"
        else:
            return "Kein METAR verfügbar."
    except Exception as e:
        return f"Fehler beim Abrufen des METAR: {e}"

# Streamlit App
st.title("QNH-Rechner – Seiwi")

# Höhe
height = st.number_input("Höhe über Meer (m)", min_value=0, max_value=3000, value=550)

# Dynamische Standard-QFE-Info
std_qfe = standard_qfe(height)
st.info(f"Standard-QFE auf {height:.0f} m bei QNH 1013,25 hPa: {std_qfe:.1f} hPa")

# Eingabefelder
qfe = st.number_input("QFE in hPa", min_value=800.0, max_value=1100.0, value=950.0)
temp = st.number_input("Temperatur in °C", min_value=-50.0, max_value=50.0, value=15.0)

if st.button("QNH berechnen"):
    qnh = qfe_to_qnh(qfe, temp, height)
    st.success(f"Berechneter QNH: {qnh:.1f} hPa")

# METAR anzeigen
metar_text = get_metar("LOWS")
st.info(f"**Aktueller METAR für Salzburg (LOWS):**\n\n```\n{metar_text}\n```")