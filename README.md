# .env Manager Pre-commit Hook

Automatically manage your `.env` files with this pre-commit hook that:

- 🔧 Creates `.env.example` from your `.env` file with secrets stripped
- 📋 Ensures `.env` is added to `.gitignore`
- 💡 Preserves comments and formatting
- ⚙️ Configurable and flexible

## Usage

Add this to your `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/timothypreble/env-manager-hook
    rev: v1.0.0
    hooks:
      - id: env-manager
```

## Configuration

The hook supports several options for different use cases:

### Basic Usage (Default)
```yaml
repos:
  - repo: https://github.com/timothypreble/env-manager-hook
    rev: v1.0.0
    hooks:
      - id: env-manager
```
This will process `.env` → `.env.example` and ensure `.env` is in `.gitignore`.

### Custom Environment File
```yaml
repos:
  - repo: https://github.com/timothypreble/env-manager-hook
    rev: v1.0.0
    hooks:
      - id: env-manager
        args: ['--env-file', '.env.production']
```
Perfect for projects with multiple environment files like `.env.staging`, `.env.production`, etc.

### Skip GitIgnore Management
```yaml
repos:
  - repo: https://github.com/timothypreble/env-manager-hook
    rev: v1.0.0
    hooks:
      - id: env-manager
        args: ['--skip-gitignore']
```
Useful when you have a custom `.gitignore` setup or use global gitignore rules.

### Multiple Environment Files
```yaml
repos:
  - repo: https://github.com/timothypreble/env-manager-hook
    rev: v1.0.0
    hooks:
      - id: env-manager-dev
        alias: env-manager-dev
        args: ['--env-file', '.env.development']
      - id: env-manager-prod
        alias: env-manager-prod
        args: ['--env-file', '.env.production', '--skip-gitignore']
```
Handle multiple environment files in one go (gitignore only updated once).

### Monorepo Setup
```yaml
repos:
  - repo: https://github.com/timothypreble/env-manager-hook
    rev: v1.0.0
    hooks:
      - id: env-manager-api
        alias: env-manager-api
        args: ['--env-file', 'api/.env']
      - id: env-manager-frontend
        alias: env-manager-frontend
        args: ['--env-file', 'frontend/.env']
```
Perfect for monorepos with multiple services that each have their own `.env` files.

### Options Reference

| Option | Description | Default |
|--------|-------------|---------|
| `--env-file` | Path to the environment file to process | `.env` |
| `--skip-gitignore` | Skip updating .gitignore with .env entry | `false` |

## Example

Given a `.env` file:
```bash
# Database settings
DB_HOST=localhost
DB_PASSWORD=super_secret_123
API_KEY=sk-abcdef123456  # OpenAI API key

# App settings
DEBUG=true
```

The hook will create `.env.example`:
```bash
# Environment variables template
# Copy this file to .env and fill in your actual values

# Database settings
DB_HOST=
DB_PASSWORD=
API_KEY=  # OpenAI API key

# App settings
DEBUG=
```

## Installation

### Via Pre-commit (Recommended)
Add the hook to your `.pre-commit-config.yaml` as shown above, then run:
```bash
pre-commit install
```

### Direct Installation
```bash
pip install git+https://github.com/timothypreble/env-manager-hook
```

### Manual Usage
You can also run the tool manually:
```bash
env-manager --env-file .env.production --skip-gitignore
```

## How It Works

1. **Finds your git repository root** - Works from any subdirectory
2. **Locates environment files** - Looks for `.env` or custom file you specify
3. **Creates example files** - Strips values while preserving keys and comments
4. **Updates .gitignore** - Ensures environment files are ignored by git
5. **Handles edge cases** - Preserves formatting, handles missing files gracefully

## Features

- ✅ **Smart value stripping** - Removes secrets but keeps structure
- ✅ **Comment preservation** - Maintains inline comments for context
- ✅ **Flexible file paths** - Works with nested directories and custom names
-