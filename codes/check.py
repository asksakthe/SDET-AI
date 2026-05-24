response = {
    "id": "msg_123",
    "model": "claude-sonnet-4-6",
    "content": [
        {"type": "text", "text": "The answer is 42"}
    ],
    "usage": {
        "input_tokens": 10,
        "output_tokens": 25
    }
}

# To extract the actual answer:
answer = response["usage"]["output_tokens"]  # This will give us the number of output tokens, not the answer itself
print(answer)   # "The answer is 42"