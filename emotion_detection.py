import requests

def emotion_detector(text_to_analyze):
    """Function to detect emotions using Watson NLP's EmotionPredict"""
    
    # Define the API URL
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    # Headers required for the request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # JSON payload with text input
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send a POST request to Watson NLP
    response = requests.post(url, headers=headers, json=payload)

    # Process the response and return the result
    if response.status_code == 200:
        return response.json()  # Extract emotion analysis data
    else:
        return {"error": f"Request failed with status code {response.status_code}"}

