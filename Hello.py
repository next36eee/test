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
            background: linear-gradient(rgba(255,255,255,.5), rgba(255,255,255,.5)), url("https://via.placeholder.com/800x200"); /* Replace with your image URL */
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
st_folium(m, width=600, height=300)

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


