
# LLM Group Project - Dataset Preparation

## Directory
- data/processed/: processed JSONL files
- outputs/stats/: cleaning stats and dataset stats
- src/data_utils.py: common loader / prompt / evaluation utils

## Unified JSONL Schema
Each sample has fields:
- id
- dataset
- split
- question
- answer
- rationale
- options
- answer_type

## Main processed files
- gsm8k_train.jsonl
- gsm8k_validation.jsonl
- gsm8k_test.jsonl
- svamp_train.jsonl
- svamp_validation.jsonl
- svamp_test.jsonl
- aqua_rat_train.jsonl
- aqua_rat_validation.jsonl
- aqua_rat_test.jsonl
- merged_train.jsonl
- merged_validation.jsonl
- merged_test.jsonl

## Notes
- Numeric datasets: GSM8K, SVAMP
- Multiple-choice dataset: AQuA-RAT
- Exact-match evaluation is provided in src/data_utils.py
