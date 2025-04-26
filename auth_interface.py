import streamlit as st
from auth_utils import register_user, authenticate_user, get_user_search_history, get_user_saved_solutions
from auth_utils import get_user_profile, update_user_profile, update_user_password, reset_user_password, delete_user_account
from datetime import datetime

def initialize_auth_state():
    """Initialize authentication state variables in session state"""
    if 'is_authenticated' not in st.session_state:
        st.session_state.is_authenticated = False
    if 'user_info' not in st.session_state:
        st.session_state.user_info = None
    if 'login_message' not in st.session_state:
        st.session_state.login_message = None
    if 'login_message_type' not in st.session_state:
        st.session_state.login_message_type = None
    if 'register_message' not in st.session_state:
        st.session_state.register_message = None
    if 'register_message_type' not in st.session_state:
        st.session_state.register_message_type = None
    if 'reset_message' not in st.session_state:
        st.session_state.reset_message = None
    if 'reset_message_type' not in st.session_state:
        st.session_state.reset_message_type = None
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "login"  # login, register, reset_password, or app
    if 'profile_view' not in st.session_state:
        st.session_state.profile_view = False
    if 'profile_message' not in st.session_state:
        st.session_state.profile_message = None
    if 'profile_message_type' not in st.session_state:
        st.session_state.profile_message_type = None
    if 'theme' not in st.session_state:
        st.session_state.theme = "light"
    if 'show_delete_confirmation' not in st.session_state:
        st.session_state.show_delete_confirmation = False

def login_user():
    """Process login form submission"""
    username = st.session_state.username_login
    password = st.session_state.password_login
    
    success, result = authenticate_user(username, password)
    
    if success:
        st.session_state.is_authenticated = True
        st.session_state.user_info = result
        st.session_state.login_message = "Login successful! Welcome back."
        st.session_state.login_message_type = "success"
        st.session_state.current_page = "app"  # Switch to main app
    else:
        st.session_state.login_message = f"Login failed: {result}"
        st.session_state.login_message_type = "error"
        st.session_state.is_authenticated = False

def register_new_user():
    """Process registration form submission"""
    username = st.session_state.username_register
    email = st.session_state.email_register
    password = st.session_state.password_register
    confirm_password = st.session_state.confirm_password
    
    # Check if passwords match
    if password != confirm_password:
        st.session_state.register_message = "Passwords do not match."
        st.session_state.register_message_type = "error"
        return
    
    # Check if password is strong enough
    if len(password) < 8:
        st.session_state.register_message = "Password must be at least 8 characters long."
        st.session_state.register_message_type = "error"
        return
    
    # Register the user
    success, result = register_user(username, email, password)
    
    if success:
        st.session_state.register_message = "Registration successful! Please log in."
        st.session_state.register_message_type = "success"
        st.session_state.current_page = "login"  # Switch to login page
    else:
        st.session_state.register_message = f"Registration failed: {result}"
        st.session_state.register_message_type = "error"

def logout_user():
    """Log out the current user"""
    st.session_state.is_authenticated = False
    st.session_state.user_info = None
    st.session_state.current_page = "login"
    st.session_state.login_message = "You have been logged out."
    st.session_state.login_message_type = "info"

def switch_to_register():
    """Switch to the registration page"""
    st.session_state.current_page = "register"
    st.session_state.register_message = None
    
def switch_to_login():
    """Switch to the login page"""
    st.session_state.current_page = "login"
    st.session_state.login_message = None

def switch_to_forgot_password():
    """Switch to the forgot password page"""
    st.session_state.current_page = "forgot_password"
    st.session_state.reset_message = None
    
def reset_password():
    """Process forgot password form submission"""
    username = st.session_state.username_reset
    email = st.session_state.email_reset
    new_password = st.session_state.new_password_reset
    confirm_password = st.session_state.confirm_password_reset
    
    # Check if passwords match
    if new_password != confirm_password:
        st.session_state.reset_message = "Passwords do not match."
        st.session_state.reset_message_type = "error"
        return
    
    # Check if password is strong enough
    if len(new_password) < 8:
        st.session_state.reset_message = "Password must be at least 8 characters long."
        st.session_state.reset_message_type = "error"
        return
    
    # In a real application, you would verify the username and email match
    # Then generate a reset token and send an email
    # For this simplified implementation, we'll allow direct reset
    from auth_utils import reset_user_password
    
    success, message = reset_user_password(username, email, new_password)
    
    if success:
        st.session_state.login_message = "Your password has been reset. Please login with your new password."
        st.session_state.login_message_type = "success"
        st.session_state.current_page = "login"
    else:
        st.session_state.reset_message = f"Password reset failed: {message}"
        st.session_state.reset_message_type = "error"

