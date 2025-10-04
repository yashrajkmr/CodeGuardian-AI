import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware  # <-- NEW IMPORT

load_dotenv()

app = FastAPI()

# vvvvvvvvvvvvvvvvvvvvvvvv NEW CORS MIDDLEWARE vvvvvvvvvvvvvvvvvvvvvvvv
# This block tells our backend to accept requests from any origin.
# The "*" is a wildcard, which is fine for development.
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ^^^^^^^^^^^^^^^^^^^^^^^^ END OF NEW CODE ^^^^^^^^^^^^^^^^^^^^^^^^^^^

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not found.")
client = OpenAI(api_key=api_key)

class CodeReviewRequest(BaseModel):
    code: str
    language: str

@app.get("/")
def read_root():
    return {"message": "CodeGuardian AI is alive!"}

@app.post("/review-code")
async def review_code(request: CodeReviewRequest):
    # We are still using our mock response for now
    print(f"Received request to review {request.language} code.")
    mock_review_text = """
| Severity | Line Number(s) | Issue                                     | Suggestion                               |
|:---------|:---------------|:------------------------------------------|:-----------------------------------------|
| Critical | 2              | Incorrect Type Operation                  | You cannot add a string to a number.     |
| Low      | 1              | Inconsistent Naming                       | Function name should follow camelCase.   |
    """
    return {"review": mock_review_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)