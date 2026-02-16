from classifier import classify_pattern
from action_mapper import get_suggested_action

text = "I keep thinking about starting but I end up scrolling instead"

result = classify_pattern(text)

label = result["label"]
confidence = result["confidence"]

action = get_suggested_action(label)

print("Label:", label)
print("Confidence:", confidence)
print("Suggested Action:", action)