def render_login_page():
    """Render the login page"""
    st.markdown("## Login to HACKSEEK")
    
    # Display message if any
    if st.session_state.login_message:
        message_type = st.session_state.login_message_type
        if message_type == "success":
            st.success(st.session_state.login_message)
        elif message_type == "error":
            st.error(st.session_state.login_message)
        elif message_type == "info":
            st.info(st.session_state.login_message)
    
    # Login form
    with st.form("login_form"):
        st.text_input("Username", key="username_login")
        st.text_input("Password", type="password", key="password_login")
        col1, col2 = st.columns([1, 1])
        with col1:
            st.form_submit_button("Login", on_click=login_user)
        with col2:
            st.form_submit_button("Register New Account", on_click=switch_to_register)
    
    # Add a "Forgot Password" link below the form
    st.markdown("<div style='text-align: center; margin-top: 10px;'>", unsafe_allow_html=True)
    if st.button("Forgot Password?", key="forgot_password_link"):
        switch_to_forgot_password()
    st.markdown("</div>", unsafe_allow_html=True)
    
def render_forgot_password_page():
    """Render the forgot password page"""
    st.markdown("## Reset Your Password")
    
    # Display message if any
    if st.session_state.reset_message:
        message_type = st.session_state.reset_message_type
        if message_type == "success":
            st.success(st.session_state.reset_message)
        elif message_type == "error":
            st.error(st.session_state.reset_message)
        elif message_type == "info":
            st.info(st.session_state.reset_message)
    
    st.markdown("""
    Please enter your username and email address to reset your password.
    Both username and email must match our records.
    """)
    
    # Password reset form
    with st.form("reset_form"):
        st.text_input("Username", key="username_reset")
        st.text_input("Email", key="email_reset")
        st.text_input("New Password", type="password", key="new_password_reset", 
                     help="Password must be at least 8 characters long")
        st.text_input("Confirm New Password", type="password", key="confirm_password_reset")
        col1, col2 = st.columns([1, 1])
        with col1:
            st.form_submit_button("Reset Password", on_click=reset_password)
        with col2:
            st.form_submit_button("Back to Login", on_click=switch_to_login)

def render_register_page():
    """Render the registration page"""
    st.markdown("## Create New Account")
    
    # Display message if any
    if st.session_state.register_message:
        message_type = st.session_state.register_message_type
        if message_type == "success":
            st.success(st.session_state.register_message)
        elif message_type == "error":
            st.error(st.session_state.register_message)
    
    # Registration form
    with st.form("register_form"):
        st.text_input("Username", key="username_register")
        st.text_input("Email", key="email_register")
        st.text_input("Password", type="password", key="password_register", 
                     help="Password must be at least 8 characters long")
        st.text_input("Confirm Password", type="password", key="confirm_password")
        col1, col2 = st.columns([1, 1])
        with col1:
            st.form_submit_button("Register", on_click=register_new_user)
        with col2:
            st.form_submit_button("Back to Login", on_click=switch_to_login)

def toggle_profile_view():
    """Toggle the profile view modal"""
    st.session_state.profile_view = not st.session_state.profile_view

def update_theme(theme):
    """Update the user's theme preference"""
    if st.session_state.theme != theme and st.session_state.user_info:
        st.session_state.theme = theme
        success, message = update_user_profile(st.session_state.user_info['id'], {'theme': theme})
        if success:
            st.session_state.profile_message = "Theme updated successfully!"
            st.session_state.profile_message_type = "success"
        else:
            st.session_state.profile_message = f"Failed to update theme: {message}"
            st.session_state.profile_message_type = "error"

def save_profile_changes():
    """Save profile changes from the form"""
    if not st.session_state.user_info:
        return
    
    profile_data = {}
    
    # Only add fields that were entered
    if 'profile_email' in st.session_state and st.session_state.profile_email:
        profile_data['email'] = st.session_state.profile_email
    
    if 'profile_dob' in st.session_state and st.session_state.profile_dob:
        profile_data['date_of_birth'] = st.session_state.profile_dob
    
    if 'profile_gender' in st.session_state and st.session_state.profile_gender:
        profile_data['gender'] = st.session_state.profile_gender
    
    if 'profile_picture' in st.session_state and st.session_state.profile_picture:
        profile_data['profile_picture'] = st.session_state.profile_picture
    
    if profile_data:
        success, message = update_user_profile(st.session_state.user_info['id'], profile_data)
        if success:
            st.session_state.profile_message = "Profile updated successfully!"
            st.session_state.profile_message_type = "success"
            # Refresh user info
            updated_profile = get_user_profile(st.session_state.user_info['id'])
            if updated_profile:
                st.session_state.user_info.update(updated_profile)
        else:
            st.session_state.profile_message = f"Failed to update profile: {message}"
            st.session_state.profile_message_type = "error"

