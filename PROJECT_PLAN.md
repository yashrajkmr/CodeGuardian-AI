# CodeGuardian AI: Project Plan & Status

This document tracks the development progress, roadmap, and key decisions for the CodeGuardian AI project.

---
### ## Current Status (As of Oct 3, 2025)

- **Module 0: Setup:** COMPLETE.
  - Pivoted from a local environment to GitHub Codespaces due to local system corruption.
  - Professional environment with Python, Docker, and Node.js is fully configured.

- **Module 1: Core Engine:** IN PROGRESS.
  - Basic FastAPI server is built and running (`main.py`).
  - `.env` file is set up for API key management.
  - Endpoint for AI calls (`/review-code`) is created and tested.
  - **Blocker:** OpenAI account has an `insufficient_quota` error. Billing needs to be set up to proceed with real AI calls.

- **Module 3: Frontend Setup:** IN PROGRESS.
  - React + Vite project created in the `frontend` directory.
  - Default development server is running successfully.

---
### ## Project Roadmap

1.  **Module 2: Expand the AI Core:**
    - [ ] Implement Security & Performance prompts.
    - [ ] Create a final "Lead Engineer" synthesis prompt.

2.  **Module 3: Build the Frontend UI:**
    - [ ] Build React components (input, button, output display).
    - [ ] Connect the UI to the backend API.
    - [ ] Use "mock" data until the billing issue is resolved.

3.  **Module 4: GitHub App Integration:**
    - [ ] Create an official GitHub App.
    - [ ] Build a webhook handler in the backend.
    - [ ] Automate reviews on Pull Requests.

4.  **Module 5: Deployment & Polish:**
    - [ ] Deploy the backend to a cloud service (e.g., AWS).
    - [ ] Deploy the frontend to a cloud service (e.g., Vercel).
    - [ ] Finalize the main `README.md` with links and documentation.

---
### ## Immediate Next Step

- Begin building the UI components in React inside the `frontend` folder.