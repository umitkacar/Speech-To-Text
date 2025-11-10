#!/bin/bash
# Development environment setup script

set -e  # Exit on error

echo "🎤 Speech-To-Text AI - Development Setup"
echo "========================================"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check Python version
echo -e "${BLUE}Checking Python version...${NC}"
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "  Python version: $python_version"

# Check if we're in a virtual environment
if [[ -z "${VIRTUAL_ENV}" ]]; then
    echo -e "${YELLOW}⚠️  Not in a virtual environment!${NC}"
    echo "  It's recommended to use a virtual environment."
    echo "  Create one with: python3 -m venv venv"
    echo "  Activate with: source venv/bin/activate"
    read -p "  Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    echo -e "${GREEN}✓ Virtual environment active${NC}"
fi

# Upgrade pip
echo ""
echo -e "${BLUE}Upgrading pip...${NC}"
python3 -m pip install --upgrade pip setuptools wheel

# Install package with dev dependencies
echo ""
echo -e "${BLUE}Installing package with development dependencies...${NC}"
pip install -e ".[dev]"

# Install pre-commit hooks
echo ""
echo -e "${BLUE}Setting up pre-commit hooks...${NC}"
pre-commit install
pre-commit install --hook-type commit-msg

# Run pre-commit on all files (optional)
echo ""
read -p "Run pre-commit on all files now? (y/N) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    pre-commit run --all-files || true
fi

# Verify installations
echo ""
echo -e "${BLUE}Verifying installations...${NC}"

commands=("pytest" "black" "ruff" "mypy" "pre-commit" "hatch")
for cmd in "${commands[@]}"; do
    if command -v $cmd &> /dev/null; then
        version=$($cmd --version 2>&1 | head -n 1)
        echo -e "  ${GREEN}✓${NC} $cmd: $version"
    else
        echo -e "  ${RED}✗${NC} $cmd: not found"
    fi
done

# Show project info
echo ""
echo -e "${BLUE}Project structure:${NC}"
tree -L 2 -I '__pycache__|*.pyc|*.egg-info|.git|.venv|venv' . 2>/dev/null || find . -maxdepth 2 -type d | grep -v "__pycache__\|\.git\|\.venv\|venv" | head -20

echo ""
echo -e "${GREEN}✓ Development environment setup complete!${NC}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "  1. Run tests:        make test"
echo "  2. Run linters:      make lint"
echo "  3. Format code:      make format"
echo "  4. Try the CLI:      speech-to-text-ai --help"
echo "  5. View commands:    make help"
echo ""
