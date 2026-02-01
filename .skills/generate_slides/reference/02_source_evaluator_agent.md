# Source Evaluator Agent

## Purpose

Evaluates and filters research sources by quality before importing them into the NotebookLM notebook. Filters out low-quality or irrelevant sources to improve slide content quality.

## Agent Role

Source Evaluator Agent - Quality filtering of research sources

## Function Signature

```python
async def run_source_evaluator(
    sources: List[Dict[str, str]],  # Sources with url, title, summary
    document_domain: str,            # Domain from topic analysis
    research_query: str,             # Query that found these sources
    material_type: str,              # Document type (FG, LG, CP)
    model_choice: str,               # LLM model selection
) -> Dict[str, Any]
```

## System Prompt

Loaded from: `prompt_templates/slides/source_evaluation.md`

Variables:
- `{document_domain}` - Domain identified by topic analysis
- `{research_query}` - The research query
- `{material_type}` - Document type

## User Task

```
Evaluate the following {num_sources} research sources:

{sources_json}

Return your evaluation as a JSON object.
```

## Input Source Format

```json
[
    {
        "url": "https://example.com/article",
        "title": "Supply Chain Best Practices 2026",
        "summary": "Comprehensive guide to modern supply chain..."
    }
]
```

## Output Schema

```json
{
    "evaluated_sources": [
        {
            "url": "https://example.com/article",
            "title": "Supply Chain Best Practices 2026",
            "relevance_score": 8,
            "quality_score": 9,
            "credibility_score": 7,
            "approved": true,
            "reason": "Highly relevant industry content from reputable source"
        },
        {
            "url": "https://blog.example.com/random",
            "title": "Random Blog Post",
            "relevance_score": 2,
            "quality_score": 3,
            "credibility_score": 2,
            "approved": false,
            "reason": "Low relevance and questionable credibility"
        }
    ],
    "approved_count": 1,
    "rejected_count": 1
}
```

## Evaluation Criteria

| Criterion | Description | Score Range |
|-----------|-------------|-------------|
| `relevance_score` | How relevant to the research query | 1-10 |
| `quality_score` | Content quality and depth | 1-10 |
| `credibility_score` | Source authority and trustworthiness | 1-10 |

## Approval Logic

Sources are approved if they meet minimum thresholds across all criteria. Only approved sources are imported into NotebookLM.

## Key Rules

- Called once per research query batch (not per source)
- Minimizes LLM calls while evaluating multiple sources
- Only approved sources are imported to notebook
- Fallback: Import all sources if evaluator fails
