# WSQ Courseware Generator

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Chainlit](https://img.shields.io/badge/Chainlit-2.9+-6366F1?style=for-the-badge&logo=chainlit&logoColor=white)](https://chainlit.io/)
[![Claude](https://img.shields.io/badge/Claude_Agent_SDK-Anthropic-D4A574?style=for-the-badge&logo=anthropic&logoColor=white)](https://docs.anthropic.com/)
[![OpenRouter](https://img.shields.io/badge/OpenRouter-38+_Models-00D4AA?style=for-the-badge)](https://openrouter.ai/)
[![License](https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge)](LICENSE)

A comprehensive AI-powered courseware generation platform built with **Claude Agent SDK** and **Streamlit/Chainlit**. This system uses an **orchestrator-based multi-agent architecture** with **34 AI agents** to automate the creation of educational documents including Course Proposals, Assessment Plans, Learning Guides, Presentation Slides, and more for Workforce Skills Qualification (WSQ) training programs.

---

## What is This App?

The **WSQ Courseware Generator** is an enterprise-grade AI platform designed for training providers to:

- **Generate Course Proposals** from Training Specification Content (TSC) documents
- **Create Complete Courseware** including Assessment Plans, Facilitator Guides, Learner Guides, and Lesson Plans
- **Produce 9 Types of Assessments** (SAQ, PP, CS, PRJ, ASGN, OI, DEM, RP, OQ)
- **Generate Presentation Slides** using Google NotebookLM with AI-enhanced research
- **Create Marketing Brochures** from course data or web scraping
- **Validate Supporting Documents** with entity extraction and ACRA company verification

The platform uses a sophisticated multi-agent architecture where specialized AI agents collaborate to produce high-quality, WSQ-compliant training materials.

---

## Tech Stack

### Core Frameworks
| Technology | Purpose |
|------------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Backend runtime |
| ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) | Web UI (Form-based interface) |
| ![Chainlit](https://img.shields.io/badge/Chainlit-6366F1?style=flat&logoColor=white) | Chat UI (Conversation-first interface) |

### AI & LLM
| Technology | Purpose |
|------------|---------|
| ![Claude](https://img.shields.io/badge/Claude_Agent_SDK-D4A574?style=flat&logo=anthropic&logoColor=white) | Multi-agent orchestration |
| ![OpenRouter](https://img.shields.io/badge/OpenRouter-00D4AA?style=flat&logoColor=white) | Unified LLM gateway (38+ models) |
| ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white) | GPT models access |
| ![Google](https://img.shields.io/badge/Gemini-4285F4?style=flat&logo=google&logoColor=white) | Gemini models & NotebookLM |
| ![Anthropic](https://img.shields.io/badge/Anthropic-D4A574?style=flat&logoColor=white) | Claude models |

### Document Processing
| Technology | Purpose |
|------------|---------|
| `python-docx` | Word document creation |
| `docxtpl` | Jinja2 DOCX templates |
| `docxcompose` | Multi-document composition |
| `PyPDF2` | PDF reading |
| `openpyxl` | Excel file handling |

### Database & Storage
| Technology | Purpose |
|------------|---------|
| ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white) | Company data (Neon) |
| ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white) | Local config & models |

### Web & Data
| Technology | Purpose |
|------------|---------|
| `beautifulsoup4` | Web scraping |
| `pydantic` | Data validation |
| `pandas` | Data manipulation |
| `gspread` | Google Sheets integration |

---

## Platform Statistics

| Metric | Count |
|--------|-------|
| AI Agents | 34 |
| Generation Modules | 7 |
| Assessment Types | 9 |
| Courseware Documents | 4 |
| Prompt Templates | 22 (customizable) |
| Skills | 12 |
| Supported LLM Providers | 7+ |
| Available Models (via OpenRouter) | 38+ |

---

## Quick Start

### 1. System Requirements
- **Python 3.11+** (check with `python3 --version`)
- **macOS / Linux / Windows** supported
- **4GB+ RAM** recommended
- **Git** installed
- **uv** installed (modern Python package manager)

### 2. Clone & Install

```bash
# Clone the repository
git clone https://github.com/alfredang/courseware_claude_agents.git
cd courseware_claude_agents

# Create virtual environment with uv
uv venv
source .venv/bin/activate          # macOS/Linux
# OR
.venv\Scripts\activate             # Windows

# Install dependencies
uv pip install -r requirements.txt
```

### 3. Configure Secrets

Create `.streamlit/secrets.toml`:

```toml
# API Keys
OPENAI_API_KEY = "sk-your-openai-key"
OPENROUTER_API_KEY = "sk-or-your-openrouter-key"
ANTHROPIC_API_KEY = "sk-ant-your-anthropic-key"
GEMINI_API_KEY = "your-gemini-key"

# Database (for company management)
DATABASE_URL = "postgresql://user:password@host/database?sslmode=require"

# Admin Authentication
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "your-secure-password"

# Google Service Account (for Google Sheets access)
[GOOGLE_SERVICE_ACCOUNT]
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-key-id"
private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
client_email = "your-service@project.iam.gserviceaccount.com"
client_id = "your-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
```

### 4. Run the Application

**Option A: Streamlit (Form-based UI)**
```bash
streamlit run app.py
```
Open browser to `http://localhost:8501`

**Option B: Chainlit (Chat-based UI)**
```bash
cd chainlit_app
chainlit run app.py --port 8000
```
Open browser to `http://localhost:8000`

---

## Deployment

### Deploy to Streamlit Cloud

1. **Push to GitHub** (ensure secrets are NOT committed)

2. **Connect to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your repository
   - Set main file: `app.py`

3. **Configure Secrets**
   - Go to App Settings → Secrets
   - Paste your `secrets.toml` content:
   ```toml
   OPENAI_API_KEY = "sk-..."
   OPENROUTER_API_KEY = "sk-or-..."
   ANTHROPIC_API_KEY = "sk-ant-..."
   DATABASE_URL = "postgresql://..."
   ADMIN_USERNAME = "admin"
   ADMIN_PASSWORD = "your-password"
   ```

4. **Deploy**
   - Click "Deploy"
   - Your app will be live at `https://your-app.streamlit.app`

### Deploy to Render / Railway / Heroku

1. **Create `Procfile`:**
   ```
   web: streamlit run app.py --server.port $PORT --server.headless true
   ```

2. **Set Environment Variables:**
   ```
   OPENAI_API_KEY=sk-...
   OPENROUTER_API_KEY=sk-or-...
   ANTHROPIC_API_KEY=sk-ant-...
   DATABASE_URL=postgresql://...
   ```

3. **Deploy from GitHub**

### Deploy Chainlit to Cloud

1. **Create `chainlit_app/Procfile`:**
   ```
   web: chainlit run app.py --host 0.0.0.0 --port $PORT
   ```

2. **Set Environment Variables:**
   ```
   CHAINLIT_AUTH_SECRET=your-jwt-secret
   OPENAI_API_KEY=sk-...
   ```

3. **Deploy to Render/Railway**

---

## Key Features

### Core Document Generation (7 Modules)

| Module | Description | Agents Used |
|--------|-------------|-------------|
| **Generate CP** | Course Proposal generation from TSC documents | 10 agents |
| **Generate Courseware** | Assessment Plan, Facilitator Guide, Learner Guide, Lesson Plan | 4 agents |
| **Generate Assessment** | 9 assessment types (SAQ, PP, CS, PRJ, ASGN, OI, DEM, RP, OQ) | 9 agents |
| **Generate Slides** | Agentic slide generation with Google NotebookLM | 4 agents + NotebookLM |
| **Generate Brochure** | Marketing materials with web scraping | 1 agent |
| **Add Assessment to AP** | Integrate assessments into AP annexes | Template-based |
| **Check Documents** | Supporting document validation | Gemini API |

### Dual Interface

| Interface | Port | Best For |
|-----------|------|----------|
| **Streamlit** | 8501 | Form-based workflows, bulk operations |
| **Chainlit** | 8000 | Conversational interaction, guided workflows |

### Model Support

| Provider | Models Available |
|----------|------------------|
| **OpenRouter** | 38+ models (unified gateway) |
| **OpenAI** | GPT-4o, GPT-4o-Mini, o1, o3-mini |
| **Anthropic** | Claude Opus 4.5, Claude Sonnet 4 |
| **Google** | Gemini 2.5 Pro/Flash, Gemini 2.0 |
| **DeepSeek** | DeepSeek-Chat, DeepSeek-R1 |
| **Meta** | Llama 3.3 70B |

---

## Multi-Agent Architecture

The system uses an **orchestrator-based architecture** powered by the Claude Agent SDK:

```
                    ┌─────────────────────────┐
                    │   Orchestrator Agent    │
                    │  (User Interaction)     │
                    └───────────┬─────────────┘
                                │ handoffs
        ┌───────────┬───────────┼───────────┬───────────┐
        ▼           ▼           ▼           ▼           ▼
   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
   │CP Agent │ │Courseware│ │Assessment│ │Brochure │ │Document │
   │         │ │  Agent   │ │  Agent   │ │  Agent  │ │  Agent  │
   └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘
```

### All 34 Agents

- **Orchestrator Agents (6)**: Main coordinator, CP, Courseware, Assessment, Brochure, Document
- **Course Proposal Agents (10)**: TSC, Extraction Team (5), Research Team, Validation Team, Justification, Excel
- **Assessment Agents (9)**: SAQ, PP, CS, PRJ, ASGN, OI, DEM, RP, OQ
- **Courseware Agents (4)**: AP, FG, LG, LP
- **Slides Agents (5)**: Topic Analysis, Source Evaluator, Slide Instructions, Quality Validator, Orchestrator

---

## Project Structure

```
courseware_claude_agents/
├── app.py                          # Main Streamlit application
├── chainlit_app/                   # Chainlit chat interface
│   ├── app.py                      # Chainlit entry point
│   ├── modules/                    # Chat profile handlers
│   └── public/                     # Static assets
├── courseware_agents/              # Claude Agent SDK agents
│   ├── orchestrator.py             # Main orchestrator
│   ├── cp_agent.py                 # Course Proposal agent
│   ├── courseware_agent.py         # Courseware agent
│   ├── assessment_agent.py         # Assessment agent
│   └── tools/                      # MCP tools
├── generate_cp/                    # Course Proposal generation
├── generate_assessment/            # Assessment generation (9 types)
├── generate_ap_fg_lg_lp/           # Courseware suite generation
├── generate_slides/                # Slide generation
├── generate_brochure/              # Brochure generation
├── settings/                       # Configuration & admin
├── company/                        # Company management
├── skills/                         # AI skill definitions
└── utils/                          # Shared utilities
```

---

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENROUTER_API_KEY` | Yes* | OpenRouter API key (recommended) |
| `OPENAI_API_KEY` | Yes* | OpenAI API key |
| `ANTHROPIC_API_KEY` | No | Anthropic API key |
| `GEMINI_API_KEY` | No | Google Gemini API key |
| `DATABASE_URL` | No | PostgreSQL connection string |
| `ADMIN_USERNAME` | No | Admin login username |
| `ADMIN_PASSWORD` | No | Admin login password |
| `CHAINLIT_AUTH_SECRET` | Chainlit only | JWT secret for Chainlit auth |

*At least one LLM API key is required

---

## Security

- **No hardcoded secrets** - All API keys stored in `secrets.toml` or environment variables
- **`.gitignore` configured** - Secrets files excluded from version control
- **Admin authentication** - Protected settings access
- **Session-based storage** - NotebookLM sessions stored locally only

### Files Excluded from Git
- `.streamlit/secrets.toml`
- `.env`
- `chainlit_app/.env`
- `*-credentials.json`
- `ssg-api-calls*.json`

---

## Troubleshooting

### Import Errors
```bash
uv pip install -r requirements.txt
python3 --version  # Must be 3.11+
```

### API Key Issues
- Use **Settings → API Keys** to manage keys
- Verify key validity with your provider
- OpenRouter: one key gives access to 38+ models

### Model Selection Issues
- Go to **Settings → LLM Models → Fetch Models**
- Ensure models are enabled
- Set a default model

### Chainlit Auth Errors
```bash
cd chainlit_app
chainlit create-secret
# Add the secret to .env file
```

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## License

This project is proprietary software developed for Tertiary Infotech. All rights reserved.

---

## Support

- [GitHub Issues](https://github.com/alfredang/courseware_claude_agents/issues)
- Check the troubleshooting section above
