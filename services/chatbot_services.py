import openai

class AppointmentChatBot:
    def __init__(self, api_key, appointments_context):
        openai.api_key = api_key
        self.appointments_context = appointments_context

    def get_ai_response(self, chat_messages):
        # Prepare the messages for OpenAI, including system context
        messages = [
            {"role": "system", "content": f"You are an AI assistant for appointment data. Use the following context: {self.appointments_context}"}
        ] + chat_messages
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Or another model like gpt-4 if available
                messages=messages,
                max_tokens=150,
                temperature=0.7
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"