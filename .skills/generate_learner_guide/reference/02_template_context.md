# Learner Guide Template Context

## Purpose

Documents the context fields extracted from the Course Proposal and used to populate the Learner Guide DOCX template.

## Context Structure

### Course Information

| Field | Source | Description |
|-------|--------|-------------|
| `Course_Title` | Course Proposal | Full course name |
| `Name_of_Organisation` | User selection | Training provider name |
| `UEN` | Organization database | Unique Entity Number |
| `company_logo` | Logo directory | Organization logo image |

### AI-Generated Content

| Field | Source | Description |
|-------|--------|-------------|
| `Course_Overview` | AI Agent | 90-100 word course introduction |
| `LO_Description` | AI Agent | 45-50 word learning outcome summary |

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

## Template Placeholders

The DOCX template uses Jinja2 syntax for variable substitution:

```
{{ Course_Title }}
{{ Course_Overview }}
{{ LO_Description }}
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
{% endfor %}

{% for summary in Assessment_Summary %}
    {{ summary.LO }}
    {{ summary.Assessment_Methods }}
{% endfor %}
```
