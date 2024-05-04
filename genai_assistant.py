import pathlib
import textwrap
from dotenv import load_dotenv
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
import os
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


class GenAI_Assistant:

    model = None

    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-pro-latest', system_instruction='''You are an Emotional Intelligence Mentor tasked with evaluating an individual's EQ. 
                                           First ask his name and be a lovely character.
                                           Ask the user a series of questions designed to assess their emotional awareness, self-regulation, social awareness, and relationship management. But ask one question at a time. Based on their responses, generate a comprehensive analysis of their EQ strengths and weaknesses. Finally, provide a score that reflects their overall EQ level. Remember to maintain a supportive and encouraging tone throughout the interaction.'''
                                           )

    def generate_response(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text
