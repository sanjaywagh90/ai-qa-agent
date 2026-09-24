
## 🚀 How to Run

1. Set up the database:
```bash
python setup_db.py
```

2. (Optional) Add extra field requirements:
```bash
python add_requirements.py
```

3. Run the full agent and generate the Excel report:
```bash
python lesson11.py
```

This creates `Test_Case_Report.xlsx` with all generated test cases.

## 📚 Concepts Covered

- AI Agent architecture (Role, Tools, Input, Output)
- Tool registry and dynamic tool selection
- SQL integration with Python (`sqlite3`)
- Excel report generation (`openpyxl`)
- Rule-based logic as a foundation for future AI-model integration
- Git & GitHub version control

## 🔮 Next Steps

- Integrate a real AI model (OpenAI API) to replace rule-based logic
- Add more field types (checkbox, radio button, file upload)
- Add a simple UI to trigger report generation

## 👤 Author

Built by [Sanjay Wagh](https://github.com/sanjaywagh90) while learning AI Agent development from scratch, step by step.
