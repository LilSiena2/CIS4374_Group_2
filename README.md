# CIS4374_Group_2
Project Management group project 

Project Topic: 

Our project aims to develop an application that can scan our client’s alteration tickets and utilize AI to parse the data into a database. This data can then be used to track trends and extract insights, such as identifying the most profitable alterations, work-in-progress (WIP) items, or the most common alteration requests. Additionally, the digital scan will serve as a backup and archive of the physical copies in case they are lost.

Frontend (User Interface):
    Framework: React (for a responsive and user-friendly interface)
    UI Library: Tailwind CSS (for quick styling)
    Document Upload: FilePond or similar library for handling image uploads

Backend (Logic & API Services):
    Framework: Python (Flask or FastAPI for REST API)
    OCR/NLP: Tesseract OCR (for text extraction) and spaCy (for data parsing)
    AI Integration: OpenAI API or local LLM for advanced parsing

Database (Data Storage):
    Database Type: MySQL (for structured ticket storage)
    Cloud Storage: AWS S3 (for storing scanned images as backups)
    Tools & Deployment

Version Control: GitHub (for collaboration and version tracking)

Project Management: Microsoft Project (for tracking milestones)

Deployment: Docker (for containerized deployment) and AWS (for hosting)