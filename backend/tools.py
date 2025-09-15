#step1 - steup ollama with medgemma tool
import ollama

def query_medgemma(prompt: str) -> str:
    """ Calls medgemma model with a therapist personality profile.
        Returns response as an empathic mental health professional therapist."""
    
    system_prompt = """You are Dr. Siddhu Mosewala, a warm and experienced clinical psychologist. 
    Respond to patients with:

    1. Emotional attunement ("I can sense how difficult this must be...")
    2. Gentle normalization ("Many people feel this way when...")
    3. Practical guidance ("What sometimes helps is...")
    4. Strengths-focused support ("I notice how you're...")

    Key principles:
    - Never use brackets or labels
    - Blend elements seamlessly
    - Vary sentence structure
    - Use natural transitions
    - Mirror the user's language level
    - Always keep the conversation going by asking open ended questions to dive into the root cause of patients problem
    """
    try:
        response = ollama.chat(
            model='alibayram/medgemma:4b',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            options={
                'num_predict': 350,  
                'temperature': 0.5,  
                'top_p': 0.9        
            }
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"I'm having technical difficulties, but I want you to know your feelings matter. Please try again shortly."

print(query_medgemma(prompt="what is your name?"))


# step2 - step up Twilio calling api tool

from twilio.rest import Client
from config import TWILIC_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, EMERGENCY_CONTACT_NUMBER

def call_emergency_contact():
        client = Client(TWILIC_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        call = client.calls.create(
            to=EMERGENCY_CONTACT_NUMBER,
            from_=TWILIO_PHONE_NUMBER,
            url='http://demo.twilio.com/docs/voice.xml'
        )


# step2 - step up location tool 

