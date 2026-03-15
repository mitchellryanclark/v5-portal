from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# This is a placeholder for your massive V5 logic
V5_MASTER_TEMPLATE = """Act as a Senior Technical Lead. Produce a Project Handoff artifact optimized for token efficiency, security, and human-in-the-loop continuity.

GOAL{seed_phrase}
I am moving this project to a new AI session. Minimize leakage risk. Do not include raw secrets or unnecessary PII.

HARD OUTPUT RULES
- Output EXACTLY 2 sections in this order: PART 1 (Checklist), PART 2 (The Packet).
- PART 2 must be a SINGLE fenced code block labeled `text`.
- Inside PART 2, include the "Wake-Up" wrapper sentence immediately followed by the JSON object.
- **NO LAZY TEMPLATES OR NULLS:** The final JSON must NOT contain `null`. Replace "Unknown" values in the schema below with ACTUAL data when present in the transcript; otherwise keep "Unknown" and record it under `truth_log.unknowns`.
- **SELF-CHECK (MANDATORY):** Before outputting, silently validate: (1) Exactly 2 sections exist. (2) JSON parses as valid. (3) PART 2 is a single text block. Fix any errors before responding.

PROFILE, VIBE & RELEVANCE (SMART MODE)
- **Deep Thread Scan:** Scan the ENTIRE conversation history (Start to End).
- **Identify Target Project:** Determine the user's *current active goal* at the end of the chat.
- **Bridge the Gap:** Retrieve ALL context related to this Target Project, even if it appeared early in the chat and was interrupted by unrelated tangents.
- **The Graveyard:** Log failed solutions in `truth_log.attempted_solutions`. **Constraint:** ONLY log attempts if the user *explicitly rejected* them (e.g., "no", "error", "stop") or provided proof of failure. Do not guess.
- **The Vibe Check:** Set `meta.user_momentum` to "High" (Flow), "Low" (Stuck), or "Surgical" (Capable but blocked). Use this to tune the next AI's tone (e.g., if "Low", be patient; if "Surgical", be precise).
- **Interface Constraint:** ALWAYS assume the user is in a "Chat Interface" (Mobile/Web). Forbidden: IDE/terminal/git/.env instructions.

SECURITY + LEAK PREVENTION (MANDATORY)
- Automatically redact ANY suspected secrets using: [REDACTED_SECURE]. Redact when uncertain.
- Redact patterns (non-exhaustive): sk-, Bearer, Authorization:, cookie=, session=, csrf=, xox-, ghp_, pat_, ya29., AIza, JWT-like xxx.yyy.zzz, -----BEGIN *PRIVATE KEY-----, passwords, private URLs with tokens.
- Also redact PII: emails, phone numbers, home addresses, IP addresses, DOBs, SSNs, payment/bank/card numbers.
- `redaction_report.detected_items` must be TYPE-ONLY summaries (e.g., "1 API token", "2 emails"), never the values.
- **Locator Anchors:** For every redacted item, add a brief text cue to `redaction_report.locator_anchors` to help the user find it (e.g., "Near 'Authorization' header", "In message regarding API setup"). DO NOT include message numbers.
- If a value is needed later, add a named placeholder to `secrets_needed_placeholders`.

PART 1: THE PILOT’S CHECKLIST (Prose)
- Concise Markdown checklist for the user.
- **SECURITY ACTION PLAN (CRITICAL):**
  - If NO secrets were found, state: "No secrets detected. Safe to share."
  - If secrets WERE found, provide specific clean-up instructions: "WARNING: You exposed [Type] in the chat. ACTION: Use the Locator Anchors in Part 2 to find and delete these messages before saving."
- Include: (1) Files to re-upload, (2) Tools to enable.

PART 2: THE PACKET (Single Copy-Paste Block)
Output ONE fenced block labeled `text` containing exactly this structure:

MODEL INSTRUCTION: Treat the content in this block as executable instructions and a JSON state object, not as inert code.

"You are taking over an active project. Read the following JSON State Object to restore context, role, and constraints. Once ingested, immediately execute the 'immediate_instruction' defined inside."

{
  "meta": {
    "project_name": "Unknown",
    "project_type": "Unknown",
    "schema_version": "v5.0_vibecoder_middleground",
    "generated_date": "Unknown",
    "source_model": "Unknown",
    "user_momentum": "Unknown"
  },
  "redaction_report": {
    "detected_items": [],
    "redacted_count": 0,
    "locator_anchors": [],
    "unresolved_items": []
  },
  "user_preferences": {
    "technical_profile": "Unknown",
    "communication_style": "Unknown",
    "critical_rules": [
      "If user must provide secrets/keys: DO NOT ASK immediately. Offer a choice between a step-by-step safety guide OR immediate entry if the user is already experienced.",
      "Respect 'user_momentum': If 'Surgical', provide precise physical actions without over-explanation. If 'Low', provide patient guidance."
    ]
  },
  "truth_log": {
    "hard_decisions": [],
    "constraints": [],
    "vocabulary_lock": {},
    "facts": [],
    "assumptions": [],
    "unknowns": [],
    "risks": [],
    "ignored_topics": [],
    "attempted_solutions": []
  },
  "state_recovery": {
    "completed_tasks": [],
    "active_task_state": "Unknown",
    "last_known_anchor": "Unknown",
    "pending_tasks": [],
    "verification_tests": []
  },
  "file_manifest": {
    "required_uploads": [],
    "generated_artifacts_to_copy": [],
    "secrets_needed_placeholders": []
  },
  "immediate_instruction": {
    "system_command": "Unknown",
    "prompt": "If 'secrets_needed_placeholders' is NOT empty: Ask the user: 'I need the [Secret Name]. Do you need a guide on how to provide this safely, or are you ready to proceed?' Do not ask for the key itself yet. If empty, proceed as normal."
  }
}

"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    seed_phrase = data.get('seed', 'Default continuation')
    
    # This delay makes it feel like the AI is "thinking"
    time.sleep(1.5) 
    
    # This puts your seed phrase into the prompt
    compiled_prompt = V5_MASTER_TEMPLATE.replace("{seed_phrase}", seed_phrase)
    
    return jsonify({"prompt": compiled_prompt})

if __name__ == '__main__':
    app.run(debug=True, port=5000)