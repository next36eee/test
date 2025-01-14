import streamlit as st
from streamlit_folium import st_folium
import folium

# Apply custom style using HTML and CSS
st.markdown("""
    <style>
        @keyframes blink {
            0% { background-color: #fffaf0; }
            50% { background-color: #ffd1c4; }
            100% { background-color: #fffaf0; }
        }
      .map-container {
            margin-bottom: -10px; /* Reduce space between map and next component */
        }
        sup {
            vertical-align: super;
            font-size: medium;
        }
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
           .card1 {
            background-color: #fffaf0;
            margin-top:5px;
            border: 3px solid #ff7f50;
            border-radius: 15px;
            padding: 20px;
            box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
            font-family: 'Arial', sans-serif;
            color: #444;
            animation: blink 1.5s infinite; /* Add blinking effect */
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
        <div class="title" style="color:black;">🎉 House Warming Ceremony Invitation 🎉</div>
        <div class="subheader" style="color:black;">You're Invited!</div>
    </div>
""", unsafe_allow_html=True)

# Event details
st.markdown("""
    <div class="card">
        <div class="content">
            We are thrilled to invite you to our house warming ceremony to celebrate our new home.  
            Join us for a joyous day filled with love, laughter, and blessings!  
        </div>
    </div>
""", unsafe_allow_html=True)

# Event details card
st.markdown("""
    <div class="card1">
        <div class="content">
            <b>Date</b>: 31st January 2025<br>
            <b>Time</b>: 05:00 AM <br>
             <b>Lunch</b>: 12:00 PM <br>
            <b>Venue</b>:
            7<sup>th</sup> Cdoss, Ravindra Nagar, Tirupati, AP 
        </div>
    </div>
""", unsafe_allow_html=True)

# Adding a map with the location
# st.markdown("""
#     <div class="card">
#         <div class="content">
#             📍 <b>Event Location:</b>
#         </div>
#     </div>
# """, unsafe_allow_html=True)

# location_coords = [13.633796, 79.442083]  # Coordinates for the location
# m = folium.Map(location=location_coords, zoom_start=16)
#
# # Add a marker for the event location
# folium.Marker(location_coords, tooltip="Our New Home").add_to(m)
# st_folium(m, width=None, height=350)

# Display the map
st.markdown("""
    <div style="margin-top:0px !important;padding:0px;align:centre;">
        <iframe src="https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d31019.1499631962!2d79.42148363476564!3d13.633796199999997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zMTPCsDM4JzAxLjciTiA3OcKwMjYnMzEuNSJF!5e0!3m2!1sen!2sin!4v1736684616829!5m2!1sen!2sin" width="400" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
""", unsafe_allow_html=True)

# Button to view location in Google Maps, centered
st.markdown("""
    <div class="center-button" style="margin-top:0px !important;padding:0px;">
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
          <div class="footer">
            With Warm Regards😊,<br>
            Naresh & Jyothsna Family👨‍👩‍👦‍👦,<br>
            PH: 7989767695, 7386986164.
           </div>
    </div>
""", unsafe_allow_html=True)
