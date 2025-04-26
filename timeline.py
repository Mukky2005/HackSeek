import streamlit as st
import pandas as pd
from datetime import datetime
from auth_utils import get_user_search_history, get_user_saved_solutions

def format_datetime(dt_str):
    """Format datetime string to a more readable format"""
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S.%f")
    return dt.strftime("%b %d, %Y at %I:%M %p")

def render_timeline():
    """Render the user's timeline of searches and solutions"""
    if not st.session_state.get('is_authenticated', False):
        st.warning("Please log in to view your timeline.")
        return
    
    st.title("Your HACKSEEK Timeline")
    
    # Get user's search history
    user_id = st.session_state.user_info['id']
    searches = get_user_search_history(user_id)
    
    if not searches:
        st.info("You haven't made any searches yet. Start by analyzing a problem in the main app!")
        return
    
    # Display search history - simplified view with only previous searches
    st.subheader("Your Previous Searches")
    
    # Create a cleaner list of past searches
    for i, search in enumerate(searches):
        # Create a card-like container for each search
        with st.container():
            col1, col2 = st.columns([5, 1])
            
            with col1:
                # Problem title with truncation
                st.markdown(f"**{i+1}. {search['problem_statement'][:100]}{'...' if len(search['problem_statement']) > 100 else ''}**")
                st.caption(f"Date: {format_datetime(str(search['created_at']))}")
            
            with col2:
                # Add a button to reanalyze this problem
                if st.button(f"Reanalyze", key=f"reanalyze_{search['id']}"):
                    st.session_state.problem_input = search['problem_statement']
                    # Redirect to app main page
                    st.session_state.current_view = "main"
                    st.rerun()  # Use st.rerun() instead of experimental_rerun
            
            # Add a separator between items
            st.markdown("---")