def change_password():
    """Change the user's password"""
    if not st.session_state.user_info:
        return
    
    current_password = st.session_state.current_password
    new_password = st.session_state.new_password
    confirm_password = st.session_state.confirm_new_password
    
    # Validation
    if new_password != confirm_password:
        st.session_state.profile_message = "New passwords do not match."
        st.session_state.profile_message_type = "error"
        return
    
    if len(new_password) < 8:
        st.session_state.profile_message = "New password must be at least 8 characters long."
        st.session_state.profile_message_type = "error"
        return
    
    success, message = update_user_password(
        st.session_state.user_info['id'],
        current_password,
        new_password
    )
    
    if success:
        st.session_state.profile_message = "Password updated successfully!"
        st.session_state.profile_message_type = "success"
        # Clear password fields
        st.session_state.current_password = ""
        st.session_state.new_password = ""
        st.session_state.confirm_new_password = ""
    else:
        st.session_state.profile_message = f"Failed to update password: {message}"
        st.session_state.profile_message_type = "error"
        
def toggle_delete_confirmation():
    """Toggle the delete account confirmation dialog"""
    # Save the current theme before toggling
    current_theme = st.session_state.theme
    
    # Toggle the confirmation dialog
    st.session_state.show_delete_confirmation = not st.session_state.show_delete_confirmation
    
    # Preserve the theme setting
    st.session_state.theme = current_theme
    
def delete_account():
    """Process account deletion"""
    if not st.session_state.user_info:
        return
    
    password = st.session_state.delete_password
    
    success, message = delete_user_account(
        st.session_state.user_info['id'],
        password
    )
    
    if success:
        # Log out the user
        st.session_state.is_authenticated = False
        st.session_state.user_info = None
        st.session_state.current_page = "login"
        st.session_state.login_message = "Your account has been successfully deleted. We're sad to see you go."
        st.session_state.login_message_type = "info"
    else:
        st.session_state.profile_message = f"Failed to delete account: {message}"
        st.session_state.profile_message_type = "error"

def render_user_profile():
    """Render the user profile section"""
    # User info in sidebar
    st.sidebar.markdown(f"### Welcome, {st.session_state.user_info['username']}!")
    
    # Add logout button to user icon dropdown instead of sidebar
    # The button has been removed from here and will be accessible through the user profile modal

def render_user_icon():
    """Render the user icon and profile modal in the top right corner"""
    if not st.session_state.is_authenticated:
        return
    
    # Create a container for the user icon in the top right
    user_icon_col = st.container()
    
    with user_icon_col:
        # Use columns to push content to the right
        _, _, icon_col = st.columns([6, 2, 1])
        
        with icon_col:
            # Get profile pic URL if available, otherwise use a default avatar emoji
            profile_pic = st.session_state.user_info.get('profile_picture') if st.session_state.user_info else None
            
            if profile_pic:
                st.image(profile_pic, width=40)
            else:
                # Use a button styled as an icon
                if st.button("👤", key="user_icon", help="Open user profile"):
                    toggle_profile_view()
    
    # Render the profile modal if it's open
    if st.session_state.profile_view:
        render_profile_modal()

