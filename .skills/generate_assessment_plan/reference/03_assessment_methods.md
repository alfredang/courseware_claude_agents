# Assessment Methods Data Models

## Purpose

Documents the data structures and models used for assessment methods in the Assessment Plan generation.

## Pydantic Models

### AssessmentMethod

```python
class AssessmentMethod(BaseModel):
    evidence: Union[str, List[str]]      # Evidence type/description
    submission: Union[str, List[str]]    # Submission method
    marking_process: Union[str, List[str]]  # Evaluation criteria
    retention_period: str                 # Storage duration
    no_of_scripts: Union[str, None] = None  # Optional - for RP only
```

### AssessmentMethods Container

```python
class AssessmentMethods(BaseModel):
    PP: Optional[AssessmentMethod] = None  # Practical Performance
    CS: Optional[AssessmentMethod] = None  # Case Study
    RP: Optional[AssessmentMethod] = None  # Role Play
    OQ: Optional[AssessmentMethod] = None  # Oral Questioning
```

### EvidenceGatheringPlan

```python
class EvidenceGatheringPlan(BaseModel):
    assessment_methods: AssessmentMethods
```

## Assessment Method Types

### WA-SAQ (Written Assessment - Short Answer Questions)

**Note**: WA-SAQ is hardcoded in the template and NOT processed by AI.

| Field | Value |
|-------|-------|
| Evidence | Handwritten or typed responses |
| Submission | Candidates submit answer sheets to assessor |
| Marking Process | Pre-defined marking rubric |
| Retention Period | 3 years |

### PP (Practical Performance)

| Field | Description |
|-------|-------------|
| Evidence | List of LO-specific practical demonstrations |
| Submission | How candidates submit practical work (digital portfolio, physical submission) |
| Marking Process | 3 criteria, max 6 words each |
| Retention Period | Typically 3 years |

### CS (Case Study)

| Field | Description |
|-------|-------------|
| Evidence | List of LO-specific case analysis requirements |
| Submission | Electronic submission of reports |
| Marking Process | 3 criteria, max 6 words each |
| Retention Period | Typically 3 years |

### OQ (Oral Questioning)

| Field | Description |
|-------|-------------|
| Evidence | List of LO-specific verbal demonstration requirements |
| Submission | Assessor records during structured session |
| Marking Process | 3 criteria, max 6 words each |
| Retention Period | Typically 2 years |

### RP (Role Play)

| Field | Description |
|-------|-------------|
| Evidence | "Role Play" (fixed string) |
| Submission | Assessor observation checklist |
| Marking Process | 3 criteria, max 6 words each |
| Retention Period | Typically 3 years |
| No_of_Scripts | Minimum script requirements |

## Evidence Merging Logic

```python
def combine_assessment_methods(structured_data, evidence_data):
    evidence_methods = evidence_data.get("assessment_methods", {})

    for method in structured_data.get("Assessment_Methods_Details", []):
        method_abbr = method.get("Method_Abbreviation")

        if method_abbr in evidence_methods:
            evidence_details = evidence_methods[method_abbr]

            # PP, CS, OQ: List-based evidence
            if method_abbr in ["PP", "CS", "OQ"]:
                method.update({
                    "Evidence": evidence_details.get("evidence", []),
                    "Submission": evidence_details.get("submission", []),
                    "Marking_Process": evidence_details.get("marking_process", []),
                    "Retention_Period": evidence_details.get("retention_period", "")
                })

            # RP: Special handling with no_of_scripts
            if method_abbr == "RP":
                method.update({
                    "Evidence": evidence_details.get("evidence", ""),
                    "Submission": evidence_details.get("submission", ""),
                    "Marking_Process": evidence_details.get("marking_process", []),
                    "Retention_Period": evidence_details.get("retention_period", ""),
                    "No_of_Scripts": evidence_details.get("no_of_scripts", "Not specified")
                })

    return structured_data
```

## Method Abbreviations Reference

| Abbreviation | Full Name |
|-------------|-----------|
| WA-SAQ | Written Assessment - Short Answer Questions |
| WA | Written Assessment |
| PP | Practical Performance |
| CS | Case Study |
| OQ | Oral Questioning |
| RP | Role Play |
| PJ | Project |
| PF | Portfolio |
| OB | Observation |
