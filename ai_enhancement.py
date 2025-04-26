"""
AI Enhancement Module for HACKSEEK

This module provides enhanced AI capabilities including image analysis
and speech-to-text functionality for improved problem analysis.
"""
import streamlit as st
from typing import Dict, Any, Optional, Tuple
import os
import time

from groq_api import analyze_problem_with_image, transcribe_audio_to_text, generate_enhanced_insights, groq_chat_completion
from file_upload_utils import process_uploaded_image, process_uploaded_audio, cleanup_temp_files, initialize_file_upload_state

def handle_image_upload() -> Tuple[Optional[str], Optional[str]]:
    """
    Handle image upload and processing.
    
    Returns:
        Tuple of (base64_encoded_image, preview_path)
    """
    uploaded_file = st.file_uploader(
        "Upload an image related to your problem", 
        type=["jpg", "jpeg", "png"],
        key="problem_image_uploader"
    )
    
    if uploaded_file:
        base64_image, preview_path = process_uploaded_image(uploaded_file)
        if preview_path:
            st.session_state.temp_files.append(preview_path)
            st.session_state.image_preview_path = preview_path
            st.session_state.uploaded_image = base64_image
            return base64_image, preview_path
    
    return None, None

def handle_audio_upload() -> Tuple[Optional[str], Optional[str]]:
    """
    Handle audio upload and processing.
    
    Returns:
        Tuple of (base64_encoded_audio, audio_path)
    """
    uploaded_file = st.file_uploader(
        "Upload an audio recording of your problem statement", 
        type=["wav", "mp3"],
        key="problem_audio_uploader"
    )
    
    if uploaded_file:
        base64_audio, audio_path = process_uploaded_audio(uploaded_file)
        if audio_path:
            st.session_state.temp_files.append(audio_path)
            st.session_state.audio_path = audio_path
            st.session_state.uploaded_audio = base64_audio
            return base64_audio, audio_path
    
    return None, None

def handle_transcription(audio_description: Optional[str] = None) -> Optional[str]:
    """
    Handle audio transcription.
    
    Args:
        audio_description: Optional text description of audio content (for simulation)
        
    Returns:
        Transcription text if successful, None otherwise
    """
    if st.session_state.uploaded_audio or audio_description:
        with st.spinner("Transcribing audio..."):
            if audio_description:
                # For simulation/testing
                result = transcribe_audio_to_text(audio_description)
            else:
                # In reality, we would pass the actual audio, but for this demo
                # we'll use a placeholder message
                result = transcribe_audio_to_text("This is a simulation of audio transcription since Groq doesn't support direct audio processing.")
            
            if result.get("success"):
                st.session_state.transcription_result = result.get("transcript")
                return result.get("transcript")
            else:
                st.error(f"Transcription failed: {result.get('error', 'Unknown error')}")
    
    return None

def generate_chat_response(user_input: str) -> str:
    """
    Generate a chat response based on user input.
    
    Args:
        user_input: User's chat message
        
    Returns:
        AI response text
    """
    messages = [
        {"role": "system", "content": "You are HACKSEEK's AI assistant, an expert in innovation, hackathons, and problem-solving. Help users with project ideas, technical questions, and creative solutions for hackathon challenges. Provide concise, practical advice and respond in a friendly, encouraging tone."},
        {"role": "user", "content": user_input}
    ]
    
    try:
        with st.spinner("Generating response..."):
            response = groq_chat_completion(messages, max_tokens=300, temperature=0.7)
            if "error" not in response:
                return response["choices"][0]["message"]["content"]
            else:
                return f"Error generating response: {response.get('error', 'Unknown error')}"
    except Exception as e:
        return f"Failed to generate response: {str(e)}"

def display_media_previews() -> None:
    """Display preview of uploaded media files."""
    col1, col2 = st.columns(2)
    
    with col1:
        if st.session_state.image_preview_path and os.path.exists(st.session_state.image_preview_path):
            st.image(st.session_state.image_preview_path, caption="Uploaded Image", use_column_width=True)
    
    with col2:
        if st.session_state.audio_path and os.path.exists(st.session_state.audio_path):
            st.audio(st.session_state.audio_path, format="audio/wav")
            
            if st.session_state.transcription_result:
                st.success("Audio Transcribed")
                with st.expander("View Transcription", expanded=True):
                    st.write(st.session_state.transcription_result)
            else:
                if st.button("Transcribe Audio"):
                    handle_transcription()

