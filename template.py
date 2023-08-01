import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "algoTradingBot"

list_of_files = [
    f"data/raw/.gitkeep",
    f"data/processed/.gitkeep",
    f"models/.gitkeep",
    f"notebooks/.gitkeep",
    f"scripts/data_preprocessing.py",
    f"scripts/model_training.py",
    f"scripts/backtesting.py",
    f"scripts/live_trading.py",
    "README.md",
    "requirements.txt",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w", encoding="utf-8") as f:
            pass
            logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filename}")
