import streamlit as st

st.title("AgriAssist - Crop Advisor")

crop = st.text_input("Enter crop name")
if crop:
    crop_seasons = {
        'wheat': 'Rabi',
        'rice': 'Kharif',
        'soybean': 'Kharif',
        'mustard': 'Rabi'
    }
    season = crop_seasons.get(crop.lower(), 'Unknown crop')
    st.success(f"{crop.title()} is typically grown in {season} season.")
