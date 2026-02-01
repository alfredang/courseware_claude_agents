# Slide Instructions Agent

## Purpose

Crafts optimal NotebookLM slide generation instructions based on document analysis, topics, and configuration. Replaces hardcoded instruction strings with intelligent, context-aware instructions.

## Agent Role

Slide Instructions Agent - Generates tailored NotebookLM generation instructions

## Function Signature

```python
async def run_slide_instructions(
    content: str,                    # Document content (truncated)
    topics: List[Dict[str, Any]],    # Topics from topic analysis
    config: Dict[str, Any],          # UI configuration
    research_sources_count: int,     # Number of approved research sources
    model_choice: str,               # LLM model selection
) -> Dict[str, Any]
```

## System Prompt

Loaded from: `prompt_templates/slides/slide_instructions.md`

Variables:
- `{material_type}` - Document type
- `{slide_style}` - Presentation style (Professional, Academic, etc.)
- `{slides_per_topic}` - Target slides per topic
- `{include_notes}` - Include speaker notes (True/False)
- `{include_summaries}` - Include section summaries (True/False)
- `{include_objectives}` - Include learning objectives (True/False)
- `{include_assessment}` - Include assessment points (True/False)
- `{has_research_sources}` - Whether research sources exist
- `{research_sources_count}` - Number of research sources
- `{document_summary}` - First 5000 chars of document
- `{topics_list}` - Formatted list of topics with rationale

## User Task

```
Generate the optimal slide generation instructions based on the analysis above.
Return as JSON.
```

## Output Schema

```json
{
    "instructions": "Create a professional slide deck for this WSQ course material. Structure the presentation with clear section titles for each learning unit. Target approximately 3 slides per topic. Include detailed speaker notes for facilitators. Add summary slides at the end of each section. Incorporate the latest research findings from the web sources provided. Cover all key learning outcomes and competencies.",
    "estimated_slides": 15,
    "structure_outline": [
        "Title and Agenda",
        "Learning Unit 1: Introduction",
        "Learning Unit 1: Key Concepts",
        "Learning Unit 1: Summary",
        "Learning Unit 2: Core Skills",
        "Learning Unit 2: Practical Applications",
        "Learning Unit 2: Summary",
        "Conclusion and Assessment Overview"
    ]
}
```

## Key Rules

- Document summary limited to 5000 characters
- Instructions tailored to material type and configuration
- Structure outline used for quality validation
- Includes research integration if sources available

## Fallback Instructions

If agent fails, hardcoded fallback is used:

```python
def _build_fallback_instructions(config, research_sources_count):
    instructions = (
        f"Create a {slide_style.lower()} slide deck for this WSQ course material. "
        f"Target approximately {slides_per_topic} slides per topic/learning unit. "
        "Structure the presentation so each major topic or learning unit has its own "
        "clearly separated section with a section title slide. "
        "Use a logical flow: start with an overview/agenda slide, then dedicate "
        "separate sections for each topic, and end with a conclusion/summary. "
    )
    if include_notes:
        instructions += "Include detailed speaker/facilitator notes for each slide. "
    if include_summaries:
        instructions += "Add a summary slide at the end of each section. "
    if research_sources_count > 0:
        instructions += "Incorporate the latest research findings from web sources. "
    instructions += "Ensure all key learning outcomes and competencies are covered."
    return instructions
```
