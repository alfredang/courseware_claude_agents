# Slides Generation Reference

## Overview

The Slides Generation module creates professional presentation slides from course materials using a 5-agent AI pipeline integrated with NotebookLM MCP. It extracts learning outcomes and topics from the Course Proposal, conducts deep web research for internet and YouTube sources, and generates comprehensive presentation slides.

## Pipeline Flow

```
Course Proposal → CP Extraction → Topic Analysis Agent → NotebookLM Setup
                                        ↓
                               Web Research (NotebookLM)
                                        ↓
                               Source Evaluator Agent
                                        ↓
                               Slide Instructions Agent
                                        ↓
                               Generate Slides (NotebookLM)
                                        ↓
                               Quality Validator Agent
                                        ↓
                               Adaptive Retry (if needed)
                                        ↓
                               Final Slide Deck
```

## Components

| File | Purpose |
|------|---------|
| [01_topic_analysis_agent.md](01_topic_analysis_agent.md) | Extracts research-worthy topics from document |
| [02_source_evaluator_agent.md](02_source_evaluator_agent.md) | Filters and evaluates research sources |
| [03_slide_instructions_agent.md](03_slide_instructions_agent.md) | Crafts optimal NotebookLM instructions |
| [04_quality_validator_agent.md](04_quality_validator_agent.md) | Post-generation quality assessment |
| [05_notebooklm_integration.md](05_notebooklm_integration.md) | NotebookLM MCP operations and API |
| [06_slide_template_format.md](06_slide_template_format.md) | Slide template branding and formatting |

## Key Features

1. **5-Agent AI Pipeline**: Intelligent orchestration of specialized agents
2. **NotebookLM MCP Integration**: Deep web research for internet and YouTube sources
3. **Wikipedia Sources**: Automatic addition of relevant Wikipedia articles
4. **Source Quality Filtering**: AI-powered evaluation of research sources
5. **Adaptive Retry**: Quality-based regeneration with enhanced instructions
6. **Zero LLM Tokens for NotebookLM**: Only agents use LLM tokens

## Input Requirements

- **Course Proposal (Excel)**: Primary input with learning outcomes and topics
- **Facilitator Guide**: Alternative input for comprehensive content
- **Learner Guide**: Alternative input for learner-focused slides

## NotebookLM MCP Tools Used

| Tool | Purpose |
|------|---------|
| `create_notebook` | Create new notebook for course |
| `add_source_text` | Add course content as source |
| `add_source_url` | Add Wikipedia/web sources |
| `research.start` | Start web research query |
| `research.import_sources` | Import approved sources |
| `artifacts.generate_slide_deck` | Generate presentation slides |
| `chat.ask` | Query notebook for quality review |

## Configuration Options

| Option | Default | Description |
|--------|---------|-------------|
| `enable_research` | True | Enable web research |
| `num_queries` | 2 | Number of research queries |
| `slides_per_topic` | 3 | Target slides per topic |
| `include_notes` | True | Include speaker notes |
| `include_summaries` | True | Add section summaries |
| `slide_style` | "Professional" | Presentation style |
| `material_type` | "Course Material" | Source document type |

## Slide Template (`templates/slide_template.pptx`)

### Branding
- **Background**: White throughout all slides
- **Front/Back Pages**: Standard branded template

### Typography
| Element | Font | Size | Spacing |
|---------|------|------|---------|
| Page Header | Arial | 36 point | - |
| Page Body | Arial | 24 point | Single |

### Content Replaced from Course Proposal
- Learning Outcomes (LO1, LO2, etc.)
- Skills Framework K factors (Knowledge)
- Skills Framework A factors (Abilities)
- TSC Reference Code
- Lesson Plan / Topics
