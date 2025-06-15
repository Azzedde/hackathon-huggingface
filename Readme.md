# AI Project Advisor - Multi-Agent Orchestration Platform

A powerful multi-agent AI system built for the Hugging Face Hackathon that combines specialized AI agents to provide comprehensive project advisory services. The platform features a drag-and-drop interface for creating custom agent workflows and supports various brainstorming methodologies.

## 🌟 Overview

The AI Project Advisor is an innovative platform that orchestrates multiple specialized AI agents to help users with:
- Creative brainstorming and ideation
- Technical project analysis
- Legal and regulatory research
- Data-driven insights and analysis
- Comprehensive project evaluation

## 🏗️ Architecture

### Backend (Python)
- **Framework**: FastAPI for REST API endpoints
- **AI Framework**: Smolagents with LiteLLM for model integration
- **Model**: Anthropic Claude (via API)
- **Key Components**:
  - Orchestrator Agent: Manages multi-agent workflows
  - Specialized Agents: Brainstorming, Technical, Legal, Data Analyst
  - API Server: FastAPI-based REST endpoints

### Frontend (Next.js)
- **Framework**: Next.js 15 with TypeScript
- **UI Library**: Tailwind CSS with Headless UI
- **State Management**: React Context API
- **Key Features**:
  - Drag-and-drop agent selection
  - Real-time chat interface
  - Dynamic brainstorming method selection

## 🤖 Available Agents

### 1. **Office Hours Agent (Brainstorming)**
- Generates creative ideas using multiple brainstorming techniques
- Supported methods:
  - **SCAMPER**: Substitute, Combine, Adapt, Modify, Put to another use, Eliminate, Reverse
  - **Mind Mapping**: Expands ideas into related concepts
  - **Starbursting**: Generates questions using 5W1H framework
  - **Reverse Brainstorming**: Identifies potential problems and challenges
  - **Role Storming**: Adopts different personas for diverse perspectives

### 2. **Analyst Agent**
- Provides data-driven insights and analysis
- Analyzes startup metrics and business data
- Generates comprehensive reports with actionable recommendations

### 3. **Technical Agent**
- Helps understand complex technical projects
- Searches and analyzes technical documentation
- Provides implementation guidance and best practices

### 4. **Legal Assistant Agent**
- Conducts legal research using Legifrance API
- Provides regulatory compliance analysis
- Evaluates legal risks and requirements

### 5. **Research Agents** (Coming Soon)
- Market Research Agent
- HR Agent
- Stress Test Agent

## 🚀 Getting Started

### Prerequisites
- Python 3.12+
- Node.js 18+
- Anthropic API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd hackathon-huggingface
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your ANTHROPIC_API_KEY
   ```

3. **Install Python dependencies**
   ```bash
   # Install uv package manager
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Install dependencies
   uv sync --all-extras --dev
   
   # Add project to Python path
   export PYTHONPATH=/path/to/hackathon-huggingface:$PYTHONPATH
   ```

4. **Install and run the frontend**
   ```bash
   cd workspace/app
   npm install
   npm run dev
   ```

5. **Start the backend API**
   ```bash
   # From project root
   python workspace/src/orchestrator_api.py
   ```

6. **Access the application**
   - Frontend: http://localhost:3000
   - API: http://localhost:8000

## 💡 Usage Examples

### Basic Usage
1. Navigate to the web interface
2. Enter your prompt in the text area
3. Drag and drop agents to the active zone
4. Select a brainstorming method (if using the brainstorming agent)
5. Click "Run" to execute the workflow

### Recommended Agent Combinations

| Use Case | Agent Combination | Description |
|----------|------------------|-------------|
| Ideation | Brainstorming alone | Free-form creative thinking |
| Market Analysis | Analyst + Research | Data-driven market insights |
| Technical Documentation | Technical + Research | Understanding complex projects |
| Comprehensive Analysis | Research + Analyst + Technical/Legal | Deep, multi-perspective insights |
| Research-backed Ideas | Brainstorming + Research | Well-researched creative solutions |

### CLI Usage
```bash
# Run the orchestrator from command line
python workspace/src/run_orchestrator_cli.py
```

## 📁 Project Structure

```
hackathon-huggingface/
├── .env.example              # Environment variables template
├── pyproject.toml           # Python project configuration
├── Readme.md               # This file
├── workspace/
│   ├── app/                # Next.js frontend application
│   │   ├── app/           # Next.js app directory
│   │   │   ├── api/      # API routes
│   │   │   ├── results/  # Results page
│   │   │   └── page.tsx  # Main page
│   │   ├── components/    # React components
│   │   │   ├── AgentPlayground.tsx
│   │   │   ├── ChatInterface.tsx
│   │   │   └── PromptForm.tsx
│   │   ├── contexts/      # React contexts
│   │   ├── data/         # Agent configurations
│   │   └── public/       # Static assets
│   ├── data/             # Sample data files
│   └── src/              # Python backend
│       ├── brainstorming_methods.py  # Brainstorming prompts
│       ├── brainstorming.py         # Brainstorming agent
│       ├── data_analyst_agent.py    # Data analysis agent
│       ├── legal_assistant.py       # Legal research agent
│       ├── technical_assistant.py   # Technical analysis agent
│       ├── orchestrator_agent.py    # Main orchestrator
│       └── orchestrator_api.py      # FastAPI server
```

## 🛠️ Development

### Code Standards
- **Commit Messages**: Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- **Branching**: Feature branches merged via Pull Requests
- **Python**: Type hints with mypy, formatted with ruff
- **TypeScript**: Strict mode enabled

### Running Tests
```bash
# Python tests
pytest

# TypeScript/React tests
cd workspace/app
npm test
```

### Development Tools
- **Python Linting**: `ruff`
- **Python Type Checking**: `mypy`
- **JavaScript Linting**: ESLint with Next.js config
- **CSS**: Tailwind CSS v4

## 🔧 Configuration

### Environment Variables
- `ANTHROPIC_API_KEY`: Your Anthropic API key for Claude access

### Python Configuration
- See `pyproject.toml` for dependency management and tool configuration
- Python 3.12+ required

### Frontend Configuration
- Next.js configuration in `workspace/app/next.config.ts`
- Tailwind CSS configuration in `workspace/app/tailwind.config.js`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project was created for the Hugging Face Hackathon. Please refer to the hackathon guidelines for licensing information.

## 🙏 Acknowledgments

- Built with [Smolagents](https://github.com/huggingface/smolagents) by Hugging Face
- Powered by Anthropic's Claude AI
- UI components from Headless UI and Tailwind CSS
- Drag-and-drop functionality using react-beautiful-dnd