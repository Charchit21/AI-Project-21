
feeling_lexicon = {
    'delicious': 2,
    'great': 2,
    'love': 2,
    'good': 1,
    'nice': 1,
    'okay': 0,
    'fine': 0,
    'bad': -1,
    'awful': -2,
    'disgusting': -2,
    'horrible': -2,
    'cold': -1,
    'salty': -1
}

test_dataset = [
    {"comment": "The food was absolutely delicious and great!", "label": "HAPPY"},
    {"comment": "I did not think the soup was good.", "label": "UNHAPPY"},
    {"comment": "The sandwich was okay, nothing special.", "label": "OK"},
    {"comment": "Completely disgusting and awful service.", "label": "UNHAPPY"},
    {"comment": "It was not bad at all, actually pretty nice.", "label": "HAPPY"},
    {"comment": "The coffee was cold and horrible.", "label": "UNHAPPY"}
]

def analyze_comment(comment):
    """
    Analyzes a comment through 3 parts:
    1. Cleans the comment into lowercase words.
    2. Adds up word points, applying a "not" flip if preceded by "not".
    3. Turns the final score into HAPPY, UNHAPPY, or OK[cite: 5].
    """
    words = comment.lower().replace('.', '').replace(',', '').replace('!', '').split()
    
    score = 0
    not_flag = False
    
    for word in words:
        if word == "not":
            not_flag = True
            continue
            
        if word in feeling_lexicon:
            points = feeling_lexicon[word]
            
            if not_flag:
                points = -points
                not_flag = False 
            score += points
        else:
            not_flag = False

    if score >= 2:
        return "HAPPY"
    elif score <= -1:
        return "UNHAPPY"
    else:
        return "OK"

def evaluate_mood_meter(dataset):
    mistakes = 0
    print("==================================================")
    print("        CANTEEN COMMENT BOX: MOOD METER           ")
    print("==================================================\n")
    
    for i, data in enumerate(dataset):
        comment = data["comment"]
        true_label = data["label"]
        
        predicted_label = analyze_comment(comment)
        
        status = "MATCH" if predicted_label == true_label else "MISTAKE"
        if status == "MISTAKE":
            mistakes += 1
            
        print(f"Comment {i+1}: \"{comment}\"")
        print(f"  -> True: {true_label} | Predicted: {predicted_label} [{status}]")
        print("-" * 50)
        
    print(f"\nTotal Mistakes Made by Program: {mistakes} out of {len(dataset)}.")

if __name__ == "__main__":
    evaluate_mood_meter(test_dataset)