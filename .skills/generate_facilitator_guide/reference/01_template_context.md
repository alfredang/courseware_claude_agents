# Facilitator Guide Template Context

## Purpose

Documents the context fields extracted from the Course Proposal and used to populate the Facilitator Guide DOCX template.

## Context Structure

### Course Information

| Field | Source | Description |
|-------|--------|-------------|
| `Course_Title` | Course Proposal | Full course name |
| `Name_of_Organisation` | User selection | Training provider name |
| `UEN` | Organization database | Unique Entity Number |
| `company_logo` | Logo directory | Organization logo image |

### TSC (Training Skills Competency) Fields

| Field | Source | Description |
|-------|--------|-------------|
| `TSC_Code` | Course Proposal | Technical Skills Competency code (e.g., LOG-XXX-XXXX-1.1) |
| `TSC_Title` | Course Proposal | TSC competency title |
| `TSC_Category` | Derived from TSC Code | Sector category (e.g., Logistics) |
| `TSC_Sector_Abbr` | Derived from TSC Code | Full Skills Framework name |
| `TSC_Description` | Course Proposal / Auto-generated | TSC description text |
| `Skills_Framework` | Derived from TSC Code | Full Skills Framework name |
| `Proficiency_Level` | Extracted from TSC Code | Level designation (e.g., Level 1) |
| `Proficiency_Description` | Course Proposal / Auto-generated | Description of proficiency requirements |

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
{{ TSC_Code }}
{{ TSC_Title }}
{{ TSC_Category }}
{{ TSC_Sector_Abbr }}
{{ Skills_Framework }}
{{ Proficiency_Level }}
{{ Proficiency_Description }}
{{ Name_of_Organisation }}
{{ UEN }}
{{ company_logo }}

{% for lu in Learning_Units %}
    {{ lu.LU_Title }}
    {{ lu.LO }}
    {% for k in lu.K_numbering_description %}
        {{ k.K_number }}: {{ k.Description }}
    {% endfor %}
    {% for a in lu.A_numbering_description %}
        {{ a.A_number }}: {{ a.Description }}
    {% endfor %}
    {% for topic in lu.Topics %}
        {{ topic.Topic_Title }}
        {% for point in topic.Bullet_Points %}
            {{ point }}
        {% endfor %}
    {% endfor %}
{% endfor %}
```
