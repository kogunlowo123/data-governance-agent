# Data Governance Agent

[![CI](https://github.com/kogunlowo123/data-governance-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/data-governance-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Data Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Data governance agent that manages data catalogs, enforces access policies, classifies sensitive data, tracks data ownership, and ensures compliance with data regulations across the organization.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `catalog_dataset` | Register a dataset in the data catalog with metadata |
| `classify_data` | Classify data sensitivity level (public, internal, confidential, restricted) |
| `set_access_policy` | Set access policy for a dataset based on classification |
| `track_ownership` | Assign or transfer data ownership and stewardship |
| `check_compliance` | Check dataset compliance against regulations (GDPR, CCPA, HIPAA) |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/governance/catalog` | Catalog dataset |
| `POST` | `/api/v1/governance/classify` | Classify data |
| `POST` | `/api/v1/governance/access-policy` | Set access policy |
| `POST` | `/api/v1/governance/ownership` | Track ownership |
| `POST` | `/api/v1/governance/compliance` | Check compliance |

## Features

- Data Catalog
- Access Control
- Data Classification
- Ownership Tracking
- Regulatory Compliance

## Integrations

- Datahub
- Apache Atlas
- Collibra
- Alation
- Immuta

## Architecture

```
data-governance-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── data_governance_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Data Catalog + Access Control + Classification Engine**

---

Built as part of the Enterprise AI Agent Platform.
