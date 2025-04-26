"""
File Upload Utilities for HACKSEEK

This module provides utilities for handling file uploads (images and audio)
and processing them for use with AI analysis.
"""
import os
import tempfile
import base64
from typing import Dict, Any, Optional, Tuple
import streamlit as st

def process_uploaded_image(uploaded_file) -> Tuple[Optional[str], Optional[str]]:
    """
    Process an uploaded image file.
    
    Args:
        uploaded_file: Streamlit UploadedFile object
        
    Returns:
        Tuple of (base64_encoded_image, preview_path)
    """
    if uploaded_file is None:
        return None, None
    
    # Save the file to a temporary location for display
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        preview_path = tmp_file.name
    
    # Get the base64 encoding for API calls
    base64_image = base64.b64encode(uploaded_file.getvalue()).decode('utf-8')
    
    return base64_image, preview_path

def process_uploaded_audio(uploaded_file) -> Tuple[Optional[str], Optional[str]]:
    """
    Process an uploaded audio file.
    
    Args:
        uploaded_file: Streamlit UploadedFile object
        
    Returns:
        Tuple of (base64_encoded_audio, audio_path)
    """
    if uploaded_file is None:
        return None, None
    
    # Save the file to a temporary location for playback
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        audio_path = tmp_file.name
    
    # Get the base64 encoding for API calls
    base64_audio = base64.b64encode(uploaded_file.getvalue()).decode('utf-8')
    
    return base64_audio, audio_path

def cleanup_temp_files(file_paths: list) -> None:
    """
    Clean up temporary files that were created for preview/playback.
    
    Args:
        file_paths: List of file paths to clean up
    """
    for path in file_paths:
        if path and os.path.exists(path):
            try:
                os.unlink(path)
            except Exception as e:
                st.error(f"Error cleaning up temporary file: {e}")

def initialize_file_upload_state() -> None:
    """
    Initialize session state variables for file uploads.
    """
    if 'temp_files' not in st.session_state:
        st.session_state.temp_files = []
    if 'uploaded_image' not in st.session_state:
        st.session_state.uploaded_image = None
    if 'uploaded_audio' not in st.session_state:
        st.session_state.uploaded_audio = None
    if 'image_preview_path' not in st.session_state:
        st.session_state.image_preview_path = None
    if 'audio_path' not in st.session_state:
        st.session_state.audio_path = None
    if 'transcription_result' not in st.session_state:
        st.session_state.transcription_result = None