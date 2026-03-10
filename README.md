# GitHub Models — Zero Infrastructure AI Development

Start building AI apps **today** using GitHub Models. No Azure environment needed. When Azure is ready, change one env var.

## Prerequisites

- Python 3.10+
- [GitHub CLI](https://cli.github.com/) (`gh`) authenticated
- A GitHub account with Copilot access (Free tier works — 50 premium requests/month; paid plans get more)

## Quick Start

### macOS / Linux

```bash
git clone https://github.com/idanshimon/github-models-demo.git
cd github-models-demo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

GITHUB_TOKEN=$(gh auth token) python3 demo.py
GITHUB_TOKEN=$(gh auth token) python3 demo_streaming.py
GITHUB_TOKEN=$(gh auth token) python3 demo_repoint.py
```

### Windows (PowerShell)

```powershell
git clone https://github.com/idanshimon/github-models-demo.git
cd github-models-demo
python -m venv .venv
.venv\Scripts\Activate
pip install -r requirements.txt

$env:GITHUB_TOKEN = gh auth token
python demo.py
python demo_streaming.py
python demo_repoint.py
```

## What's Inside

| File | What It Shows |
|---|---|
| `demo.py` | Basic chat completion — 10 lines, works immediately |
| `demo_streaming.py` | Real-time token streaming — same UX as Azure OpenAI |
| `demo_repoint.py` | The money shot — one env var switches GitHub ↔ Azure |

## How It Works

The [OpenAI Python SDK](https://github.com/openai/openai-python) is model-provider agnostic. You just change the `base_url`:

```python
from openai import OpenAI

# GitHub Models (today — no Azure needed)
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"]
)

# Azure OpenAI (when your environment is ready)
# client = OpenAI(
#     base_url="https://<your-endpoint>.openai.azure.com/openai/deployments/gpt-4o",
#     api_key=os.environ["AZURE_OPENAI_KEY"],
#     default_headers={"api-key": os.environ["AZURE_OPENAI_KEY"]},
#     api_version="2024-06-01"
# )

# Same code, same SDK, same prompts. Zero changes below this line.
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

## Available Models (GitHub Models)

Picked from the model dropdown — same models available via API:

| Model | Cost (Paid Plan) | Best For |
|---|---|---|
| GPT-5 mini | **Free** (0x) | Fast coding, general tasks |
| GPT-4.1 | **Free** (0x) | Fast coding, general tasks |
| Claude Sonnet 4.6 | 1x | Complex reasoning, code generation |
| Gemini 3 Pro | 1x | Long context, research |
| Claude Opus 4.6 | 3x | Deep reasoning, architecture decisions |

Full model list: [GitHub Copilot Model Comparison](https://docs.github.com/en/copilot/reference/ai-models/model-comparison)

## The Repoint Story

### Phase 1: Now (GitHub Models)

macOS/Linux:
```bash
GITHUB_TOKEN=$(gh auth token) AI_PROVIDER=github python3 demo_repoint.py
```

Windows (PowerShell):
```powershell
$env:GITHUB_TOKEN = gh auth token
$env:AI_PROVIDER = "github"
python demo_repoint.py
```
- Zero Azure dependency
- Zero infrastructure
- Devs are productive immediately

### Phase 2: When Azure is ready

macOS/Linux:
```bash
AI_PROVIDER=azure \
  AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com \
  AZURE_OPENAI_KEY=your-key \
  python3 demo_repoint.py
```

Windows (PowerShell):
```powershell
$env:AI_PROVIDER = "azure"
$env:AZURE_OPENAI_ENDPOINT = "https://your-endpoint.openai.azure.com"
$env:AZURE_OPENAI_KEY = "your-key"
python demo_repoint.py
```
- Same code, same prompts
- Add App Gateway / WAF / APIM as needed for enterprise
- Zero wasted dev work

## Using with Copilot Chat in VS Code

If your devs are using Copilot Chat (not building an app that calls models), they don't need any of this. Just:

1. Open VS Code
2. Open Copilot Chat
3. Pick a model from the dropdown (GPT-5 mini, Sonnet 4.6, etc.)
4. Start coding

GitHub Models are already built into Copilot. No API calls, no tokens, no config.

**Foundry Local** (via the AI Toolkit extension) adds local models to that same dropdown if you need offline/air-gapped development.

## Author

**Idan Shimon** — Microsoft Solution Engineer, Healthcare & Life Sciences

## License

MIT — see [LICENSE](LICENSE) for details.
