# dc_crime

Fast-launch template for data journalism and analysis projects using modern Python tools.

## 🚀 Quick Start

This template is designed to be used with `uv` for fast package management and environment isolation.

### Option 1: Using the Global Command (Recommended)

If you've installed the global command (see setup instructions below):

```bash
# Create a new project from anywhere
new-ds-project my-awesome-analysis

# Navigate to your new project
cd my-awesome-analysis

# Initialize the environment (this creates an isolated virtual environment)
uv sync

# Launch Jupyter Lab
uv run jupyter lab
```

### Option 2: Manual Template Copy

To create a new project using this template manually:

```bash
# Navigate to your Code directory
cd ~/Code

# Copy the template to a new project
cp -r datascience-template housing-crisis-analysis
cd housing-crisis-analysis

# Initialize with uv (this will create a new virtual environment)
uv sync

# Launch Jupyter Lab
uv run jupyter lab
```

### Setting Up the Global Command

To enable the `new-ds-project` command globally:

```bash
# Run the installation script from the template directory
./install-global.sh

# This will install the command to ~/.local/bin/new-ds-project
# Make sure ~/.local/bin is in your PATH
```

## 📁 Project Structure

```
├── data/
│   ├── raw/                    # Original, immutable data
│   ├── processed/              # Cleaned and processed data
│   └── external/               # External data sources
├── notebooks/
│   └── 00_exploratory_data_analysis.ipynb
├── utils/                      # Utility functions and helpers
│   ├── __init__.py
│   └── data_utils.py          # Data processing utilities
├── .env.example                # Environment variables template
├── .env                        # Your environment variables (git-ignored)
├── config.py                   # Project configuration
├── pyproject.toml             # Project dependencies and metadata
└── README.md                  # This file
```

## 🔧 Environment Setup

After creating your new project, set up your environment variables:

```bash
# Copy the environment template
cp .env.example .env

# Edit the .env file with your actual values
# - API keys for data sources
# - Database connection strings  
# - Custom output directories
# - Any project-specific settings
```

**Important:** The `.env` file is automatically git-ignored for security. Never commit API keys or secrets to version control.

### What's in the Environment File?

The `.env.example` file includes settings for:
- **Project paths** - Custom output and figure directories
- **Analysis settings** - Random seeds, DPI settings
- **API keys** - Data sources, news APIs, social media  
- **Database URLs** - PostgreSQL, MongoDB connections
- **Web scraping** - User agents, rate limiting
- **Cloud services** - AWS, email settings

All these variables are automatically loaded by `config.py` using python-dotenv.

## 📦 Pre-installed Packages

This template comes with essential data science packages:

### Core Data Analysis
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **polars** - Fast dataframes (alternative to pandas)
- **pyarrow** - Columnar data format

### Visualization
- **matplotlib** - Basic plotting
- **seaborn** - Statistical visualizations
- **plotly** - Interactive visualizations
- **folium** - Interactive maps and geospatial visualization

### Machine Learning
- **scikit-learn** - Machine learning library

### Geospatial Analysis  
- **geopandas** - Geospatial data analysis (extends pandas)
- **censusdis** - US Census data access
- **folium** - Interactive maps and spatial visualization

### Jupyter Environment
- **jupyter** - Jupyter ecosystem
- **jupyterlab** - Modern Jupyter interface
- **notebook** - Classic Jupyter notebooks
- **ipywidgets** - Interactive widgets

### Utilities
- **requests** - HTTP requests
- **beautifulsoup4** - Web scraping and HTML parsing
- **selenium** - Browser automation for dynamic content
- **python-dotenv** - Environment variable management

### Database & SQL
- **sqlalchemy** - SQL toolkit and ORM
- **psycopg2-binary** - PostgreSQL adapter

## 🎯 VS Code Integration

This template is optimized for VS Code with automatic configuration:
- **Built-in Python formatting** - Clean, consistent code without external dependencies
- **Python environment** - Auto-detected virtual environment  
- **Jupyter support** - Notebooks work seamlessly with VS Code
- **Recommended extensions** - VS Code will suggest helpful extensions

When you open a new project in VS Code, it will:
1. Automatically detect the Python environment created by `uv`
2. Suggest installing recommended extensions
3. Enable format-on-save and import organization for Python files and notebooks
4. Provide a stable, crash-free development experience

## ⚙️ Code Quality & Linting

**Built-in Approach (Default)**
This template uses VS Code's built-in Python formatter for stability and simplicity:
- **Automatic formatting** - Format on save enabled
- **Import organization** - Automatic import sorting  
- **No setup required** - Works immediately
- **Stable** - No external dependencies that can break

