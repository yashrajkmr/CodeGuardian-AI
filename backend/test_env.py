import os
from dotenv import load_dotenv

print("--- Running Environment Test ---")

# Try to load the .env file
load_dotenv()
print("Attempted to load .env file.")

# Try to get the API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

if api_key and api_key != "sk-...":
    # To protect your key, we'll only show the first and last parts
    print("✅ SUCCESS: API Key found!")
    print(f"   Key starts with: {api_key[:5]}")
    print(f"   Key ends with:   {api_key[-4:]}")
else:
    print("❌ FAILED: OPENAI_API_KEY not found or is still the placeholder.")
    print("   Please open your .env file and ensure the variable name is correct and you have pasted your real key.")

print("--- Test Finished ---")