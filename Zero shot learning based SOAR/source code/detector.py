from transformers import pipeline

classifier = pipeline("zero-shot-classification")

labels = [
    "SQL Injection",
    "Cross Site Scripting",
    "Brute Force Attack",
    "Normal Traffic"
]

def detect(log):
    ip = log.split(" ")[0]
    result = classifier(log, labels)

    return ip, result["labels"][0], result["scores"][0]
