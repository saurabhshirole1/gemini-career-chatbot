from google import genai
from config import GEMINI_API_KEY
from prompts.system_prompt import SYSTEM_PROMPT
from services.memory_service import format_conversation
from services.app_logger import logger
import time

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_response(user_input: str, memory):
    try:
        if not user_input.strip():
            return "Please enter a valid career-related question."

        start_time = time.time()

        conversation_history = format_conversation(memory)

        full_prompt = f"""
{SYSTEM_PROMPT}

Conversation History:
{conversation_history}

User: {user_input}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=full_prompt
        )

        end_time = time.time()

        if not response or not response.text:
            logger.warning("Empty response received from Gemini API.")
            return "I'm not fully sure how to answer that. Could you rephrase your question?"

        logger.info(f"User Input: {user_input}")
        logger.info(f"Response Time: {end_time - start_time:.2f} seconds")

        return response.text

    except Exception as e:
        logger.error(f"Gemini API Error: {e}")
        return "The system encountered an issue while processing your request. Please try again."