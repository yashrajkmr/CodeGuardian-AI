import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Create an instance of the FastAPI class
app = FastAPI()

# Initialize the OpenAI client with the API key from the .env file
# It's a good practice to handle the case where the key might be missing.
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not found.")
client = OpenAI(api_key=api_key)


# Define the structure of the request body using Pydantic
# This ensures that any data sent to this endpoint matches this structure.
class CodeReviewRequest(BaseModel):
    code: str
    language: str


# This is our original root endpoint, good for checking if the server is running.
@app.get("/")
def read_root():
    return {"message": "CodeGuardian AI is alive!"}


# This is our new, more advanced endpoint for code reviews.
# It uses a POST request because the client is sending data (the code) to the server.
@app.post("/review-code")
async def review_code(request: CodeReviewRequest):
    # Here we use the "Meticulous Bug Hunter Prompt" we designed earlier.
    prompt = f"""
    ### ROLE ###
    You are a Principal Software Engineer at Google, known for your ability to find subtle bugs and edge cases that others miss. Your tone is constructive but direct.

    ### OBJECTIVE ###
    Your sole objective is to identify potential bugs, logical fallacies, and unhandled edge cases in the provided {request.language} code.

    ### LAYOUT ###
    Provide your feedback in a Markdown table with columns: Severity, Line Number(s), Issue, and Suggestion. If no bugs are found, you MUST return the single phrase: "No bugs found."

    ### STRAINTS ###
    - Do not comment on code style, formatting, or performance.
    - Focus exclusively on bugs and correctness.

    ### CODE TO REVIEW ###
    ```
    {request.code}
    ```
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Or "gpt-3.5-turbo" for faster, cheaper responses
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2 # Lower temperature for more deterministic, factual output
        )
        review_content = response.choices[0].message.content
        return {"review": review_content}
    except Exception as e:
        # It's important to handle potential errors from the API call.
        return {"error": f"An error occurred: {str(e)}"}
    
    # This block allows us to run the server directly by running this Python file.
# It's a standard practice for Python applications.
if __name__ == "__main__":
    import uvicorn
    # We run the server programmatically here.
    # Uvicorn will still use its reloader because we are in a dev environment.
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)