# NotebookLM MCP Integration

## Purpose

Documents the NotebookLM MCP (Model Context Protocol) operations used in the slides generation pipeline. NotebookLM operations use zero LLM tokens - all AI processing happens within Google's NotebookLM service.

## Authentication

```bash
# Initial login (opens browser for Google authentication)
cd notebooklm-mcp
uv run notebooklm login
```

## Client Initialization

```python
from notebooklm import NotebookLMClient

# Load credentials from storage
client = await NotebookLMClient.from_storage()

# Use as context manager
async with client:
    # Operations here
```

## Operations

### 1. Create Notebook

```python
notebook_title = f"{filename} - {material_type} Slides"
notebook = await client.notebooks.create(notebook_title)
notebook_id = notebook.id
```

### 2. Add Source Text (Course Content)

```python
source_title = f"{filename} ({material_type})"
source_text = content[:100000]  # Truncate to 100K chars
source = await client.sources.add_text(notebook_id, source_title, source_text)
source_id = source.id

# Wait for processing
wait_time = min(15, max(8, len(source_text) // 10000))
await asyncio.sleep(wait_time)
```

### 3. Add Wikipedia Sources

```python
# Build search URLs for topics
wiki_query = urllib.parse.quote_plus(topic_name)
url = f"https://en.wikipedia.org/w/index.php?search={wiki_query}"

source = await client.sources.add_url(notebook_id, url, wait=False)
```

### 4. Web Research

```python
# Start research query
task = await client.research.start(
    notebook_id,
    query,           # Research query string
    source="web",    # Source type
    mode="fast"      # Research mode
)
task_id = task.get("task_id")

# Poll for completion (timeout 120s)
while elapsed < timeout:
    await asyncio.sleep(5)
    result = await client.research.poll(notebook_id)
    if result.get("status") == "completed":
        found_sources = result.get("sources", [])
        break

# Import approved sources
imported = await client.research.import_sources(
    notebook_id,
    task_id,
    approved_sources  # Filtered by Source Evaluator Agent
)
```

### 5. Wait for Sources

```python
# Wait for platform sources (Wikipedia)
await client.sources.wait_for_sources(
    notebook_id,
    platform_source_ids,
    timeout=60.0
)

# Wait for research sources
await client.sources.wait_for_sources(
    notebook_id,
    research_source_ids,
    timeout=120.0
)
```

### 6. Generate Slides

```python
gen_result = await client.artifacts.generate_slide_deck(
    notebook_id,
    source_ids=all_source_ids,     # All sources to include
    instructions=instructions,      # From Slide Instructions Agent
)
task_id = gen_result.task_id

# Wait for completion (timeout 300s)
final_status = await client.artifacts.wait_for_completion(
    notebook_id,
    task_id,
    timeout=300.0
)
```

### 7. Chat Review (Quality Validation)

```python
review_question = (
    "Summarize the slide deck you generated. List all section titles, "
    "the key topics covered in each section, and whether speaker notes "
    "are included."
)
result = await client.chat.ask(notebook_id, review_question)
answer = result.answer
```

## Error Handling

### Authentication Errors

```python
if "auth" in error_msg.lower() or "login" in error_msg.lower():
    return {
        "success": False,
        "message": "NotebookLM authentication error. Please re-authenticate."
    }
```

### Import Errors

```python
try:
    from notebooklm import NotebookLMClient
except ImportError:
    return {
        "success": False,
        "message": "notebooklm-py is not installed. Run: pip install notebooklm-py[browser]"
    }
```

## MCP Tools Summary

| Tool | Operation | Zero LLM Tokens |
|------|-----------|-----------------|
| `notebooks.create` | Create new notebook | ✅ |
| `sources.add_text` | Add text source | ✅ |
| `sources.add_url` | Add URL source | ✅ |
| `sources.list` | List all sources | ✅ |
| `sources.wait_for_sources` | Wait for processing | ✅ |
| `research.start` | Start web research | ✅ |
| `research.poll` | Check research status | ✅ |
| `research.import_sources` | Import found sources | ✅ |
| `artifacts.generate_slide_deck` | Generate slides | ✅ |
| `artifacts.wait_for_completion` | Wait for generation | ✅ |
| `chat.ask` | Query notebook content | ✅ |

## Pipeline Result

```json
{
    "success": true,
    "message": "Slide deck generated successfully!",
    "notebook_id": "abc123",
    "notebook_title": "Course_FG - Facilitator Guide Slides",
    "task_id": "gen_xyz789",
    "source_id": "src_456",
    "generation_status": "completed",
    "research_enabled": true,
    "research_queries": ["topic 1 best practices", "topic 2 industry standards"],
    "research_sources_count": 5,
    "platform_sources_count": 3,
    "total_sources": 9,
    "topic_analysis": { ... },
    "source_evaluations": [ ... ],
    "quality_report": { ... },
    "instructions_used": "Create a professional slide deck..."
}
```
