from src.decision.classifier import classify_pattern
from src.decision.action_mapper import get_suggested_action


def get_next_move(user_input):

    # Step 1: classify input
    result = classify_pattern(user_input)

    label = result["label"]
    confidence = result["confidence"]
    confidence = f"{confidence:.0%}"

    # Step 2: retrieve aligned action
    action = get_suggested_action(label)

    # Step 3: return structured output
    return {
        "input": user_input,
        "label": label,
        "confidence": confidence,
        "next_move": action
    }

