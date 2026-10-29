# AI Job Hunter Agent (Multi-Agent System in Python)

Orvanta Technologies — MCP / AI Agents Series

3 AI agents ki team jo aap ke liye job dhoondti hai:

1. **Planner** — aap ka goal aur CV parh kar plan banata hai (roles, skills, min score)
2. **Scout** — har job ko CV se match karke 0–100 score deta hai
3. **Writer** — top jobs ke liye CV ke asli facts se cover letter likhta hai

## Files

| File | Kaam |
|------|------|
| `agents.py` | Teeno agents (Planner, Scout, Writer) |
| `main.py` | Team ko chalata hai |
| `jobs.json` | Sample jobs (apni jobs yahan daalein) |
| `cv.txt` | Aap ki CV (isay apni details se badlein) |

## Chalane ka tareeqa

```bash
pip install -r requirements.txt

# Mac / Linux
export ANTHROPIC_API_KEY="your-key-here"
# Windows (PowerShell)
setx ANTHROPIC_API_KEY "your-key-here"

python main.py
```

Result `output/` folder mein aayega: har top job ki ek `.md` file, jismein match score aur cover letter hoga.

## Note

- API key kabhi code mein na likhein.
- `jobs.json` ki companies sample hain.
- Apply karne se pehle har cover letter khud zaroor parhein.
