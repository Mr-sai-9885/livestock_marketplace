import streamlit as st
import random

st.title("🐐 AgriConnect - AI Livestock Marketplace")

# Farmer upload section
st.header("Farmer Uploads Animal Details")
name = st.text_input("Animal Name")
breed = st.selectbox("Breed", ["Goat - Local", "Goat - Boer", "Sheep - Merino", "Sheep - Native"])
weight = st.number_input("Weight (kg)", min_value=10, max_value=200, step=1)
health = st.selectbox("Health Status", ["Healthy", "Minor Issues", "Needs Vet Check"])
photo = st.file_uploader("Upload Animal Photo", type=["jpg", "png"])

if st.button("Get AI Price Suggestion"):
    # Simple mock price logic
    base_price = weight * 200  
    if health == "Minor Issues":
        base_price *= 0.9
    elif health == "Needs Vet Check":
        base_price *= 0.75
    suggested_price = round(base_price + random.randint(-500, 500), 2)

    st.success(f"💰 Suggested Fair Market Price: ₹{suggested_price}")

    st.header("Buyer Confirmation")
    if st.button("Buyer Confirms Purchase"):
        st.success("✅ Purchase Confirmed! Digital Payment Processed.")

        st.header("Transport Booking")
        routes = ["Local Transport - 5km", "Regional Transport - 20km", "Verified Partner - 50km"]
        st.info(f"🚚 Recommended: {random.choice(routes)}")
