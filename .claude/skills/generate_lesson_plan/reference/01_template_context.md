# Lesson Plan Template Context

## Purpose

Documents the context fields extracted from the Course Proposal and used to populate the Lesson Plan DOCX template.

## Context Structure

### Course Information

| Field | Source | Description |
|-------|--------|-------------|
| `Course_Title` | Course Proposal | Full course name |
| `Name_of_Organisation` | User selection | Training provider name |
| `UEN` | Organization database | Unique Entity Number |
| `company_logo` | Logo directory | Organization logo image |

### Learning Units Array

```json
{
    "Learning_Units": [
        {
            "LU_Title": "Learning Unit 1: Introduction to Topic",
            "LO": "Full learning outcome description",
            "Topics": [
                {
                    "Topic_Title": "Topic 1: Fundamentals",
                    "Bullet_Points": ["Point 1", "Point 2", "Point 3"]
                }
            ],
            "K_numbering_description": [
                {"K_number": "K1", "Description": "Knowledge statement 1"}
            ],
            "A_numbering_description": [
                {"A_number": "A1", "Description": "Ability statement 1"}
            ],
            "Assessment_Methods": ["Written Assessment", "Practical Performance"],
            "Assessment_Methods_Abbr": "WA-SAQ, PP",
            "Instructional_Methods": ["Lecture", "Demonstration", "Practical"]
        }
    ]
}
```

### Assessment Summary

```json
{
    "Assessment_Summary": [
        {
            "LO": "Full learning outcome description",
            "Assessment_Methods": "WA-SAQ, PP"
        }
    ]
}
```

### Version Control

| Field | Default | Description |
|-------|---------|-------------|
| `Rev_No` | "1.0" | Document revision number |
| `Effective_Date` | Current date | Date in "DD Mon YYYY" format |
| `Author` | "" | Author name (user input) |
| `Reviewed_By` | "" | Reviewer name (user input) |
| `Approved_By` | "" | Approver name (user input) |

## Assessment Method Abbreviations

| Full Name | Abbreviation |
|-----------|-------------|
| Written Assessment - Short Answer Questions | WA-SAQ |
| Written Assessment | WA |
| Practical Performance | PP |
| Case Study | CS |
| Oral Questioning | OQ |
| Role Play | RP |
| Project | PJ |
| Portfolio | PF |
| Observation | OB |

## Learning Unit Validation

Each Learning Unit is validated to ensure required fields:

```python
validated_lu = {
    "LU_Title": lu.get("LU_Title", f"Learning Unit {i+1}"),  # Default if missing
    "LO": lu.get("LO", ""),
    "Topics": lu.get("Topics", []),
    "K_numbering_description": lu.get("K_numbering_description", []),
    "A_numbering_description": lu.get("A_numbering_description", []),
    "Assessment_Methods": lu.get("Assessment_Methods", []),
    "Instructional_Methods": lu.get("Instructional_Methods", []),
}
```

### Topic Validation

```python
validated_topics = []
for topic in lu["Topics"]:
    if isinstance(topic, dict):
        validated_topics.append({
            "Topic_Title": topic.get("Topic_Title", ""),
            "Bullet_Points": topic.get("Bullet_Points", [])
        })
```

### K/A Statement Validation

```python
# K statements
validated_k = []
for k in lu["K_numbering_description"]:
    if isinstance(k, dict):
        validated_k.append({
            "K_number": k.get("K_number", ""),
            "Description": k.get("Description", "")
        })

# A statements
validated_a = []
for a in lu["A_numbering_description"]:
    if isinstance(a, dict):
        validated_a.append({
            "A_number": a.get("A_number", ""),
            "Description": a.get("Description", "")
        })
```

## Template Placeholders

The DOCX template uses Jinja2 syntax for variable substitution:

```
{{ Course_Title }}
{{ Name_of_Organisation }}
{{ UEN }}
{{ company_logo }}

{% for lu in Learning_Units %}
    {{ lu.LU_Title }}
    {{ lu.LO }}
    {% for topic in lu.Topics %}
        {{ topic.Topic_Title }}
        {% for point in topic.Bullet_Points %}
            {{ point }}
        {% endfor %}
    {% endfor %}
    {% for im in lu.Instructional_Methods %}
        {{ im }}
    {% endfor %}
    {{ lu.Assessment_Methods_Abbr }}
{% endfor %}

{% for summary in Assessment_Summary %}
    {{ summary.LO }}
    {{ summary.Assessment_Methods }}
{% endfor %}
```
