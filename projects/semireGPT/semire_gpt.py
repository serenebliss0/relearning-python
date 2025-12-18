"""
SemireGPT - A Custom AI Assistant

This is a starter implementation that demonstrates:
- API integration (currently using OpenAI as example)
- Basic chat interface
- Conversation history
- Extensible architecture for future enhancements

TODO: Replace with your own AI implementation
Current status: API call to ChatGPT (to be enhanced)
"""

import os
import json
from datetime import datetime


class SemireGPT:
    """Main class for SemireGPT AI assistant"""
    
    def __init__(self, api_key=None):
        """
        Initialize SemireGPT
        
        Args:
            api_key: API key for the AI service (optional)
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.conversation_history = []
        self.system_prompt = "You are SemireGPT, a helpful AI assistant."
    
    def add_to_history(self, role, content):
        """Add a message to conversation history"""
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        }
        self.conversation_history.append(message)
    
    def get_response(self, user_message):
        """
        Get AI response to user message
        
        Args:
            user_message: The user's input message
            
        Returns:
            AI response string
        """
        # Add user message to history
        self.add_to_history("user", user_message)
        
        # TODO: Replace this with your custom AI implementation
        # For now, this is a placeholder that shows the structure
        
        # Simulated response (replace with actual AI call)
        ai_response = self._simulate_response(user_message)
        
        # Add AI response to history
        self.add_to_history("assistant", ai_response)
        
        return ai_response
    
    def _simulate_response(self, message):
        """
        Simulate an AI response (placeholder for actual implementation)
        
        In the future, replace this with:
        - Custom trained model
        - Fine-tuned LLM
        - RAG (Retrieval-Augmented Generation)
        - Your own AI architecture
        """
        # Simple rule-based responses for demonstration
        message_lower = message.lower()
        
        if "hello" in message_lower or "hi" in message_lower:
            return "Hello! I'm SemireGPT. How can I help you today?"
        elif "how are you" in message_lower:
            return "I'm functioning well, thank you! How can I assist you?"
        elif "what can you do" in message_lower or "help" in message_lower:
            return ("I'm SemireGPT, currently in development. "
                   "I can have basic conversations, but I'm being enhanced "
                   "to become a fully custom AI assistant!")
        elif "name" in message_lower:
            return "My name is SemireGPT - a custom AI being developed!"
        else:
            return (f"I heard you say: '{message}'. "
                   f"I'm still learning and improving my responses!")
    
    def save_conversation(self, filename="conversation_history.json"):
        """Save conversation history to a file"""
        with open(filename, "w") as f:
            json.dump(self.conversation_history, f, indent=2)
        print(f"Conversation saved to {filename}")
    
    def load_conversation(self, filename="conversation_history.json"):
        """Load conversation history from a file"""
        try:
            with open(filename, "r") as f:
                self.conversation_history = json.load(f)
            print(f"Conversation loaded from {filename}")
        except FileNotFoundError:
            print(f"No conversation file found at {filename}")
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        print("Conversation history cleared")
    
    def display_history(self):
        """Display the conversation history"""
        print("\n=== Conversation History ===")
        for msg in self.conversation_history:
            role = msg["role"].capitalize()
            content = msg["content"]
            print(f"\n{role}: {content}")
        print("\n" + "="*30)


def main():
    """Main function to run SemireGPT in interactive mode"""
    print("="*50)
    print("Welcome to SemireGPT!")
    print("="*50)
    print("\nA custom AI assistant in development")
    print("Type 'quit' to exit")
    print("Type 'history' to see conversation history")
    print("Type 'clear' to clear history")
    print("Type 'save' to save conversation")
    print("="*50)
    
    # Initialize SemireGPT
    gpt = SemireGPT()
    
    # Main conversation loop
    while True:
        try:
            # Get user input
            user_input = input("\nYou: ").strip()
            
            # Handle commands
            if user_input.lower() == "quit":
                print("\nThank you for using SemireGPT! Goodbye!")
                break
            elif user_input.lower() == "history":
                gpt.display_history()
                continue
            elif user_input.lower() == "clear":
                gpt.clear_history()
                continue
            elif user_input.lower() == "save":
                gpt.save_conversation()
                continue
            elif not user_input:
                continue
            
            # Get and display AI response
            response = gpt.get_response(user_input)
            print(f"\nSemireGPT: {response}")
            
        except KeyboardInterrupt:
            print("\n\nInterrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
