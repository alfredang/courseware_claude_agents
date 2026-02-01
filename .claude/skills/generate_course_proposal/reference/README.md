# Course Proposal Prompt Templates Reference

This folder contains all the prompt templates used by the Course Proposal (CP) generation pipeline. These prompts are used to extract data from TSC (Training & Competency Standards) documents and generate structured Course Proposals in Excel format.

## Pipeline Overview

The CP generation uses a multi-agent pipeline that processes TSC documents in the following order:

```
TSC Document → Extraction Team → TSC Agent → Excel Generation Agents → Course Proposal (Excel)
```

## Extraction Team (Agents 01-04)

These agents run sequentially to extract different aspects from the TSC document:

| # | Agent | File | Purpose |
|---|-------|------|---------|
| 01 | Course Info Extractor | `01_course_info_extractor.md` | Extracts course metadata (title, hours, industry) |
| 02 | Learning Outcomes Extractor | `02_learning_outcomes_extractor.md` | Extracts LOs, K statements, A statements |
| 03 | TSC and Topics Extractor | `03_tsc_topics_extractor.md` | Extracts TSC title/code, topics, learning units |
| 04 | Assessment Methods Extractor | `04_assessment_methods_extractor.md` | Extracts assessment/instructional methods, course outline |

## TSC Agent (Agent 05)

| # | Agent | File | Purpose |
|---|-------|------|---------|
| 05 | TSC Agent | `05_tsc_agent.md` | Parses and corrects TSC data, validates structure |

## Excel Generation Agents (Agents 06-09)

These agents generate content for the Excel Course Proposal form:

| # | Agent | File | Purpose |
|---|-------|------|---------|
| 06 | Assessment Justification | `06_assessment_justification.md` | Generates evidence/marking criteria for assessments |
| 07 | Course Description | `07_course_description.md` | Generates 2-paragraph course description |
| 08 | KA Analysis | `08_ka_analysis.md` | Maps K&A factors to assessment rationale |
| 09 | Instructional Methods | `09_instructional_methods.md` | Contextualizes instructional method explanations |

## Key Data Structures

### Course Information
- Course Title
- Organization Name
- Classroom/Practical/Assessment Hours
- Industry (derived from TSC code prefix)

### Learning Outcomes
- LO1, LO2, etc. - Learning outcome statements
- K1, K2, etc. - Knowledge statements
- A1, A2, etc. - Ability statements

### TSC and Topics
- TSC Title and Code (XXX-XXX-XXXX-X.X format)
- Topics with K/A factor mappings
- Learning Units (LU1, LU2, etc.)

### Assessment Methods
Standard WSQ assessment methods:
- Written Assessment (WA-SAQ)
- Practical Performance (PP)
- Case Study (CS)
- Oral Questioning (OQ)
- Role Play (RP)

### Instructional Methods
Standard WSQ instructional methods:
- Didactic Questioning
- Demonstration
- Practical
- Peer Sharing
- Role Play
- Group Discussion
- Case Study
- Lecture
- Interactive Presentation

## Usage

These prompt templates are automatically used by the `generate_cp` module when processing TSC documents. To customize the prompts, edit the corresponding markdown file and restart the application.

## Related Code

- `generate_cp/agents/claude_extraction_team.py` - Extraction agents
- `generate_cp/agents/claude_tsc_agent.py` - TSC parsing agent
- `generate_cp/agents/claude_justification_agent.py` - Assessment justification
- `generate_cp/agents/claude_excel_agents.py` - Excel generation agents
