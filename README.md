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
  - repo: https://github.com/yourusername/env-manager-hook
    rev: v1.0.0
    hooks:
      - id: env-manager
