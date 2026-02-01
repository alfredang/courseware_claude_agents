# Lesson Plan Generation Reference

## Overview

The Lesson Plan (LP) generation module creates a structured teaching plan document for instructors. It extracts data from the Course Proposal and populates a DOCX template. This module does NOT use AI generation - it performs data extraction and template population only.

## Pipeline Flow

```
Course Proposal (Excel) → Data Extraction → Learning Units Validation → Template Population → LP Document (DOCX)
```

## Components

| File | Purpose |
|------|---------|
| [01_template_context.md](01_template_context.md) | Context fields extracted from Course Proposal |

## Data Source

The Lesson Plan extracts data from the Course Proposal Excel file, including:
- Course Title
- Learning Units (LU_Title, LO, Topics)
- K and A Factors
- Assessment Methods
- Instructional Methods

## Template

Uses DOCX template: `generate_ap_fg_lg_lp/input/Template/LP_TGS-Ref-No_Course-Title_v1.docx`

## Key Features

1. **No AI Generation**: Pure data extraction and template population
2. **Learning Units Validation**: Ensures proper structure for all LUs
3. **Organization Branding**: Company logo integration
4. **Assessment Summary**: LO to Assessment Method mapping with abbreviations
5. **Version Control**: Automatic date stamping and revision tracking