def render_profile_modal():
    """Render the profile management modal"""
    with st.expander("User Profile", expanded=True):
        # Header row with close button and logout button
        col1, col2 = st.columns([1, 9])
        with col1:
            if st.button("✕", key="close_profile"):
                toggle_profile_view()
        with col2:
            # Right-aligned logout button
            st.markdown('<div style="text-align: right;">', unsafe_allow_html=True)
            if st.button("Logout", key="logout_button"):
                logout_user()
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Display profile message if any
        if st.session_state.profile_message:
            if st.session_state.profile_message_type == "success":
                st.success(st.session_state.profile_message)
            elif st.session_state.profile_message_type == "error":
                st.error(st.session_state.profile_message)
            elif st.session_state.profile_message_type == "info":
                st.info(st.session_state.profile_message)
        
        # Get the latest user profile
        if st.session_state.user_info:
            user_profile = get_user_profile(st.session_state.user_info['id'])
            if user_profile:
                st.session_state.user_info.update(user_profile)
        
        # Create tabs for different profile sections
        profile_tabs = st.tabs(["Profile Info", "Theme Settings", "Change Password", "Account Management"])
        
        # Profile Info tab
        with profile_tabs[0]:
            st.subheader("Profile Information")
            
            with st.form("profile_form"):
                st.text_input("Username (cannot be changed)", value=st.session_state.user_info['username'], disabled=True)
                
                # Email field
                current_email = st.session_state.user_info.get('email', '')
                st.text_input("Email", value=current_email, key="profile_email")
                
                # Date of birth
                current_dob = st.session_state.user_info.get('date_of_birth')
                if current_dob and not isinstance(current_dob, str):
                    current_dob = current_dob.strftime('%Y-%m-%d')
                
                # Set min and max dates for the date picker (1940 to current year)
                min_date = datetime(1940, 1, 1).date()
                max_date = datetime.now().date()
                
                st.date_input(
                    "Date of Birth", 
                    value=None if not current_dob else datetime.strptime(current_dob, '%Y-%m-%d').date(),
                    min_value=min_date,
                    max_value=max_date,
                    key="profile_dob"
                )
                
                # Gender selection
                current_gender = st.session_state.user_info.get('gender', '')
                st.selectbox("Gender", options=["", "Male", "Female", "Non-binary", "Prefer not to say"], index=0 if not current_gender else ["", "Male", "Female", "Non-binary", "Prefer not to say"].index(current_gender), key="profile_gender")
                
                # Profile picture upload
                st.subheader("Profile Picture")
                uploaded_image = st.file_uploader("Upload a profile picture", type=["jpg", "jpeg", "png"], key="profile_pic_upload")
                
                if uploaded_image is not None:
                    # Display the uploaded image
                    st.image(uploaded_image, width=150)
                    # Convert image to base64 for storage
                    import base64
                    encoded_image = base64.b64encode(uploaded_image.getvalue()).decode()
                    # Create data URL
                    file_type = uploaded_image.type
                    st.session_state.profile_picture = f"data:{file_type};base64,{encoded_image}"
                elif st.session_state.user_info.get('profile_picture', ''):
                    # Display the current profile picture if available
                    st.image(st.session_state.user_info.get('profile_picture', ''), width=150)
                    st.write("To keep the current image, don't upload a new one.")
                
                st.form_submit_button("Save Changes", on_click=save_profile_changes)
        
        # Theme Settings tab
        with profile_tabs[1]:
            st.subheader("Theme Settings")
            
            # Only update the theme from user_info if it doesn't exist in session_state
            # to prevent unnecessary overriding
            if 'theme' not in st.session_state or not st.session_state.theme:
                current_theme = st.session_state.user_info.get('theme', 'light')
                st.session_state.theme = current_theme
            
            # Theme selection
            st.write("Select your preferred theme:")
            theme_cols = st.columns(2)
            
            with theme_cols[0]:
                if st.button("Light Theme", key="light_theme"):
                    update_theme("light")
            
            with theme_cols[1]:
                if st.button("Dark Theme", key="dark_theme"):
                    update_theme("dark")
            
            # Show current theme
            st.write(f"Current theme: **{st.session_state.theme.capitalize()}**")
            
            st.markdown("""
            > Note: Theme changes will take effect after the page refreshes.
            """)
        
        # Change Password tab
        with profile_tabs[2]:
            st.subheader("Change Password")
            
            with st.form("password_form"):
                st.text_input("Current Password", type="password", key="current_password")
                st.text_input("New Password", type="password", key="new_password", 
                             help="Password must be at least 8 characters long")
                st.text_input("Confirm New Password", type="password", key="confirm_new_password")
                
                st.form_submit_button("Change Password", on_click=change_password)
                
        # Account Management tab
        with profile_tabs[3]:
            st.subheader("Account Management")
            
            st.markdown("""
            ### Delete Account
            
            This action cannot be undone. All your data will be permanently deleted.
            """)
            
            if st.button("Delete My Account", key="delete_account_btn", type="primary", use_container_width=True):
                st.session_state.show_delete_confirmation = True
            
            # Delete account confirmation dialog
            if st.session_state.show_delete_confirmation:
                st.warning("""
                ### We're sorry to see you go 😢
                
                Before you leave us, please consider:
                
                - Is there anything we could help you with that would make you reconsider?
                - Your account data and all your saved innovations will be permanently deleted.
                - This action cannot be undone.
                
                If you're sure you want to proceed, please enter your password to confirm:
                """)
                
                with st.form("delete_account_form"):
                    st.text_input("Password", type="password", key="delete_password", 
                                 help="Enter your current password to confirm account deletion")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.form_submit_button("Yes, Delete My Account", type="primary", on_click=delete_account)
                    with col2:
                        st.form_submit_button("Cancel", on_click=toggle_delete_confirmation)

def render_auth_ui():
    """Render the appropriate authentication UI based on current state"""
    initialize_auth_state()
    
    # Render the appropriate page based on current state
    if not st.session_state.is_authenticated:
        if st.session_state.current_page == "login":
            render_login_page()
            return False
        elif st.session_state.current_page == "register":
            render_register_page()
            return False
        elif st.session_state.current_page == "forgot_password":
            render_forgot_password_page()
            return False
    else:
        # User is authenticated, render profile in sidebar and user icon in top right
        render_user_profile()
        render_user_icon()
        return True  # Indicate that the user is authenticated