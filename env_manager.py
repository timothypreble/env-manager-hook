#!/usr/bin/env python3
"""
Pre-commit hook to manage .env files and .gitignore
Automatically creates .env.example and ensures .env is gitignored
"""

import argparse
import os
import re
import sys
from pathlib import Path


def find_git_root():
    """Find the root directory of the git repository."""
    current = Path.cwd()
    for parent in [current] + list(current.parents):
        if (parent / '.git').exists():
            return parent
    return current  # Fallback to current directory


def create_env_example(env_path: Path) -> bool:
    """Create .env.example from .env file, stripping values."""
    try:
        with open(env_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        example_lines = []
        example_lines.append("# Environment variables template\n")
        example_lines.append("# Copy this file to .env and fill in your actual values\n")
        example_lines.append("\n")
        
        for line in lines:
            stripped = line.strip()
            
            # Skip empty lines
            if not stripped:
                example_lines.append(line)
                continue
            
            # Keep comments that start and end with ###
            if stripped.startswith('###') and stripped.endswith('###'):
                example_lines.append(line)
                continue
            
            # Handle key=value pairs
            if '=' in stripped:
                key = stripped.split('=', 1)[0]
                # Preserve any inline comments that start and end with ###
                comment_match = re.search(r'#.*###$', stripped)
                comment = comment_match.group() if comment_match else ''
                example_lines.append(f"{key}={comment}\n")
            else:
                # Keep non-standard lines as-is
                example_lines.append(line)
        
        example_path = env_path.parent / '.env.example'
        with open(example_path, 'w', encoding='utf-8') as f:
            f.writelines(example_lines)
        
        print(f"✅ Created {example_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error creating .env.example: {e}")
        return False


def ensure_gitignore_has_env(root_dir: Path) -> bool:
    """Ensure .env is in .gitignore."""
    gitignore_path = root_dir / '.gitignore'
    
    try:
        if gitignore_path.exists():
            with open(gitignore_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if .env is already ignored (handle various patterns)
            env_patterns = [r'^\.env$', r'^\.env\s', r'/\.env$', r'/\.env\s']
            for pattern in env_patterns:
                if re.search(pattern, content, re.MULTILINE):
                    print("✅ .env already in .gitignore")
                    return True
            
            # Add .env to existing .gitignore
            with open(gitignore_path, 'a', encoding='utf-8') as f:
                if not content.endswith('\n'):
                    f.write('\n')
                f.write('\n# Environment variables\n')
                f.write('.env\n')
            print("➕ Added .env to existing .gitignore")
            
        else:
            # Create new .gitignore
            with open(gitignore_path, 'w', encoding='utf-8') as f:
                f.write("# Environment variables\n")
                f.write(".env\n")
                f.write("\n# Add other common ignores below as needed\n")
            print("📝 Created .gitignore with .env entry")
        
        return True
        
    except Exception as e:
        print(f"❌ Error updating .gitignore: {e}")
        return False


def main():
    """Main function for the pre-commit hook."""
    parser = argparse.ArgumentParser(
        description="Manage .env files and .gitignore for pre-commit"
    )
    parser.add_argument(
        '--env-file',
        default='.env',
        help='Path to the .env file (default: .env)'
    )
    parser.add_argument(
        '--skip-gitignore',
        action='store_true',
        help='Skip updating .gitignore'
    )
    args = parser.parse_args()
    
    print("🔧 Running .env management pre-commit hook...")
    
    # Find git root
    root_dir = find_git_root()
    env_path = root_dir / args.env_file
    
    success = True
    
    # Handle .env.example creation
    if env_path.exists():
        print(f"🔍 Found {env_path}")
        if not create_env_example(env_path):
            success = False
    else:
        print(f"ℹ️  No {args.env_file} file found, skipping .env.example creation")
    
    # Handle .gitignore
    if not args.skip_gitignore:
        if not ensure_gitignore_has_env(root_dir):
            success = False
    
    if success:
        print("🎉 Pre-commit .env management complete!")
        return 0
    else:
        print("💥 Some operations failed")
        return 1


if __name__ == '__main__':
    sys.exit(main())
