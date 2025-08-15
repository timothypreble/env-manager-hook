from setuptools import setup, find_packages

setup(
    name="env-manager-hook",
    version="1.0.0",
    description="Pre-commit hook to manage .env files and .gitignore",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/env-manager-hook",
    py_modules=["env_manager"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "env-manager=env_manager:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Version Control :: Git",
    ],
)
