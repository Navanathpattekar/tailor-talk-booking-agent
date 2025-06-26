@echo off
cd /d %~dp0

:: Activate virtual environment
call venv\Scripts\activate.bat

:: Start FastAPI backend in new terminal
start cmd /k "uvicorn app.main:app --reload"

:: Wait for backend to boot
timeout /t 2

:: Start Streamlit
cd streamlit_ui
streamlit run chat_ui.py
