# CLAUDE.md - Project Context for Claude Code

## Project Overview

**WSQ Courseware Generator** - An AI-powered platform for generating Singapore Workforce Skills Qualifications (WSQ) training materials using Claude AI.

## Tech Stack

| Component | Technology |
|-----------|------------|
| UI Framework | Chainlit 2.0+ |
| Backend | Python 3.13 |
| LLM | Claude API (Anthropic) |
| Database | PostgreSQL (Neon) |
| Deployment | Docker, Hugging Face Spaces |

## Project Structure

```
courseware_claude/
├── app.py                    # Main Chainlit application
├── chainlit_modules/         # Chat profile handlers
├── generate_cp/              # Course Proposal generation (10 agents)
├── generate_assessment/      # Assessment generation (9 agents)
├── generate_ap_fg_lg_lp/     # Courseware documents (4 agents)
├── generate_slides/          # Slides generation (5 agents)
├── generate_brochure/        # Brochure generation
├── add_assessment_to_ap/     # Annex assessments to AP
├── check_documents/          # Document verification
├── courseware_agents/        # Shared agent utilities
├── settings/                 # API & model configuration
├── company/                  # Company management
├── skills/                   # NLP skill matching
├── utils/                    # Shared utilities
├── docs/                     # Documentation
├── .skills/                  # Skill definitions for Claude (13 skills)
└── public/                   # Static assets (CSS)
```

## Key Patterns

### Chainlit Patterns
- Use `@cl.on_chat_start` for initialization
- Use `@cl.on_message` for message handling
- Use `cl.ChatProfile` for module switching
- Use `cl.user_session` for state management
- Use `cl.Step()` for long-running operations

### Agent Pattern
Each generation module follows this pattern:
```python
# agents/<agent_name>.py
async def run_agent(input_data: dict) -> dict:
    # 1. Extract data from input
    # 2. Call Claude API with prompt
    # 3. Parse and return structured output
```

### Claude API Usage
```python
from anthropic import Anthropic

client = Anthropic()  # Uses ANTHROPIC_API_KEY from env

response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=4096,
    messages=[{"role": "user", "content": prompt}]
)
```

## Environment Variables

```bash
ANTHROPIC_API_KEY=sk-ant-...     # Required - Claude API
DATABASE_URL=postgresql://...     # Required - Neon PostgreSQL
CHAINLIT_AUTH_SECRET=...          # Required - Session encryption
```

## Skills System

Skills are defined in `.skills/<skill_name>/`:
- `SKILL.md` - Command, keywords, response template
- `README.md` - Developer documentation
- `examples.md` - Example prompts
- `reference/` - Technical reference docs for agents

Skills use fuzzy matching via `rapidfuzz` to match user intents.

**Execution**: All skills run using **Claude Code with subscription plan** (not pay-as-you-go API).

## Document Generation

Generated documents use templates stored in `generate_ap_fg_lg_lp/utils/`:
- Assessment Plan (AP)
- Facilitator Guide (FG)
- Learner Guide (LG)
- Lesson Plan (LP)

Templates use `docxtpl` (Jinja2 syntax) for variable substitution. Slide templates are in `.skills/generate_slides/templates/`.

## Coding Conventions

- Use `async/await` for all I/O operations
- Use type hints for function signatures
- Keep agents modular and single-purpose
- Store prompts in separate files under `prompts/`
- Use `cl.Message()` for user feedback, not print()

## Common Commands

```bash
# Run locally
uv run chainlit run app.py -w

# Build Docker
docker build -t wsq-courseware .

# Run Docker
docker run -p 7860:7860 --env-file .env wsq-courseware
```

## Models

| Model | ID | Use Case |
|-------|------|----------|
| Claude Sonnet 4 | `claude-sonnet-4-20250514` | Default - balanced |
| Claude Opus 4.5 | `claude-opus-4-5-20250130` | Complex reasoning |
| Claude Haiku 3.5 | `claude-3-5-haiku-20241022` | Fast tasks |
