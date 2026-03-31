
import re
import json

def load_jsonl(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    return data

def build_prompt(sample, prompt_type="base"):
    question = sample["question"]
    answer_type = sample["answer_type"]
    options = sample["options"]

    if answer_type == "multiple_choice" and options:
        options_text = "\n".join(options)
        core = f"Question: {question}\nOptions:\n{options_text}\n"
    else:
        core = f"Question: {question}\n"

    if prompt_type == "base":
        return core + "Answer:"
    elif prompt_type == "cot":
        return core + "Let's think step by step, then provide the final answer.\nAnswer:"
    elif prompt_type == "short_cot":
        return core + "Reason briefly and give the final answer only.\nAnswer:"
    else:
        raise ValueError(f"Unknown prompt_type: {prompt_type}")

def normalize_text(text):
    if text is None:
        return ""
    text = str(text)
    text = text.strip()
    text = " ".join(text.split())
    return text

def normalize_numeric_string(s):
    s = str(s).strip()
    s = s.replace(",", "")
    s = s.replace("$", "")
    s = s.strip()
    if s.endswith("."):
        s = s[:-1].strip()
    return s

def normalize_choice_answer(s):
    s = normalize_text(s).upper()
    match = re.search(r"\b([A-E])\b", s)
    if match:
        return match.group(1)
    return s

def normalize_gold_answer(sample):
    if sample["answer_type"] == "multiple_choice":
        return normalize_choice_answer(sample["answer"])
    else:
        return normalize_numeric_string(sample["answer"])

def normalize_pred_answer(pred, answer_type):
    if answer_type == "multiple_choice":
        return normalize_choice_answer(pred)
    else:
        return normalize_numeric_string(pred)

def exact_match_score(pred, gold):
    return int(pred == gold)

def evaluate_predictions(samples, predictions):
    assert len(samples) == len(predictions), "samples and predictions must have the same length"

    results = []
    correct = 0

    for sample, pred in zip(samples, predictions):
        gold = normalize_gold_answer(sample)
        pred_norm = normalize_pred_answer(pred, sample["answer_type"])
        is_correct = exact_match_score(pred_norm, gold)
        correct += is_correct

        results.append({
            "id": sample["id"],
            "dataset": sample["dataset"],
            "split": sample["split"],
            "question": sample["question"],
            "gold_answer": gold,
            "prediction": pred,
            "prediction_normalized": pred_norm,
            "correct": bool(is_correct)
        })

    accuracy = correct / len(samples) if len(samples) > 0 else 0.0
    return accuracy, results
