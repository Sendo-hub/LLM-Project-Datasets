
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

## Example usage

from src.data_utils import load_jsonl, build_prompt, evaluate_predictions

samples = load_jsonl("/content/drive/MyDrive/llm_group_project/data/processed/gsm8k_test.jsonl")
prompt = build_prompt(samples[0], prompt_type="base")
print(prompt)

## Notes
- Numeric datasets: GSM8K, SVAMP
- Multiple-choice dataset: AQuA-RAT
- Exact-match evaluation is provided in src/data_utils.py
