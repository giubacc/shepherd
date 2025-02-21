# Development

This section provides instructions for setting up the development environment
for contributors.

## Prerequisites

Ensure you have the following installed on your system:

- Python 3.12 or later
- `pip` (Python package installer)
- `virtualenv` (optional but recommended for managing dependencies)

To install these on Ubuntu, run:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone git@github.com:LunaticFringers/shepherd.git
   cd shepherd
   ```

2. **Create a Virtual Environment**

   Use a virtual environment to isolate dependencies:

   ```bash
   cd src
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   Install the required Python packages from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure the necessary tools are installed locally in your Python environment:

   ```bash
   pip install black isort pyright pytest pytest-cov pre-commit
   ```

4. **Verify Installation**

   Test the CLI to ensure it works:

   ```bash
   python shpdctl.py --help
   ```

   You should see the list of available commands and options.

5. **Run the CLI**

   You can now use the CLI:

   ```bash
   python shpdctl.py <command> [options]
   ```

## Lints & Checks

1. **pre-commit**

   Run pre-commit manually:

   ```bash
   pre-commit run --all-files
   ```

   Install pre-commit:

   ```bash
   pre-commit install
   ```

2. **Black**

   Format your code manually:

   ```bash
   black .
   ```

3. **Isort**

   Sort imports manually by running:

   ```bash
   isort .
   ```

4. **Pyright**

   Run type checking:

   ```bash
   pyright
   ```

5. **Pytest**

   Run tests with coverage:

   ```bash
   pytest
   ```
