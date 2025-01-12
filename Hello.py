import streamlit as st
from streamlit_folium import st_folium
import folium

# Apply custom style using HTML and CSS
st.markdown("""
    <style>
        .card {
            background-color: #fffaf0;
            margin-top:5px;
            border: 3px solid #ff7f50;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
            font-family: 'Arial', sans-serif;
            color: #444;
        }
        .title-card {
            background: linear-gradient(rgba(255,255,255,.5), rgba(255,255,255,.5)), url("data:image/jpeg;base64,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"); /* Replace with your image URL */
            background-size: cover;
            background-position: center;
            border-radius: 15px;
            color: white;
            padding: 40px 20px;
            text-align: center;
            box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.3);
        }
        .title {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .subheader {
            font-size: 20px;
            margin-bottom: 0;
        }
        .content {
            font-size: 16px;
            line-height: 1.6;
            text-align: center;
        }
        .footer {
            font-size: 16px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
        .center-button {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and header with background image
st.markdown("""
    <div class="title-card">
        <div class="title" style="color:black;">🎉 Housewarming Ceremony Invitation 🎉</div>
        <div class="subheader" style="color:black;">You're Invited!</div>
    </div>
""", unsafe_allow_html=True)

# Event details
st.markdown("""
    <div class="card">
        <div class="content">
            We are thrilled to invite you to our housewarming ceremony to celebrate our new home.  
            Join us for a joyous day filled with love, laughter, and blessings!  
        </div>
    </div>
""", unsafe_allow_html=True)

# Event details card
st.markdown("""
    <div class="card">
        <div class="content">
            <b>Date</b>: 31st January 2025<br>
            <b>Time</b>: 05:00 AM onwards<br>
            <b>Venue</b>:<br>
            Tirupati, AP 
        </div>
    </div>
""", unsafe_allow_html=True)

# Adding a map with the location
st.markdown("""
    <div class="card">
        <div class="content">
            📍 <b>Event Location:</b>
        </div>
    </div>
""", unsafe_allow_html=True)

location_coords = [13.633796, 79.442083]  # Coordinates for the location
m = folium.Map(location=location_coords, zoom_start=15)

# Add a marker for the event location
folium.Marker(location_coords, tooltip="Our New Home").add_to(m)

# Display the map
st_folium(m, width=700, height=400)

# Button to view location in Google Maps, centered
st.markdown("""
    <div class="center-button" style="margin-top:0px;">
        <a href="https://www.google.com/maps?q=13.633796,79.442083" target="_blank">
            <button style="padding: 10px 20px; background-color: #ff7f50; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;">
                View Location in Google Maps
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

# Closing statement
st.markdown("""
    <div class="card">
        <div class="content">
            We look forward to seeing you there! 😊<br>
            For any queries, feel free to contact us at: <b>+91-7386986164</b>
        </div>
        <div class="footer">
            With Warm Regards,<br>
            Naresh & Jyothsna Family👨‍👩‍👦‍👦
        </div>
    </div>
""", unsafe_allow_html=True)


