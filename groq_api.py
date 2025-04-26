"""
Groq API Integration for HACKSEEK

This module provides integration with Groq's API for text analysis and model inference.
"""
import os
import json
import base64
import requests
from typing import Dict, Any, List, Optional

# Use the Groq API key from environment variables
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

# Groq API base URL
GROQ_API_BASE = "https://api.groq.com/openai/v1"

def groq_chat_completion(
    messages: List[Dict[str, str]], 
    model: str = "llama3-70b-8192",
    max_tokens: int = 1000,
    temperature: float = 0.7
) -> Dict[str, Any]:
    """
    Send a request to Groq's chat completion API.
    
    Args:
        messages: List of message dictionaries with 'role' and 'content'
        model: The Groq model to use
        max_tokens: Maximum tokens to generate
        temperature: Temperature for response generation (0-1)
        
    Returns:
        Dict containing the response from Groq API
    """
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": model,
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    
    try:
        response = requests.post(
            f"{GROQ_API_BASE}/chat/completions",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error with Groq API: {e}")
        return {"error": str(e)}

def analyze_problem_with_image(
    problem_text: str, 
    image_base64: str,
    analysis_type: str = "general"
) -> Dict[str, Any]:
    """
    Analyze a problem with an accompanying image.
    
    Args:
        problem_text: The problem statement text
        image_base64: Base64 encoded image data
        analysis_type: Type of analysis to perform
        
    Returns:
        Dict containing the analysis results
    """
    # For the image analysis, we would normally use the vision endpoints of OpenAI
    # or other multimodal providers, but Groq doesn't yet support image inputs.
    # Instead, we'll describe that we've received an image and provide image context
    # in the text itself.
    
    messages = [
        {"role": "system", "content": f"You are an expert problem analyzer for {analysis_type} domains. A user has provided both a problem statement and an image. Focus on extracting the key components of the problem."},
        {"role": "user", "content": f"Here's my problem statement: {problem_text}\n\nI've also attached an image related to this problem (this would normally be an image upload, but the image content isn't available in this API call). Please analyze this problem statement comprehensively, identify key challenges, potential approaches, and provide a structured analysis."}
    ]
    
    return groq_chat_completion(messages, max_tokens=1500)

def transcribe_audio_to_text(audio_text_description: str) -> Dict[str, Any]:
    """
    Simulate transcription by having LLM analyze a text description of audio.
    
    Args:
        audio_text_description: Description of what was said in the audio
        
    Returns:
        Dict containing the transcription result
    """
    # Since Groq doesn't have audio transcription, we're simulating with a description
    messages = [
        {"role": "system", "content": "You are an expert transcription system. Convert the audio description into a proper text transcript."},
        {"role": "user", "content": f"Here's a description of what was said in the audio: {audio_text_description}\n\nPlease format this as a proper transcript."}
    ]
    
    response = groq_chat_completion(messages, max_tokens=500, temperature=0.3)
    
    if "error" in response:
        return {"error": response["error"]}
    
    try:
        transcript = response["choices"][0]["message"]["content"]
        return {
            "success": True,
            "transcript": transcript
        }
    except Exception as e:
        return {"error": f"Failed to process transcription: {str(e)}"}

def generate_enhanced_insights(problem_statement: str, additional_context: Optional[str] = None) -> Dict[str, Any]:
    """
    Generate enhanced insights for a problem statement with optional additional context.
    
    Args:
        problem_statement: The problem statement text
        additional_context: Optional additional context from image or audio
        
    Returns:
        Dict containing the enhanced insights
    """
    prompt = f"Problem Statement: {problem_statement}"
    
    if additional_context:
        prompt += f"\n\nAdditional Context: {additional_context}"
    
    messages = [
        {"role": "system", "content": "You are an advanced innovation insights generator. Analyze the problem statement and provide deep, actionable insights that might not be immediately obvious. Organize your response into: 1) Core Problem Identification, 2) Hidden Factors, 3) Cross-Domain Connections, 4) Potential Innovation Paths, and 5) Success Metrics."},
        {"role": "user", "content": prompt}
    ]
    
    response = groq_chat_completion(messages, max_tokens=2000)
    
    if "error" in response:
        return {"error": response["error"]}
    
    try:
        insights_text = response["choices"][0]["message"]["content"]
        return {
            "success": True,
            "enhanced_insights": insights_text
        }
    except Exception as e:
        return {"error": f"Failed to generate insights: {str(e)}"}