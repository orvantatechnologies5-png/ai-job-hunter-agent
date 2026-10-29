import json
from anthropic import Anthropic

client = Anthropic()  # ANTHROPIC_API_KEY environment variable se key leta hai
MODEL = "claude-sonnet-5-5"


def ask(system, prompt, max_tokens=1500):
    """Claude se ek sawal poocho aur text jawab lo."""
    msg = client.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text


def ask_json(system, prompt):
    """Jawab sirf JSON mein mangwao aur Python dict bana do."""
    text = ask(system + "\nReply with valid JSON only. No extra text.", prompt)
    start, end = text.find("{"), text.rfind("}")
    return json.loads(text[start:end + 1])


# ---------- Agent 1: Planner ----------
def planner(goal, cv):
    system = "You are a career planner. You turn a job seeker's goal and CV into a clear search plan."
    prompt = f"""Goal: {goal}

CV:
{cv}

Return JSON with these keys:
"target_roles": list of 2-4 job titles to search for,
"must_have_skills": list of skills from the CV that matter most,
"min_score": number 0-100, the lowest match score worth applying to,
"steps": list of short steps the team will follow."""
    return ask_json(system, prompt)


# ---------- Agent 2: Scout ----------
def scout(plan, cv, jobs):
    system = "You are a job scout. You compare jobs with a CV and score how well each one matches."
    prompt = f"""Plan: {json.dumps(plan)}

CV:
{cv}

Jobs:
{json.dumps(jobs)}

Score every job from 0 to 100 for this candidate.
Return JSON: {{"matches": [{{"id": job id, "score": number, "reason": one short sentence}}]}}"""
    result = ask_json(system, prompt)
    return sorted(result["matches"], key=lambda m: m["score"], reverse=True)


# ---------- Agent 3: Writer ----------
def writer(plan, cv, job):
    system = "You are a cover letter writer. You write short, specific, honest cover letters."
    prompt = f"""Job:
{json.dumps(job)}

CV:
{cv}

Key skills to highlight: {", ".join(plan["must_have_skills"])}

Write a cover letter under 180 words. Only use facts from the CV. No made-up experience."""
    return ask(system, prompt, max_tokens=800)
