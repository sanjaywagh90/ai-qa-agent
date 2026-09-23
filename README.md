# AI QA Agent

An AI-powered QA Agent built in Python that reads requirements from a database and automatically generates positive and negative test cases for different field types (text, email, password).

## 🎯 What This Project Does

This agent demonstrates a complete AI Agent architecture:
- Fetches field requirements from a SQLite database
- Automatically selects the right tool based on field type
- Generates structured positive and negative test cases
- Produces a full test case report end-to-end

## 🏗️ Project Structure

| File | Description |
|------|-------------|
| `lesson1.py` – `lesson4.py` | Python basics, API concepts, OpenAI setup |
| `lesson5.py` – `lesson7.py` | Agent role, tools, and first Agent class |
| `lesson8.py` | Test case generation for multiple field types |
| `setup_db.py` | Creates and seeds the SQLite database |
| `lesson9.py` | SQL tool to fetch requirements from the database |
| `lesson10.py` | Full pipeline — Database + Tools + Agent combined |

## ⚙️ How It Works
