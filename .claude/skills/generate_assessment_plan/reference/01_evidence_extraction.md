# Assessment Evidence Extraction Agent

## Purpose

Extracts structured assessment evidence data from course details using AI. Generates justifications for assessment methods including type of evidence, submission method, marking process, and retention period.

## Agent Role

Evidence Extraction Agent - Generates assessment evidence gathering plan

## System Prompt

```
Based on the following course details, you are to provide structured justifications for the selected Assessment Methods, aligning them with Learning Outcomes (LOs) and Topics.

**Course Details:**
- **Course Title:** {Course_Title}
- **Learning Outcomes:**
{Learning Outcomes from all Learning Units}
- **Topics Covered:** {Extracted topics and bullet points}
- **Assessment Methods:** {List of method abbreviations}

---

**Your Task:**
- Generate structured justifications for these applicable assessment methods:
- **CS (Case Study)**
- **PP (Practical Performance)**
- **OQ (Oral Questioning)**
- **RP (Role Play)**

- For each assessment method, extract the following:
1. **Type of Evidence**: The specific evidence candidates will submit.
2. **Manner of Submission**: How candidates submit their work.
3. **Marking Process**: The evaluation criteria used by assessors.
4. **Retention Period**: The storage duration for submitted evidence.

---

**Rules:**
- Replace "students" with "candidates."
- Replace "instructors" with "assessors."
- Ensure all **LOs** are addressed.
- **Limit word length**:
- Bullet points: Max 30 words.
- Marking Process: Max 6 words per evaluation.
- **Format must be consistent**:
- **PP, CS and OQ:** Evidence must be in a list of LOs.
- **RP:** Special handling with "No. of Role Play Scripts."

You must return valid JSON with this structure:
{
    "assessment_methods": {
        "PP": {
            "evidence": ["LO1: ...", "LO2: ..."],
            "submission": ["..."],
            "marking_process": ["..."],
            "retention_period": "..."
        },
        "CS": {
            "evidence": ["LO1: ...", "LO2: ..."],
            "submission": ["..."],
            "marking_process": ["..."],
            "retention_period": "..."
        },
        "OQ": {
            "evidence": ["LO1: ..."],
            "submission": ["..."],
            "marking_process": ["..."],
            "retention_period": "..."
        },
        "RP": {
            "evidence": "Role Play",
            "submission": ["..."],
            "marking_process": ["..."],
            "retention_period": "...",
            "no_of_scripts": "..."
        }
    }
}
```

## User Task

```
Your task is to generate the assessment evidence gathering plan.
Return the data as a valid JSON object.
```

## Output Schema

```json
{
    "assessment_methods": {
        "PP": {
            "evidence": [
                "LO1: Candidates will demonstrate practical application of...",
                "LO2: Candidates will perform hands-on exercises showing..."
            ],
            "submission": [
                "Candidates will submit completed practical work via digital portfolio."
            ],
            "marking_process": [
                "Technical accuracy of work.",
                "Application of procedures.",
                "Quality of final output."
            ],
            "retention_period": "All submitted evidence will be retained for 3 years from assessment date."
        },
        "CS": {
            "evidence": [
                "LO1: Candidates will analyze case scenarios demonstrating...",
                "LO2: Candidates will provide written analysis of..."
            ],
            "submission": [
                "Candidates will submit case study reports electronically."
            ],
            "marking_process": [
                "Depth of analysis.",
                "Application of concepts.",
                "Quality of recommendations."
            ],
            "retention_period": "All case study reports will be retained for 3 years from assessment date."
        },
        "OQ": {
            "evidence": [
                "LO1: Candidates will verbally demonstrate understanding of..."
            ],
            "submission": [
                "Assessors will record responses during structured questioning session."
            ],
            "marking_process": [
                "Accuracy of responses.",
                "Depth of understanding.",
                "Clarity of explanation."
            ],
            "retention_period": "All recordings and notes retained for 2 years from assessment date."
        },
        "RP": {
            "evidence": "Role Play",
            "submission": [
                "Assessor will evaluate using observation checklist during live role play."
            ],
            "marking_process": [
                "Effectiveness of approach.",
                "Application of techniques.",
                "Communication skills."
            ],
            "retention_period": "Observation checklists retained for 3 years from assessment date.",
            "no_of_scripts": "Minimum of two distinct role-play scripts covering different scenarios."
        }
    }
}
```

## Key Rules

- Replace "students" with "candidates"
- Replace "instructors" with "assessors"
- Address ALL Learning Outcomes in evidence
- Bullet points: Max 30 words each
- Marking Process: Max 6 words per evaluation (3 evaluations total)
- PP, CS, OQ: Evidence as list of LO-specific items
- RP: Special handling with "no_of_scripts" field
- Retention period typically 3 years (2 years for OQ)
