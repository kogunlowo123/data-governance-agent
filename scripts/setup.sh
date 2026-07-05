#!/bin/bash
set -euo pipefail
echo "Setting up Data Governance Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
