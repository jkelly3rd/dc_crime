"""
Configuration file for data science project.

Contains paths, settings, and parameters used throughout the project.
Loads environment variables from .env file if it exists.
"""

import os
from pathlib import Path

# Load environment variables from .env file if it exists
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # dotenv not available, skip loading
    pass

# Project structure
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / os.getenv('OUTPUT_DIR', 'data/processed')
EXTERNAL_DATA_DIR = DATA_DIR / "external"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
FIGURES_DIR = PROJECT_ROOT / os.getenv('FIGURE_DIR', 'notebooks/figures')
SRC_DIR = PROJECT_ROOT / "src"
UTILS_DIR = PROJECT_ROOT / "utils"
TESTS_DIR = PROJECT_ROOT / "tests"

# Ensure directories exist
for dir_path in [DATA_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, EXTERNAL_DATA_DIR, FIGURES_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

# Data settings
RANDOM_SEED = int(os.getenv('RANDOM_SEED', 42))
TEST_SIZE = 0.2
VALIDATION_SIZE = 0.2

# Plot settings
FIGURE_SIZE = (12, 8)
DPI = int(os.getenv('FIGURE_DPI', 300))
PLOT_STYLE = 'seaborn-v0_8'

# File formats
DEFAULT_CSV_ENCODING = 'utf-8'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# API settings (if applicable)
API_TIMEOUT = 30
MAX_RETRIES = 3

# Logging configuration
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Model settings
CV_FOLDS = 5
SCORING_METRIC = 'accuracy'  # or 'roc_auc', 'f1', etc.

# Data quality thresholds
MISSING_THRESHOLD = 0.5  # Drop columns with more than 50% missing values
CORRELATION_THRESHOLD = 0.95  # Flag highly correlated features
OUTLIER_THRESHOLD = 3  # Z-score threshold for outlier detection
