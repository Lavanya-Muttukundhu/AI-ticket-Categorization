backend in cmd --py main.py
frontend in cmd -- streamlit run app.py
AI-Powered Ticket Creation & Categorization System Project Overview This project is part of an Agile Internship focused on building an automated support system. The application captures user-reported issues, analyzes the text using Natural Language Processing (NLP), and automatically categorizes the ticket and assigns a priority level.

🚀 Accomplishments: Milestones 1 & 2 Milestone 1: Core Ticket Engine Source Code Structure: Established a professional project directory using a /src and /docs architecture.

Ticket Generation: Developed logic to generate unique Ticket IDs using the uuid library.

Metadata Tracking: Every ticket is automatically stamped with a Date/Time and an initial status of "Open".

Local Storage: Implemented a system to save every generated ticket as a .json file in a dedicated /tickets folder for data persistence.

Milestone 2: AI & NLP Integration NLP Text Normalization: Integrated Lemmatization techniques to convert user words to their root form (e.g., "crashing" → "crash"), improving categorization accuracy.

Sentiment Analysis: Integrated the TextBlob library to analyze user frustration.

Negative Sentiment (< -0.3): Automatically triggers an "Urgent" priority.

Categorization Logic: Developed a classifier that maps user intent to categories like Technical Issue, Access & Security, and Billing.

Error Handling: Added validation to ensure descriptions meet a minimum length requirement, preventing empty or vague tickets.

📂 Project Structure Plaintext

AI-CAREER-TICKET/ ├── docs/ # Agile Trackers (Backlog, Unit Tests, Defect Tracker) ├── src/ # Python Source Code │ ├── main.py # Entry point for the application │ └── classifier.py # AI & NLP Logic (Lemmatization & Sentiment) ├── tickets/ # Generated ticket data (JSON files) ├── requirements.txt # Project dependencies └── README.md # Project documentation 🛠️ Agile Documentation As per project requirements, the following Agile documents are maintained in the /docs folder:

Product Backlog: All user stories and MoSCoW prioritization.

Sprint Backlog: Task-level breakdown with estimated effort (0.5 - 12 hours).

Unit Test Plan: 50+ test cases covering valid/invalid inputs and AI logic accuracy.

Defect Tracker: Log of technical bugs (e.g., Git index locks, validation errors) and their resolutions.

Retrospective: Notes on "Start, Stop, and Continue" for team improvement.

How to Run Install Dependencies:

DOS

pip install -r requirements.txt Execute Application:

DOS

python src/main.py Follow the Prompts: Enter your support issue when asked, and check the tickets/ folder for the output.