**Optional Advanced Tools**
Add these only if you need advanced linting:
1. Install your preferred linter: `uv add --group dev ruff` or `uv add --group dev flake8`
```

Then configure them in your VS Code settings or pyproject.toml as needed.

### Design Philosophy
- **Reliability first** - Built-in tools are crash-free and well-tested
- **Minimal setup** - Projects work immediately without configuration
- **User choice** - Add advanced tools when you actually need them
- **No surprises** - Consistent behavior across all environments

## 🛠 Utility Functions

The `utils/data_utils.py` module provides helpful functions:

```python
from utils import quick_info, plot_distributions, correlation_analysis

# Quick dataset overview
quick_info(df)

# Plot distributions of numeric columns
plot_distributions(df)

# Correlation analysis with heatmap
corr_matrix = correlation_analysis(df)
```

Available utility functions:
- `quick_info()` - Dataset overview and missing values analysis
- `plot_distributions()` - Distribution plots for numeric columns
- `correlation_analysis()` - Correlation matrix with visualization
- `detect_outliers()` - Outlier detection using IQR or Z-score
- `clean_column_names()` - Standardize column names
- `memory_optimization()` - Optimize DataFrame memory usage
- `create_date_features()` - Extract features from datetime columns
- `categorical_analysis()` - Analyze categorical variables

## 🔧 Configuration

Edit `config.py` to customize:
- File paths and directory structure
- Random seeds and reproducibility settings
- Plot styling and figure settings
- Data quality thresholds
- Export formats and settings

## 📊 Getting Started with Analysis

1. **Place your data** in the `data/raw/` directory
2. **Open the starter notebook**: `notebooks/00_exploratory_data_analysis.ipynb`
3. **Modify the data loading section** to load your specific dataset
4. **Run the analysis cells** to get quick insights
5. **Use journalism utilities** for fast exports and publication-ready charts

## 🔄 Development Workflow

1. **Data Exploration**: Start with the provided EDA notebook
2. **Data Cleaning**: Use utilities or create custom functions in `utils/`
3. **Analysis & Visualization**: Develop insights using built-in journalism utilities
4. **Export & Publishing**: Use quick export functions for web publishing
5. **Documentation**: Update README and add docstrings

## ⚡ uv Commands Reference

```bash
# Activate the environment and run commands
uv run python script.py
uv run jupyter lab

# Add new packages
uv add package-name

# Code quality (using built-in VS Code formatter by default)
# Optional: Add advanced linters if needed
uv add --group dev ruff          # Modern linter
uv add --group dev flake8        # Traditional linter

# Update all packages
uv lock --upgrade

# Export requirements
uv export --format requirements-txt > requirements.txt
```

## 📝 Best Practices

1. **Keep raw data immutable** - Never modify files in `data/raw/`
2. **Document your process** - Use markdown cells to explain your analysis
3. **Version control** - Commit notebooks with cleared outputs
4. **Reproducibility** - Set random seeds and document versions
5. **Code organization** - Move reusable code from notebooks to modules
6. **Data validation** - Use `data_fact_check()` utility for journalism accuracy

## 🚀 Advanced Features

### Adding More Packages

```bash
# Data visualization
uv add altair bokeh

# Machine learning
uv add xgboost lightgbm catboost

# Deep learning
uv add torch torchvision tensorflow

# Time series
uv add statsmodels prophet

# Natural language processing
uv add nltk spacy transformers

# Geospatial analysis
uv add geopandas folium
```

### Pre-commit Hooks

```bash
uv add --dev pre-commit
uv run pre-commit install
```

### Jupyter Extensions

```bash
uv add jupyterlab-git nbdime
```

## � Troubleshooting

### VS Code Linting Issues
This template uses VS Code's built-in Python formatter for maximum stability. If you experience:
- **Extension crashes** - The built-in formatter is more reliable than third-party linting extensions
- **Configuration conflicts** - No external linter configuration means fewer compatibility issues
- **Performance problems** - Built-in tools are optimized for VS Code

### Adding Advanced Linting Later
If you need advanced linting features:
1. Install your preferred linter: `uv add --group dev ruff` or `uv add --group dev flake8`
2. Configure it in `.vscode/settings.json` or `pyproject.toml`
3. Remember: advanced tools may introduce stability issues

### Environment Issues
- **Package conflicts**: Use `uv sync --force` to reset the environment
- **Python version**: Ensure you have Python 3.13+ installed
- **VS Code detection**: Restart VS Code if it doesn't detect the virtual environment

## �📄 Open

This template is open source. Feel free to fork and customize.


---

**All set! 🎯📊**