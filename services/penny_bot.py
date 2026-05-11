import json
from pathlib import Path
from openai import OpenAI

class SalonDataStore:
    def __init__(self, appt_file, users_file, inventory_file):
        self.appt_file = Path(appt_file)
        self.users_file = Path(users_file)
        self.inventory_file = Path(inventory_file)

    def get_salon_context(self):
        context = ""
        try:
            if self.appt_file.exists():
                with open(self.appt_file, "r") as f:
                    appointments = json.load(f)
                context += f"Appointments: {json.dumps(appointments)}\n"
            if self.users_file.exists():
                with open(self.users_file, "r") as f:
                    users = json.load(f)
                context += f"Users: {json.dumps(users)}\n"
            if self.inventory_file.exists():
                with open(self.inventory_file, "r") as f:
                    inventory = json.load(f)
                context += f"Inventory: {json.dumps(inventory)}\n"
        except Exception as e:
            context = f"Error loading data: {str(e)}"
        return context

class ChatLoggerStore:
    def __init__(self, chat_logs_file):
        self.chat_logs_file = Path(chat_logs_file)

    def load_logs(self):
        if self.chat_logs_file.exists():
            try:
                with open(self.chat_logs_file, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def save_logs(self, logs):
        with open(self.chat_logs_file, "w") as f:
            json.dump(logs, f, indent=4)

class PennyBot:
    def __init__(self, api_key, salon_context):
        self.client = OpenAI(api_key=api_key)
        self.salon_context = salon_context

    def get_ai_response(self, chat_messages):
        messages = [
            {"role": "system", "content": f"You are Penny the Polish Pro, an AI assistant for a salon. Use this context: {self.salon_context}"}
        ] + chat_messages
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=150,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"