import json
import os
from agents import planner, scout, writer

goal = "Mujhe remote Python developer ki job chahiye"
cv = open("cv.txt", encoding="utf-8").read()
jobs = json.load(open("jobs.json", encoding="utf-8"))

# Step 1: Planner plan banata hai
plan = planner(goal, cv)
print("PLAN:", json.dumps(plan, indent=2))

# Step 2: Scout jobs ko score karta hai
matches = scout(plan, cv, jobs)
top = [m for m in matches if m["score"] >= plan["min_score"]][:3]
print(f"\n{len(top)} jobs match hui:")
for m in top:
    print(f"  #{m['id']}  {m['score']}%  {m['reason']}")

# Step 3: Writer har top job ke liye cover letter likhta hai
os.makedirs("output", exist_ok=True)
for m in top:
    job = next(j for j in jobs if j["id"] == m["id"])
    letter = writer(plan, cv, job)
    path = f"output/job_{job['id']}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {job['title']} - {job['company']}\n\n")
        f.write(f"Match: {m['score']}% - {m['reason']}\n\n{letter}\n")
    print("Saved:", path)
