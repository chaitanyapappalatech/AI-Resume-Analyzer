from PyPDF2 import PdfReader

reader = PdfReader("resume.pdf.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text()

print(text)

skills = [
    "python",
    "sql",
    "git",
    "aws",
    "docker",
    "html",
    "css",
    "javascript"
]

resume_skills = []

for skill in skills:
    if skill in text.lower():
        resume_skills.append(skill)

print(resume_skills)

with open("Job_description.txt","r") as file:
    jd = file.read().lower()

    job_skills = []

for skill in skills:
    if skill in jd:
        job_skills.append(skill)

print(job_skills)

matched = set(resume_skills) & set(job_skills)

score = (
    len(matched) /
    len(job_skills)
) * 100

print("Match Score:", score)

missing = set(job_skills) - set(resume_skills)

print("Missing Skills:")

for skill in missing:
    print(skill)


print("\nSuggestions:")

for skill in missing:
    print(
        f"Learn {skill} to improve your resume."
    )