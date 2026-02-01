# Topic Analysis Agent

## Purpose

Analyzes document content and extracts research-worthy topics using LLM. Replaces regex-based extraction with intelligent topic identification, relevance scoring, and research query generation.

## Agent Role

Topic Analysis Agent - Intelligent topic extraction and research query generation

## Function Signature

```python
async def run_topic_analysis(
    content: str,           # Extracted document text
    filename: str,          # Original filename
    material_type: str,     # Type: FG, LG, CP, Other
    num_queries: int,       # Maximum topics to return
    model_choice: str,      # LLM model selection
) -> Dict[str, Any]
```

## System Prompt

Loaded from: `prompt_templates/slides/topic_analysis.md`

Variables:
- `{material_type}` - Document type (FG, LG, CP)
- `{filename}` - Original filename

## User Task

```
Analyze the following document content and identify the top {num_queries}
most research-worthy topics.

---
{truncated_content}
---

Return your analysis as a JSON object.
```

## Output Schema

```json
{
    "document_domain": "Logistics Management",
    "document_type_detected": "Facilitator Guide",
    "topics": [
        {
            "name": "Supply Chain Optimization",
            "research_query": "supply chain optimization best practices latest developments",
            "relevance_score": 9,
            "rationale": "Core topic central to the course learning outcomes"
        },
        {
            "name": "Inventory Management Systems",
            "research_query": "inventory management systems industry standards 2026",
            "relevance_score": 8,
            "rationale": "Key practical skill covered across multiple learning units"
        }
    ],
    "total_topics_found": 5
}
```

## Key Rules

- Content truncated to 15,000 characters for context window
- Topics sorted by relevance_score (descending)
- Maximum topics capped at `num_queries`
- Research queries formatted for web search
- Fallback to regex extraction if agent fails

## Fallback Behavior

If LLM produces no queries:
1. Uses regex-based topic extraction
2. Builds Wikipedia search URLs from topic names
3. Creates basic topic dicts with extracted queries

```python
# Fallback pattern for extracting topics
research_queries = _extract_research_queries(content, filename, material_type, num_queries)
topics = [{"name": query, "research_query": query} for query in research_queries]
```
