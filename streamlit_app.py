import streamlit as st
import openai
import requests

def fetch_travel_suggestions(destination, preferences):
    """Fetch travel suggestions using an external API (placeholder implementation)"""
    search_query = f"best attractions in {destination} for {preferences}"
    # Simulating API call - Replace with an actual API like Google Places
    suggestions = [
        "Famous landmark A",
        "Hidden gem B",
        "Cultural site C",
        "Adventure spot D"
    ]
    return suggestions

def generate_itinerary(destination, days, selected_activities):
    """Generate a structured itinerary based on user-approved activities"""
    itinerary = {}
    for day in range(1, days + 1):
        itinerary[f"Day {day}"] = selected_activities[day % len(selected_activities):][:2]
    return itinerary

def main():
    st.title("AI-Powered Travel Planner")
    st.sidebar.header("User Preferences")
    
    # Collecting user inputs
    destination = st.sidebar.text_input("Enter your destination:")
    days = st.sidebar.number_input("Trip Duration (in days):", min_value=1, max_value=30, step=1)
    budget = st.sidebar.selectbox("Budget Range:", ["Low", "Moderate", "Luxury"])
    preferences = st.sidebar.text_area("Enter your travel preferences (e.g., adventure, culture, relaxation):")
    
    dietary = st.sidebar.selectbox("Any dietary preferences?", ["No Preference", "Vegetarian", "Vegan", "Halal", "Kosher"])
    mobility = st.sidebar.selectbox("Walking Tolerance:", ["Low", "Moderate", "High"])
    accommodation = st.sidebar.selectbox("Accommodation Preference:", ["Luxury", "Budget", "Central Location"])
    
    if st.sidebar.button("Get Activity Suggestions"):
        if destination and preferences:
            suggestions = fetch_travel_suggestions(destination, preferences)
            st.subheader("Recommended Activities - Approve Your Itinerary")
            selected_activities = []
            
            for activity in suggestions:
                if st.checkbox(activity, value=True):
                    selected_activities.append(activity)
            
            if st.button("Generate Final Itinerary") and selected_activities:
                itinerary = generate_itinerary(destination, days, selected_activities)
                st.subheader("Your Personalized Travel Itinerary")
                for day, activities in itinerary.items():
                    st.write(f"### {day}")
                    for activity in activities:
                        st.write(f"- {activity}")
        else:
            st.warning("Please enter both destination and preferences to fetch activity suggestions.")

main()
