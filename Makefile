# Makefile for Speech-To-Text AI

.PHONY: help install dev clean test test-cov lint format pre-commit build run

# Default target
.DEFAULT_GOAL := help

# Colors for output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m # No Color

help: ## Show this help message
	@echo "$(BLUE)🎤 Speech-To-Text AI - Makefile Commands$(NC)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-15s$(NC) %s\n", $$1, $$2}'
	@echo ""

install: ## Install package in production mode
	@echo "$(BLUE)📦 Installing package...$(NC)"
	pip install -e .

dev: ## Install package with development dependencies
	@echo "$(BLUE)🔧 Installing development dependencies...$(NC)"
	pip install -e ".[dev]"
	pre-commit install

install-all: ## Install package with all optional dependencies
	@echo "$(BLUE)🚀 Installing all dependencies...$(NC)"
	pip install -e ".[all]"

clean: ## Clean build artifacts and caches
	@echo "$(BLUE)🧹 Cleaning up...$(NC)"
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

test: ## Run tests
	@echo "$(BLUE)🧪 Running tests...$(NC)"
	pytest tests/ -v

test-cov: ## Run tests with coverage report
	@echo "$(BLUE)📊 Running tests with coverage...$(NC)"
	pytest tests/ --cov=src/speech_to_text_ai --cov-report=term-missing --cov-report=html -v
	@echo "$(GREEN)✓ Coverage report generated in htmlcov/index.html$(NC)"

test-watch: ## Run tests in watch mode
	@echo "$(BLUE)👀 Running tests in watch mode...$(NC)"
	pytest-watch tests/ -v

lint: ## Run linters (ruff, black, mypy)
	@echo "$(BLUE)🔍 Running linters...$(NC)"
	ruff check src/ tests/
	black --check src/ tests/
	mypy src/

format: ## Format code with black and ruff
	@echo "$(BLUE)✨ Formatting code...$(NC)"
	black src/ tests/
	ruff check --fix src/ tests/
	@echo "$(GREEN)✓ Code formatted$(NC)"

pre-commit: ## Run pre-commit hooks on all files
	@echo "$(BLUE)🔧 Running pre-commit hooks...$(NC)"
	pre-commit run --all-files

build: ## Build distribution packages
	@echo "$(BLUE)📦 Building package...$(NC)"
	hatch build
	@echo "$(GREEN)✓ Build complete$(NC)"

publish: ## Publish to PyPI (requires credentials)
	@echo "$(BLUE)🚀 Publishing to PyPI...$(NC)"
	hatch publish

run: ## Run the CLI (interactive mode)
	@echo "$(BLUE)🎤 Starting Speech-To-Text AI...$(NC)"
	python -m speech_to_text_ai interactive

run-listen: ## Run the CLI (listen once mode)
	@echo "$(BLUE)🎧 Listening...$(NC)"
	python -m speech_to_text_ai listen

run-continuous: ## Run the CLI (continuous mode)
	@echo "$(BLUE)🔄 Starting continuous recognition...$(NC)"
	python -m speech_to_text_ai continuous

devices: ## List available microphone devices
	@echo "$(BLUE)🎙️  Listing microphones...$(NC)"
	python -m speech_to_text_ai devices

languages: ## List supported languages
	@echo "$(BLUE)🌍 Supported languages:$(NC)"
	python -m speech_to_text_ai languages

docs: ## Generate documentation (placeholder)
	@echo "$(YELLOW)📚 Documentation generation not yet implemented$(NC)"

update-deps: ## Update dependencies
	@echo "$(BLUE)🔄 Updating dependencies...$(NC)"
	pip install --upgrade pip hatch
	pip install -e ".[dev]"

setup-hooks: ## Setup pre-commit hooks
	@echo "$(BLUE)⚙️  Setting up pre-commit hooks...$(NC)"
	pre-commit install
	pre-commit install --hook-type commit-msg
	@echo "$(GREEN)✓ Pre-commit hooks installed$(NC)"

check: lint test ## Run linters and tests

all: clean format lint test ## Clean, format, lint, and test

info: ## Show project info
	@echo "$(BLUE)ℹ️  Project Information$(NC)"
	@echo "  Name:    speech-to-text-ai"
	@echo "  Version: 1.0.0"
	@echo "  Python:  >= 3.8"
	@echo "  Build:   Hatch"
	@echo ""
	@echo "$(BLUE)📦 Installed Packages:$(NC)"
	@pip list | grep -E "(speech-to-text|SpeechRecognition|PyAudio|pyttsx3|typer|rich)"

deps-tree: ## Show dependency tree
	@echo "$(BLUE)🌲 Dependency tree:$(NC)"
	pipdeptree -p speech-to-text-ai

.PHONY: help install dev install-all clean test test-cov test-watch lint format \
        pre-commit build publish run run-listen run-continuous devices languages \
        docs update-deps setup-hooks check all info deps-tree
