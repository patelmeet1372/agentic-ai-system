from app.models.goal_interpreter import interpret_goal

def test_interpret_goal():
    user_input = "I need to finish my report by tomorrow."
    goal = interpret_goal(user_input)
    assert goal is not None  # Replace with expected label if known