## **Step 3: Write the Code**

### **1. Create the Questions in `questions.py`**

# First, we define the questions and options in a structured format. A list of dictionaries works well for this:

# questions.py
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Lisbon"], 
        "answer": "Paris",
        },
        {
            "question":"What is 5 + 3?",
            "options": ["6", "7", "8", "9"],
            "answer": "8"
        },
        {
            "question": "Which language is this quiz written in?",
            "options": ["Python", "Java", "C++", "Ruby"],
            "answer": "Python"
        }
    ]