# LLM Group Project - Dataset Preparation

## Overview
This folder contains the dataset preparation pipeline for three mathematical reasoning benchmarks:

- GSM8K
- SVAMP
- AQuA-RAT

The goal is to convert heterogeneous raw datasets into a unified JSONL format that can be directly used for:
- baseline inference
- prompt optimization
- PEFT / LoRA fine-tuning
- evaluation and reporting

---

## Data Sources

### GSM8K
Loaded from Hugging Face:
- `openai/gsm8k`

### SVAMP
Loaded from Hugging Face:
- `ChilleD/SVAMP`

### AQuA-RAT
Loaded from the official GitHub release:
- `train.json`
- `dev.json`
- `test.json`

We use the official AQuA multiple-choice version instead of the prompt-completion Hugging Face variant.

---

## Directory Structure

- `data/raw/`
  - raw downloaded files
- `data/processed/`
  - processed JSONL files
- `outputs/stats/`
  - cleaning statistics and dataset summary tables
- `src/data_utils.py`
  - common utilities for loading data, building prompts, and evaluating predictions

---

## Unified JSONL Schema

Each processed sample contains the following fields:

- `id`
- `dataset`
- `split`
- `question`
- `answer`
- `rationale`
- `options`
- `answer_type`

---

## Dataset-specific Processing

### GSM8K
- Use original `question`
- Extract final answer from the `####` pattern in `answer`
- Preserve the preceding reasoning text as `rationale`

### SVAMP
- Use `question_concat` when available, otherwise build the question from `Body + Question`
- Use `Answer` as the gold answer
- Preserve `Equation` as `rationale`

### AQuA-RAT
- Use official GitHub version with fields:
  - `question`
  - `options`
  - `rationale`
  - `correct`
- Concatenate `options` into the `question` text
- Rename `correct` to `answer`
- Preserve the original option list in `options`

---

## Split Policy

### GSM8K
- keep official train/test
- create validation from train
- use a reduced test subset for efficient evaluation

### SVAMP
- keep official train/test
- create validation from train
- use a reduced test subset for efficient evaluation

### AQuA-RAT
- keep official GitHub splits directly:
  - `train.json` -> train
  - `dev.json` -> validation
  - `test.json` -> test
- no test expansion

---

## Main Processed Files

- `gsm8k_train.jsonl`
- `gsm8k_validation.jsonl`
- `gsm8k_test.jsonl`

- `svamp_train.jsonl`
- `svamp_validation.jsonl`
- `svamp_test.jsonl`

- `aqua_rat_train.jsonl`
- `aqua_rat_validation.jsonl`
- `aqua_rat_test.jsonl`

- `merged_train.jsonl`
- `merged_validation.jsonl`
- `merged_test.jsonl`

- `*_debug.jsonl`
  - small debug subsets for quick testing

---

## Statistics Files

Saved under `outputs/stats/`:

- `cleaning_stats.csv`
- `dataset_stats.csv`
- `report_summary_table.csv`
- `split_strategy.csv`

These files summarize:
- raw vs cleaned sample counts
- filtering and deduplication results
- split sizes
- average question / answer lengths
- dataset-level report tables