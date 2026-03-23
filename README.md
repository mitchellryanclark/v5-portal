# V5.5 Context Reinforcer

V5.5 Context Reinforcer is a lightweight Flask web application designed to help you seamlessly transition complex AI chat sessions (like with Gemini or ChatGPT) without losing crucial context or leaking sensitive information.

It generates a highly structured "Project Handoff" prompt that acts as a state object, ensuring the next AI session picks up exactly where the last one left off while maintaining your active goals.

## New in V5.5
- **Extracted Prompt Template:** The massive prompt logic has been extracted from `app.py` into a standalone `prompt_template.txt` file for easier viewing and editing.
- **Robust UI Error Handling:** Improved frontend and backend error passing so the UI reports when the template is missing or the priority is empty.
- **Enhanced Clipboard Compatibility:** Includes a robust fallback mechanism for older browsers and local non-HTTPS setups.
- **Accessibility Improvements:** Added ARIA labels and live regions for better screen reader compatibility.

## Features

- **Context Preservation**: Generates a comprehensive prompt wrapping your current goals and project state.
- **Security Guidelines**: Contains instructions for the AI to redact secrets, PII, and maintain data security boundaries.
- **Modern UI**: A sleek, dark-mode user interface styled effortlessly with Tailwind CSS.
- **One-Click Copy**: Easily generate and copy the reinforcement prompt to your clipboard with a seamless UX.

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, Tailwind CSS, Vanilla JavaScript

## Application Structure
- `app.py`: The main Flask backend application containing simple API logic.
- `prompt_template.txt`: The massive prompt shell logic that will receive the seed phrase.
- `templates/index.html`: The modern Tailwind UI page.

## Prerequisites

- Python 3.x
- `pip` (Python package manager)

## Installation & Setup

1. **Navigate to the project directory**:
   ```bash
   cd v5-portal
   ```

2. **Install dependencies**:
   This project requires Flask. If you haven't installed it yet, install it via pip:
   ```bash
   pip install flask
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the App**:
   Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

1. Open the application in your browser.
2. Enter a "seed phrase" that captures your immediate priority or the current goal for the next stage of your project (e.g., "Implement the user authentication flow").
3. Click **Compile Reinforcement** to generate the context extraction prompt.
4. Click **Copy & Reinforce** to copy this massive extraction prompt to your clipboard.
5. **Paste this prompt into your CURRENT, long-running AI chat** (the one containing all your existing project history and context). The AI will analyze its own conversation history, redact sensitive data, and generate a highly structured "Project Handoff" packet.
6. Copy *that* resulting packet and paste it as the very first message into a **BRAND NEW AI session** to initialize it with all your preserved project context.

## Modifying the Prompt
To change the output behavior of the reinforcer, simply edit the `prompt_template.txt` file. Make sure to retain the `{seed_phrase}` variable where you want the active priority to inject.

## License

This project is open-source and available under the [MIT License](LICENSE).
