# Quality Validator Agent

## Purpose

Post-generation quality assessment of slides using NotebookLM chat review data. Scores the generated slides and recommends whether to accept or retry with modifications.

## Agent Role

Quality Validator Agent - Slide quality assessment and adaptive retry decisions

## Function Signature

```python
async def run_quality_validator(
    slide_review_data: str,          # NotebookLM chat review response
    expected_topics: List[str],      # Topics that should be covered
    expected_structure: List[str],   # Expected structure from instructions agent
    material_type: str,              # Document type
    model_choice: str,               # LLM model selection
) -> Dict[str, Any]
```

## System Prompt

Loaded from: `prompt_templates/slides/quality_validation.md`

Variables:
- `{material_type}` - Document type
- `{expected_topics}` - JSON list of expected topic names
- `{expected_structure}` - JSON list of expected structure outline
- `{slide_review_data}` - NotebookLM chat response about slides

## NotebookLM Chat Review

Before validation, the system queries NotebookLM:

```python
review_question = (
    "Summarize the slide deck you generated. List all section titles, "
    "the key topics covered in each section, and whether speaker notes "
    "are included. Also note any learning outcomes or assessment points covered."
)
result = await client.chat.ask(notebook_id, review_question)
```

## User Task

```
Evaluate the slide deck quality based on the information provided.
Return as JSON.
```

## Output Schema

```json
{
    "overall_score": 8,
    "criteria_scores": {
        "topic_coverage": 9,
        "structure_quality": 8,
        "speaker_notes": 7,
        "learning_outcomes": 8,
        "visual_clarity": 7
    },
    "recommendation": "pass",
    "strengths": [
        "Comprehensive topic coverage",
        "Clear section organization",
        "Good speaker notes throughout"
    ],
    "weaknesses": [
        "Assessment points could be more prominent",
        "Some sections may be too detailed"
    ],
    "retry_suggestions": ""
}
```

## Recommendation Values

| Value | Description |
|-------|-------------|
| `pass` | Slides meet quality standards |
| `retry_with_modifications` | Regenerate with enhanced instructions |
| `retry_full` | Full regeneration needed |

## Adaptive Retry Logic

If recommendation is `retry_with_modifications`:

```python
if recommendation == "retry_with_modifications" and max_retries > 0:
    retry_suggestions = quality_report.get("retry_suggestions", "")
    modified_instructions = (
        original_instructions +
        f"\n\nADDITIONAL REQUIREMENTS: {retry_suggestions}"
    )
    # Regenerate slides with modified instructions
```

## Key Rules

- Score range: 1-10 for all criteria
- `overall_score` is aggregate of criteria scores
- Only triggers retry if `max_retries > 0`
- Retry suggestions inform enhanced instructions
- Chat review uses zero additional LLM tokens (NotebookLM)