def analyze_with_enhancements(problem_statement: str) -> Dict[str, Any]:
    """
    Analyze a problem with additional image and audio enhancements.
    
    Args:
        problem_statement: The problem statement text
        
    Returns:
        Dict containing the enhanced analysis results
    """
    additional_context = ""
    
    # Add transcription as additional context if available
    if st.session_state.transcription_result:
        additional_context += f"Audio Transcription: {st.session_state.transcription_result}\n\n"
    
    # Process problem with image if available
    if st.session_state.uploaded_image:
        with st.spinner("Analyzing problem with image..."):
            try:
                result = analyze_problem_with_image(problem_statement, st.session_state.uploaded_image)
                if "error" not in result:
                    image_analysis = result["choices"][0]["message"]["content"]
                    additional_context += f"Image Analysis: {image_analysis}\n\n"
            except Exception as e:
                st.error(f"Error analyzing image: {e}")
    
    # Generate enhanced insights
    with st.spinner("Generating enhanced insights..."):
        try:
            enhanced_insights = generate_enhanced_insights(problem_statement, additional_context)
            return enhanced_insights
        except Exception as e:
            st.error(f"Error generating insights: {e}")
            return {"error": str(e)}

def render_ai_enhancement_tab() -> None:
    """Render the AI Enhancement tab UI."""
    st.header("AI Enhancement")
    
    st.markdown("""
    This feature allows you to enhance your problem analysis with additional context from images and audio.
    Upload an image related to your problem or record your problem statement to get more accurate and comprehensive insights.
    """)
    
    # Initialize session state
    initialize_file_upload_state()
    
    # Create tabs for different input methods
    tab1, tab2 = st.tabs(["🤖 AI Chat Bot", "💡 Enhanced Analysis"])
    
    with tab1:
        st.subheader("AI Chat Bot")
        st.markdown("Have a conversation with the AI chat bot. Ask questions or discuss your hackathon project ideas.")
        
        # Initialize conversation history in session state if it doesn't exist
        if "conversation_history" not in st.session_state:
            st.session_state.conversation_history = []
        
        # Display conversation history
        for i, (role, message) in enumerate(st.session_state.conversation_history):
            if role == "user":
                st.markdown(f"**You:** {message}")
            else:
                st.markdown(f"**AI:** {message}")
            
            # Add a small visual separator between messages
            if i < len(st.session_state.conversation_history) - 1:
                st.markdown("---")
        
        # Chat message input box
        st.write("")
        
        # Initialize message input in session state if it doesn't exist
        if "message_input" not in st.session_state:
            st.session_state.message_input = ""
            
        # Create the text input with the current session state value
        audio_description = st.text_area(
            "Type your message:", 
            value=st.session_state.message_input,
            help="Type a message to chat with the AI assistant."
        )
        
        if audio_description and st.button("Send Message"):
            # Add user message to conversation history
            st.session_state.conversation_history.append(("user", audio_description))
            
            # Generate AI response
            response = generate_chat_response(audio_description)
            
            # Add AI response to conversation history
            st.session_state.conversation_history.append(("ai", response))
            
            # Clear the input text area by setting the session state value to empty
            st.session_state.message_input = ""
            
            # Rerun to display updated conversation and clear input
            st.rerun()
    
    with tab2:
        st.subheader("Enhanced Analysis")
        
        # Display previews of uploaded media
        display_media_previews()
        
        # Problem statement input
        problem_statement = st.text_area(
            "Enter your problem statement:", 
            height=150,
            help="Describe your problem or challenge in detail."
        )
        
        # Analysis button
        if problem_statement and st.button("Generate Enhanced Analysis"):
            result = analyze_with_enhancements(problem_statement)
            
            if result.get("success"):
                st.success("Enhanced analysis generated")
                with st.expander("Enhanced Insights", expanded=True):
                    st.markdown(result.get("enhanced_insights"))
            else:
                st.error(f"Analysis failed: {result.get('error', 'Unknown error')}")
    
    # Cleanup temp files when the app is closed or reset
    if st.session_state.temp_files:
        cleanup_temp_files(st.session_state.temp_files)