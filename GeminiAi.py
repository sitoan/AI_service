
import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

class GeminiAi:
    def __init__(self):
        # Create the model
        generation_config = {
        "temperature": 1,
        # "top_p": 0.95,
        # "top_k": 64,
        # "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
        }
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-pro",
            generation_config=generation_config,
            safety_settings = [
                {
                    "category": "HARM_CATEGORY_DANGEROUS",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
            ],
            system_instruction = "chỉ đưa ra câu trả lời, không giải thích thêm và trả lời bằng ngôn ngữ Việt Nam"
        )

    def run(self, message):
        response = self.model.generate_content(message)
        return response.text




