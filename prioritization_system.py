import random

def prioritize_actions(innovations):
    """
    Prioritize actions based on the generated innovations.
    
    Args:
        innovations (dict): The innovations from generate_innovations
        
    Returns:
        list: Prioritized actions with scores
    """
    # Extract data from innovations
    solutions = innovations['solutions']
    technologies = innovations['technologies']
    
    # Generate actions from solutions
    actions = []
    
    # Convert solutions into actionable steps
    for solution in solutions:
        # Extract approach steps from the solution
        approach_text = solution['approach']
        approach_steps = approach_text.split("\n")
        
        # Convert approach steps into actions
        for step in approach_steps:
            if "**" in step:  # Steps are formatted with markdown bold markers
                # Extract the step name and description
                parts = step.split("**: ")
                if len(parts) >= 2:
                    step_name = parts[0].replace("**", "").strip()
                    step_description = parts[1].strip()
                    
                    # Create an action from this step
                    action = {
                        "action": f"{step_name} for {solution['title'].split(' to ')[0]}",
                        "description": step_description,
                        "related_solution": solution['title']
                    }
                    
                    actions.append(action)
    
    # If we don't have enough actions from solutions, add technology implementation actions
    if len(actions) < 5:
        for tech in technologies[:3]:
            action = {
                "action": f"Implement {tech['technology']}",
                "description": f"Integrate {tech['technology']} to enhance capabilities in the {tech['category']} area",
                "related_solution": "Technology Enhancement"
            }
            actions.append(action)
    
    # Ensure we have at least some actions
    if not actions:
        generic_actions = [
            {
                "action": "Conduct Needs Assessment",
                "description": "Analyze current state and identify specific requirements",
                "related_solution": "Initial Planning"
            },
            {
                "action": "Develop Prototype",
                "description": "Create initial version to validate core concepts",
                "related_solution": "Solution Development"
            },
            {
                "action": "Gather User Feedback",
                "description": "Collect and analyze user responses to improve solution",
                "related_solution": "Validation"
            },
            {
                "action": "Implement Core Features",
                "description": "Build the essential functionalities of the solution",
                "related_solution": "Development"
            },
            {
                "action": "Deploy and Monitor",
                "description": "Launch the solution and track performance metrics",
                "related_solution": "Implementation"
            }
        ]
        actions = generic_actions
    
    # Add metrics to each action
    prioritized_actions = []
    
    for action in actions:
        # Score impact (1-10, higher is better)
        impact = random.uniform(5, 10)
        
        # Score difficulty (1-10, lower is easier)
        difficulty = random.uniform(3, 8)
        
        # Calculate priority score (impact / difficulty)
        priority_score = impact / (difficulty * 0.5)
        
        # Assign a timeframe
        timeframes = ["Short-term (1-3 months)", "Medium-term (3-6 months)", "Long-term (6+ months)"]
        weights = [0.5, 0.3, 0.2]  # Favor shorter timeframes
        timeframe = random.choices(timeframes, weights=weights)[0]
        
        # Assign resources needed
        resource_options = [
            "Development team", "Product management", "UX/UI design", 
            "Data science expertise", "Subject matter experts", 
            "Testing resources", "Infrastructure support"
        ]
        num_resources = random.randint(1, 3)
        resources = ", ".join(random.sample(resource_options, num_resources))
        
        # Create the prioritized action
        prioritized_action = {
            "action": action["action"],
            "description": action["description"],
            "impact": impact,
            "difficulty": difficulty,
            "priority_score": priority_score,
            "timeframe": timeframe,
            "resources": resources,
            "related_solution": action["related_solution"]
        }
        
        prioritized_actions.append(prioritized_action)
    
    # Sort actions by priority score (highest first)
    prioritized_actions.sort(key=lambda x: x["priority_score"], reverse=True)
    
    return prioritized_actions
