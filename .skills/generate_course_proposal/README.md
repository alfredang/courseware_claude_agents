# Generate Course Proposal Skill

## Overview
This skill handles user requests for generating Course Proposals (CP) for WSQ courses from TSC (Training & Competency Standards) documents.

## Files
- `SKILL.md` - Skill definition with keywords and response
- `examples.md` - Example prompts and outputs
- `reference/` - Prompt templates for all CP generation agents

## Prompt Templates

The `reference/` folder contains all prompt templates used in the CP generation pipeline:

| File | Agent | Purpose |
|------|-------|---------|
| `01_course_info_extractor.md` | Course Info Extractor | Extract course metadata |
| `02_learning_outcomes_extractor.md` | Learning Outcomes Extractor | Extract LOs, K and A statements |
| `03_tsc_topics_extractor.md` | TSC and Topics Extractor | Extract TSC info and topics |
| `04_assessment_methods_extractor.md` | Assessment Methods Extractor | Extract assessment/instructional methods |
| `05_tsc_agent.md` | TSC Agent | Parse and correct TSC data |
| `06_assessment_justification.md` | Assessment Justification | Generate assessment evidence/criteria |
| `07_course_description.md` | Course Description | Generate 2-paragraph course description |
| `08_ka_analysis.md` | KA Analysis | Map K&A factors to assessment rationale |
| `09_instructional_methods.md` | Instructional Methods | Contextualize IM explanations |

## Pipeline Flow

```
TSC Document (PDF/Word)
         │
         ▼
┌─────────────────────────────────────────┐
│         EXTRACTION TEAM                  │
│  ┌──────────────┐  ┌──────────────────┐ │
│  │ Course Info  │  │ Learning Outcomes│ │
│  └──────────────┘  └──────────────────┘ │
│  ┌──────────────┐  ┌──────────────────┐ │
│  │ TSC & Topics │  │ Assessment Methods│ │
│  └──────────────┘  └──────────────────┘ │
└─────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│              TSC AGENT                   │
│   (Parse, Correct, Validate Structure)   │
└─────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────┐
│      EXCEL GENERATION AGENTS             │
│  ┌──────────────┐  ┌──────────────────┐ │
│  │ Course Desc  │  │ KA Analysis      │ │
│  └──────────────┘  └──────────────────┘ │
│  ┌──────────────┐  ┌──────────────────┐ │
│  │ Assessment   │  │ Instructional    │ │
│  │ Justification│  │ Methods          │ │
│  └──────────────┘  └──────────────────┘ │
└─────────────────────────────────────────┘
         │
         ▼
   Course Proposal (Excel)
```

## How to Modify

1. Edit prompt templates in `reference/` folder to change agent behavior
2. Edit `SKILL.md` to change keywords or navigation response
3. Add examples to `examples.md` for testing

## Related Modules

- `generate_cp/` - Main CP generation module
- `generate_cp/agents/` - Agent implementations
- `chainlit_modules/course_proposal.py` - Chainlit UI handler
