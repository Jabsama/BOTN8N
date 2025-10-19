#!/usr/bin/env python3
"""
VoltageGPU API - Chat Completions Example (Python)
Non-streaming request to the chat completions endpoint

Usage:
    export VOLTAGE_API_KEY="your_api_key_here"
    python3 python.chat-completions.py
"""

import os
import json
import requests
from typing import Dict, List, Optional

def call_voltage_api(
    messages: List[Dict[str, str]],
    model: str = "deepseek-ai/DeepSeek-R1-sgtest",
    max_tokens: int = 512,
    temperature: float = 0.7,
    api_key: Optional[str] = None
) -> Dict:
    """
    Call VoltageGPU Chat Completions API
    
    Args:
        messages: List of message dictionaries with 'role' and 'content'
        model: Model to use for completion
        max_tokens: Maximum tokens in response
        temperature: Sampling temperature (0-1)
        api_key: API key (if not provided, uses VOLTAGE_API_KEY env var)
    
    Returns:
        API response as dictionary
    """
    # Get API key from environment if not provided
    if api_key is None:
        api_key = os.environ.get('VOLTAGE_API_KEY')
        if not api_key:
            raise ValueError(
                "API key not provided. Set VOLTAGE_API_KEY environment variable "
                "or pass api_key parameter"
            )
    
    # API endpoint
    url = "https://api.voltagegpu.com/v1/chat/completions"
    
    # Headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Request payload
    payload = {
        "model": model,
        "stream": False,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "messages": messages
    }
    
    # Make request
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling API: {e}")
        if hasattr(e.response, 'text'):
            print(f"Response: {e.response.text}")
        raise


def extract_content(response: Dict) -> str:
    """Extract the assistant's response content from API response"""
    try:
        return response['choices'][0]['message']['content']
    except (KeyError, IndexError):
        return "No response content found"


def main():
    """Example usage of VoltageGPU API"""
    
    print("VoltageGPU Chat Completions Example")
    print("-" * 40)
    
    # Example 1: Simple coding question
    messages = [
        {
            "role": "system",
            "content": "You are a helpful coding assistant. Keep answers concise and include code when relevant."
        },
        {
            "role": "user",
            "content": "Write a Python function to calculate fibonacci numbers"
        }
    ]
    
    print("Sending request to VoltageGPU API...")
    print(f"User: {messages[1]['content']}")
    print()
    
    try:
        response = call_voltage_api(messages)
        content = extract_content(response)
        
        print("Assistant:")
        print(content)
        print()
        
        # Print token usage
        if 'usage' in response:
            usage = response['usage']
            print(f"Token usage: {usage.get('total_tokens', 'N/A')} total")
            print(f"  - Prompt: {usage.get('prompt_tokens', 'N/A')}")
            print(f"  - Completion: {usage.get('completion_tokens', 'N/A')}")
    
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    print("-" * 40)
    
    # Example 2: Multi-turn conversation
    print("\nExample 2: Multi-turn conversation")
    print("-" * 40)
    
    conversation = [
        {
            "role": "system",
            "content": "You are an expert on VoltageGPU infrastructure."
        },
        {
            "role": "user",
            "content": "What makes VoltageGPU different from traditional cloud providers?"
        }
    ]
    
    try:
        response = call_voltage_api(conversation)
        assistant_response = extract_content(response)
        
        print("User:", conversation[1]['content'])
        print("\nAssistant:", assistant_response)
        
        # Add assistant response to conversation
        conversation.append({
            "role": "assistant",
            "content": assistant_response
        })
        
        # Follow-up question
        conversation.append({
            "role": "user",
            "content": "What about the pricing?"
        })
        
        print("\nUser:", conversation[-1]['content'])
        
        response = call_voltage_api(conversation)
        print("\nAssistant:", extract_content(response))
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
