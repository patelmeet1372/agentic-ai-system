from transformers import pipeline

# Initialize a text classification pipeline
goal_interpreter = pipeline("text-classification", model="distilbert-base-uncased")

def interpret_goal(user_input):
    # Use the model to interpret the user's goal
    result = goal_interpreter(user_input)
    return result[0]['label']