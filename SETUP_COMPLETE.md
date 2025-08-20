# 🎯 Data Science Template Setup Notes

## What We've Built

This is our complete data science project template system using `uv` for package management.

### 📦 Template Features
- **Fast Environment Management**: Uses `uv` for package installation
- **Complete Data Science Stack**: pandas, numpy, matplotlib, seaborn, plotly, scikit-learn, jupyter, polars, pyarrow
- **Code Quality**: Built-in VS Code formatting for stability and consistency
- **Project Structure**: Organized directories for data, notebooks, and utilities
- **Starter Notebook**: Data analysis notebook template with journalism examples
- **Journalism Utilities**: Helper functions for fast publication workflows
- **Git Integration**: Starter .gitignore and automated git initialization

### 🚀 Quick Usage

#### Method 1: Global Command (Recommended)
```bash
new-ds-project my-awesome-project
```
*Set to run from any directory - projects are always created in `~/Code/`*

#### Method 2: Direct Script
```bash
cd ~/Code
./datascience-template/new-ds-project.sh my-awesome-project
```

#### Method 3: Manual Copy
```bash
cd ~/Code
cp -r datascience-template my-awesome-project
cd my-awesome-project
uv sync
```

### 📁 Project Folder Structure Created
```
my-awesome-project/
├── data/
│   ├── raw/                    # Original data files
│   ├── processed/              # Cleaned data
│   └── external/               # External data sources
├── notebooks/
│   └── 00_exploratory_data_analysis.ipynb
├── utils/                      # Helper functions
├── config.py                   # Project configuration
├── pyproject.toml             # Dependencies
└── README.md                  # Project documentation
```

### 🔧 Essential Commands

After creating a project:
```bash
cd my-awesome-project    # Navigate to project
uv sync                  # Install dependencies
uv run jupyter lab       # Start Jupyter Lab to run in browser
uv add package-name      # Add any new or additional packages
uv run python script.py  # Run Python scripts from terminal

# Code quality (built-in VS Code formatting)
# No additional commands needed - format-on-save is enabled

# Optional: Add advanced linting if desired
uv add --group dev ruff  # Modern fast linter
uv add --group dev flake8  # Traditional linter
```

### 📊 Starting with these installed Packages
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing  
- **matplotlib & seaborn** - Data visualization
- **plotly** - Interactive visualizations
- **folium** - Interactive maps and geospatial visualization
- **scikit-learn** - Machine learning
- **jupyter & jupyterlab** - Interactive development
- **polars** - Fast dataframes
- **pyarrow** - Columnar data format
- **requests** - HTTP requests
- **geopandas** - Geospatial data analysis
- **censusdis** - US Census data access
- **beautifulsoup4 & selenium** - Web scraping
- **sqlalchemy** - Database connections

### 🛠 Utility Functions Available
```python
# Data analysis utilities
from utils import quick_info, plot_distributions, correlation_analysis

# Journalism utilities  
from utils import quick_export_for_web, create_story_charts, data_fact_check

# Quick dataset overview
quick_info(df)

# Data validation for journalism
data_fact_check(df)

# Publication-ready charts
create_story_charts(df, 'column_name', save_filename='story_chart')

# Export for web publishing
quick_export_for_web(df, 'data_export', 'csv')
```

## Next Steps

1. **Create your first project**: `new-ds-project my-first-analysis`
2. **Add your data**: Place data files in `data/raw/`
3. **Start analyzing**: Open the 00_exploratory_data_analysis.ipynb notebook and begin your analysis
4. **Customize**: Add any additional packages via `uv add package-name`

## VS Code Integration

The template works seamlessly with VS Code and includes pre-configured settings:
- **Automatic Python environment detection** - Virtual environment is auto-detected
- **Built-in formatting** - Python formatting works automatically
- **Jupyter notebook support** - Code cells are formatted on save
- **Recommended extensions** - VS Code suggests helpful extensions
- **Format on save** - Code is automatically formatted when you save

### First Time Setup in VS Code
1. Open your new project folder in VS Code
2. Install recommended extensions when prompted
3. VS Code will automatically use the project's Python environment
4. Formatting will work immediately in both `.py` files and `.ipynb` notebooks

#```

## 🔧 Code Quality Philosophy

This template prioritizes **stability and reliability** over complex tooling:

### Built-in Approach
- **VS Code's built-in Python formatter** - Rock solid, no crashes
- **Automatic format-on-save** - Consistent code style without setup
- **Import organization** - Clean imports without external dependencies
- **Jupyter integration** - Seamless notebook formatting

### Why No Complex Linters?
- **Stability first** - External linting extensions can crash or conflict
- **Immediate productivity** - Projects work perfectly right away
- **User choice** - Add advanced tools only when you actually need them
- **Maintenance-free** - Fewer moving parts to break or update

### Adding Advanced Tools Later
When you're ready for advanced linting:
```bash
uv add --group dev ruff        # Modern fast linter
uv add --group dev flake8      # Traditional Python linter  
uv add --group dev black       # Opinionated code formatter
```

## Troubleshooting

**If `new-ds-project` command doesn't work:**
```bash
# Reload your shell
source ~/.zshrc

# Or use the direct path
~/Code/datascience-template/new-ds-project.sh my-project
```

**If uv isn't found:**
```bash
# Add to PATH
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

---

**All set! 🎯📊**