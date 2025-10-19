#!/bin/bash

# VoltageGPU API - Chat Completions Example (cURL)
# Non-streaming request to the chat completions endpoint
# 
# Usage: 
#   export VOLTAGE_API_KEY="your_api_key_here"
#   ./curl.chat-completions.sh

# Check if API key is set
if [ -z "$VOLTAGE_API_KEY" ]; then
    echo "Error: VOLTAGE_API_KEY environment variable is not set"
    echo "Please set it with: export VOLTAGE_API_KEY='your_api_key_here'"
    exit 1
fi

# API endpoint
API_URL="https://api.voltagegpu.com/v1/chat/completions"

# Make the request
echo "Sending request to VoltageGPU API..."
echo "---"

curl -X POST "$API_URL" \
  -H "Authorization: Bearer $VOLTAGE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-ai/DeepSeek-R1-sgtest",
    "stream": false,
    "max_tokens": 512,
    "temperature": 0.7,
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful coding assistant. Keep answers concise and include code when relevant."
      },
      {
        "role": "user",
        "content": "Write a Python function to calculate fibonacci numbers"
      }
    ]
  }' | python3 -m json.tool

echo "---"
echo "Request completed!"

# Example response format:
# {
#   "id": "chatcmpl-xxx",
#   "object": "chat.completion",
#   "created": 1234567890,
#   "model": "deepseek-ai/DeepSeek-R1-sgtest",
#   "choices": [
#     {
#       "index": 0,
#       "message": {
#         "role": "assistant",
#         "content": "Here's a Python function..."
#       },
#       "finish_reason": "stop"
#     }
#   ],
#   "usage": {
#     "prompt_tokens": 20,
#     "completion_tokens": 150,
#     "total_tokens": 170
#   }
# }
