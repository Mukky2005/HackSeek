"""
Context-Aware Hackathon Tips Generator

This module analyzes problem statements and provides tailored hackathon tips
relevant to the specific problem domain and characteristics.
"""

import spacy
from hackathon_tips import (get_hackathon_planning_tips, get_technical_execution_strategies,
                           get_presentation_strategies, get_judge_perspective_insights,
                           get_hackathon_categories_info, get_pitfall_avoidance_tips)

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except:
    # If model isn't available, use a simpler pipeline
    nlp = spacy.blank("en")
    nlp.add_pipe("sentencizer")

# Domain keywords mapping
DOMAIN_KEYWORDS = {
    "health": ["healthcare", "medical", "health", "patient", "doctor", "hospital", "wellness", "diagnosis"],
    "education": ["education", "learning", "student", "school", "teacher", "classroom", "academic", "curriculum"],
    "environment": ["environment", "climate", "sustainability", "green", "eco", "pollution", "conservation", "renewable"],
    "finance": ["finance", "banking", "payment", "money", "budget", "investment", "financial", "transaction"],
    "transportation": ["transportation", "vehicle", "traffic", "commute", "mobility", "transit", "transport", "travel"],
    "social_impact": ["social", "community", "impact", "nonprofit", "equality", "inclusive", "accessibility", "underserved"],
    "artificial_intelligence": ["ai", "machine learning", "deep learning", "neural", "algorithm", "intelligence", "prediction", "automation"],
    "blockchain": ["blockchain", "crypto", "nft", "token", "decentralized", "distributed", "ledger", "web3"],
    "gaming": ["game", "gaming", "player", "interactive", "play", "entertainment", "engagement", "immersive"],
    "iot": ["iot", "sensor", "smart device", "connected", "internet of things", "embedded", "monitoring", "automation"],
    "ar_vr": ["ar", "vr", "augmented", "virtual", "reality", "immersive", "3d", "spatial"],
    "data_science": ["data", "analytics", "statistics", "visualization", "insight", "prediction", "analysis", "dashboard"],
}

# Technical approach keywords mapping
TECHNICAL_APPROACH = {
    "mobile": ["mobile", "app", "smartphone", "ios", "android", "tablet", "responsive", "touch"],
    "web": ["web", "website", "browser", "frontend", "backend", "html", "javascript", "responsive"],
    "api": ["api", "integration", "endpoint", "service", "microservice", "interface", "request", "response"],
    "database": ["database", "storage", "query", "data management", "sql", "nosql", "record", "persistence"],
    "machine_learning": ["model", "train", "predict", "classify", "regression", "feature", "dataset", "algorithm"],
    "visualization": ["visualization", "chart", "dashboard", "graph", "display", "map", "plot", "infographic"],
    "hardware": ["hardware", "device", "physical", "sensor", "bluetooth", "electronic", "prototype", "component"],
    "cloud": ["cloud", "aws", "azure", "google cloud", "serverless", "saas", "paas", "hosted"],
}

# Target user keywords mapping
TARGET_USERS = {
    "consumers": ["consumer", "user", "customer", "client", "public", "individual", "person", "people"],
    "businesses": ["business", "company", "organization", "enterprise", "corporate", "industry", "firm", "commercial"],
    "government": ["government", "public sector", "policy", "regulation", "compliance", "agency", "official", "civic"],
    "healthcare_providers": ["hospital", "clinic", "doctor", "nurse", "physician", "caregiver", "medical staff", "provider"],
    "educators": ["teacher", "professor", "instructor", "educator", "faculty", "school", "university", "academic"],
    "researchers": ["researcher", "scientist", "academic", "study", "investigation", "laboratory", "publication", "finding"],
}

def analyze_problem_domain(problem_statement, problem_analysis=None):
    """
    Analyze the problem statement to determine relevant domain areas.
    
    Args:
        problem_statement (str): The problem statement text
        problem_analysis (dict, optional): Pre-existing problem analysis
        
    Returns:
        dict: Domain relevance scores and other analysis results
    """
    # Process text if problem_analysis not provided
    if not problem_analysis:
        doc = nlp(problem_statement.lower())
        text = problem_statement.lower()
    else:
        text = problem_analysis.get("text", "").lower()
        doc = problem_analysis.get("doc")
        if not doc:
            doc = nlp(text)
    
    # Calculate domain relevance scores
    domain_scores = {}
    for domain, keywords in DOMAIN_KEYWORDS.items():
        score = 0
        for keyword in keywords:
            if keyword.lower() in text:
                score += text.count(keyword.lower()) * 2
        
        # Add scores for token lemmas to catch variations
        if doc:
            for token in doc:
                if token.lemma_.lower() in keywords:
                    score += 1
        
        domain_scores[domain] = score
    
    # Calculate technical approach relevance
    approach_scores = {}
    for approach, keywords in TECHNICAL_APPROACH.items():
        score = 0
        for keyword in keywords:
            if keyword.lower() in text:
                score += text.count(keyword.lower()) * 2
        
        # Add scores for token lemmas
        if doc:
            for token in doc:
                if token.lemma_.lower() in keywords:
                    score += 1
        
        approach_scores[approach] = score
    
    # Calculate target user relevance
    user_scores = {}
    for user_type, keywords in TARGET_USERS.items():
        score = 0
        for keyword in keywords:
            if keyword.lower() in text:
                score += text.count(keyword.lower()) * 2
        
        # Add scores for token lemmas
        if doc:
            for token in doc:
                if token.lemma_.lower() in keywords:
                    score += 1
        
        user_scores[user_type] = score
    
    # Get top domains, approaches, and user types (normalize to ensure we have selections)
    top_domains = sorted(domain_scores.items(), key=lambda x: x[1], reverse=True)
    top_approaches = sorted(approach_scores.items(), key=lambda x: x[1], reverse=True)
    top_users = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
    
    # Default to top scoring or first item if all scores are 0
    primary_domain = top_domains[0][0] if top_domains[0][1] > 0 else list(DOMAIN_KEYWORDS.keys())[0]
    primary_approach = top_approaches[0][0] if top_approaches[0][1] > 0 else list(TECHNICAL_APPROACH.keys())[0]
    primary_user = top_users[0][0] if top_users[0][1] > 0 else list(TARGET_USERS.keys())[0]
    
    return {
        "domain_scores": domain_scores,
        "approach_scores": approach_scores,
        "user_scores": user_scores,
        "primary_domain": primary_domain,
        "primary_approach": primary_approach,
        "primary_user": primary_user,
        "top_domains": [domain for domain, score in top_domains[:3] if score > 0],
        "top_approaches": [approach for approach, score in top_approaches[:3] if score > 0],
        "top_users": [user for user, score in top_users[:3] if score > 0]
    }

def get_domain_specific_tip(domain):
    """Get a specific tip for the given domain"""
    domain_tips = {
        "health": {
            "title": "Healthcare Data Privacy",
            "description": "Pay special attention to HIPAA compliance and health data privacy.",
            "detail": "Healthcare hackathons require strict attention to data privacy regulations. Use synthetic or properly anonymized data, implement robust encryption, and document your compliance measures clearly for judges."
        },
        "education": {
            "title": "Educational Accessibility",
            "description": "Ensure your educational solution works across different learning environments and abilities.",
            "detail": "Educational hackathon projects should consider diverse learning needs. Implement accessibility features, support offline use cases, and design for various technical literacy levels to maximize your solution's impact."
        },
        "environment": {
            "title": "Environmental Impact Metrics",
            "description": "Quantify your solution's environmental benefits with clear metrics.",
            "detail": "Environmental hackathon projects need concrete impact measures. Calculate carbon reduction, resource conservation, or efficiency improvements your solution provides, and visualize these metrics in your presentation."
        },
        "finance": {
            "title": "Financial Security First",
            "description": "Prioritize security and compliance in financial technology solutions.",
            "detail": "For fintech hackathons, judges will scrutinize security aspects. Implement proper authentication, encryption for sensitive data, and be prepared to explain your security architecture during Q&A."
        },
        "transportation": {
            "title": "Multimodal Transportation Thinking",
            "description": "Consider how your solution integrates with various transportation methods.",
            "detail": "Transportation hackathon winners often address connectivity between different modes of transport. Think beyond single vehicles and demonstrate how your solution creates a cohesive mobility ecosystem."
        },
        "social_impact": {
            "title": "Inclusive Design Process",
            "description": "Incorporate perspectives from affected communities in your design process.",
            "detail": "Social impact hackathons value community-centered design. Reference specific community needs your solution addresses and explain how you would involve community members in refining your approach."
        },
        "artificial_intelligence": {
            "title": "AI Ethics and Bias Consideration",
            "description": "Address potential AI biases and ethical concerns proactively.",
            "detail": "AI hackathon judges look for responsible technology use. Identify potential bias sources in your model, explain mitigation strategies, and demonstrate thoughtfulness about the ethical implications of your solution."
        },
        "blockchain": {
            "title": "Blockchain Practicality",
            "description": "Focus on practical blockchain applications with clear advantages over traditional approaches.",
            "detail": "Successful blockchain hackathon projects demonstrate why decentralization offers tangible benefits for their specific use case. Clearly articulate the problem that centralization creates and how your blockchain solution resolves it."
        },
        "gaming": {
            "title": "Rapid Gameplay Prototyping",
            "description": "Create a playable prototype that demonstrates core mechanics quickly.",
            "detail": "Gaming hackathons require demonstrable gameplay. Focus on one innovative mechanic rather than multiple features, use placeholder assets, and ensure judges can experience the core interaction loop in under a minute."
        },
        "iot": {
            "title": "IoT Simulation Fallback",
            "description": "Prepare software simulations alongside hardware demos for reliability.",
            "detail": "IoT hackathons face hardware reliability challenges. Develop a software simulation that demonstrates your concept's functionality even if physical components encounter issues during presentation."
        },
        "ar_vr": {
            "title": "AR/VR Demo Contingencies",
            "description": "Create fallback demonstration options for AR/VR experiences.",
            "detail": "AR/VR hackathons often face demo challenges. Prepare a video recording of your experience, screenshots of key interactions, and a simplified web version to ensure judges understand your concept regardless of technical difficulties."
        },
        "data_science": {
            "title": "Data Storytelling Focus",
            "description": "Emphasize insights and narrative over technical implementation details.",
            "detail": "Data science hackathon winners excel at communication. Create compelling visualizations, focus on the story your data tells, and translate technical findings into business or social impact that non-technical judges will appreciate."
        }
    }
    
    # Return specific domain tip or a general one if domain not found
    return domain_tips.get(domain, {
        "title": "Cross-Domain Innovation",
        "description": "Look for inspiration in adjacent fields to your problem domain.",
        "detail": "Some of the most innovative hackathon projects apply techniques from seemingly unrelated domains. Research similar challenges in other industries and consider how their solutions might apply to your problem with creative adaptation."
    })

def get_approach_specific_tip(approach):
    """Get a specific tip for the given technical approach"""
    approach_tips = {
        "mobile": {
            "title": "Mobile Device Testing",
            "description": "Test your mobile app on multiple devices and screen sizes.",
            "detail": "Mobile hackathon projects should function across different devices. Use responsive design, test on at least two different screen sizes, and consider offline functionality for a more robust demonstration."
        },
        "web": {
            "title": "Browser Compatibility",
            "description": "Ensure your web application works in different browsers.",
            "detail": "Web hackathon projects should be tested in at least Chrome and one other browser. Keep a local version ready in case of internet connectivity issues, and optimize for the presentation environment's screen resolution."
        },
        "api": {
            "title": "API Documentation",
            "description": "Create clear documentation for your API with example requests and responses.",
            "detail": "API-focused hackathon projects should include simple documentation. Prepare Postman collections or curl examples that judges can run, and create visualizations of your API architecture to clarify your implementation."
        },
        "database": {
            "title": "Database Performance",
            "description": "Optimize database queries and demonstrate scalability considerations.",
            "detail": "Database hackathon projects should address performance. Implement indexing for common queries, prepare a sample dataset large enough to demonstrate real-world conditions, and document your schema design decisions."
        },
        "machine_learning": {
            "title": "Model Interpretability",
            "description": "Make your machine learning models interpretable and explainable.",
            "detail": "ML hackathon projects benefit from transparency. Include feature importance visualizations, explain your training methodology, and prepare non-technical explanations of how your model arrives at its conclusions."
        },
        "visualization": {
            "title": "Interactive Visualizations",
            "description": "Create interactive data visualizations that judges can explore.",
            "detail": "Visualization hackathon projects should allow interaction. Implement filtering, drilling down into data points, and different view options to let judges explore the data themselves and discover the insights you've identified."
        },
        "hardware": {
            "title": "Hardware Backup Plans",
            "description": "Prepare for hardware failures with backup components or simulations.",
            "detail": "Hardware hackathon projects face reliability risks. Bring spare components, prepare a video demonstration as backup, and practice quick troubleshooting of common issues that might arise during presentation."
        },
        "cloud": {
            "title": "Cloud Cost Optimization",
            "description": "Address cost efficiency in your cloud architecture design.",
            "detail": "Cloud-based hackathon projects should consider economics. Explain your resource optimization strategies, serverless function design, and how your architecture would scale cost-effectively beyond the prototype stage."
        }
    }
    
    # Return specific approach tip or a general one if approach not found
    return approach_tips.get(approach, {
        "title": "Technology Selection Justification",
        "description": "Be prepared to justify your technology choices against alternatives.",
        "detail": "Judges often ask why you selected particular technologies. Research the strengths and weaknesses of your chosen approach compared to alternatives, and prepare a concise explanation of why your selection is optimal for your specific problem."
    })

def get_complexity_specific_tip(complexity_score):
    """Get a specific tip based on problem complexity"""
    if complexity_score < 0.3:
        return {
            "title": "Execution Over Complexity",
            "description": "For simpler problems, focus on exceptional execution rather than overcomplicating.",
            "detail": "When tackling a straightforward problem, judges look for outstanding implementation quality. Focus on user experience polish, robust testing, and clearly communicating your solution's excellence in solving the specific problem."
        }
    elif complexity_score < 0.7:
        return {
            "title": "Balanced Scope Management",
            "description": "For moderately complex problems, prioritize critical features and communicate tradeoffs.",
            "detail": "Medium-complexity problems require thoughtful scoping. Create a tiered feature list with must-haves and nice-to-haves, focus on completing core functionality flawlessly, and clearly explain your prioritization decisions to judges."
        }
    else:
        return {
            "title": "Complexity Decomposition",
            "description": "For highly complex problems, break down your approach into manageable components.",
            "detail": "Complex problems benefit from clear architecture. Create visual diagrams showing how you've modularized the challenge, focus on proving the most innovative or difficult component works, and outline how the pieces connect into a comprehensive solution."
        }

def get_user_specific_tip(user_type):
    """Get a specific tip for the given user type"""
    user_tips = {
        "consumers": {
            "title": "Consumer Onboarding Flow",
            "description": "Design a frictionless first-time user experience for consumer products.",
            "detail": "Consumer-focused hackathon projects should prioritize intuitive onboarding. Design for zero learning curve, implement progressive disclosure of features, and create a compelling 'aha moment' that judges will experience during your demo."
        },
        "businesses": {
            "title": "Business ROI Focus",
            "description": "Quantify the business value and return on investment for B2B solutions.",
            "detail": "B2B hackathon projects should demonstrate economic impact. Calculate potential time/cost savings, revenue generation, or efficiency improvements your solution provides, and translate these into compelling ROI estimates for business adoption."
        },
        "government": {
            "title": "Public Sector Compliance",
            "description": "Address regulatory requirements and accessibility standards for government solutions.",
            "detail": "Government-focused hackathon projects must consider compliance. Reference relevant regulations or standards (like ADA, COPPA, etc.), implement basic accessibility features, and explain how your solution fits within existing governmental frameworks."
        },
        "healthcare_providers": {
            "title": "Clinical Workflow Integration",
            "description": "Design solutions that integrate into existing healthcare workflows.",
            "detail": "Healthcare provider hackathon projects should minimize disruption. Research typical clinical processes, explain how your solution fits into existing workflows with minimal training required, and address potential implementation barriers."
        },
        "educators": {
            "title": "Educational Assessment Features",
            "description": "Include ways to measure learning outcomes in education-focused solutions.",
            "detail": "Education hackathon projects benefit from assessment capabilities. Implement features that help educators measure effectiveness, track learner progress, and generate insights about knowledge gaps or areas for improvement."
        },
        "researchers": {
            "title": "Research Methodology Transparency",
            "description": "Document your research methodology and data handling approach clearly.",
            "detail": "Research-focused hackathon projects require methodological rigor. Document your data sources, processing methods, and analysis techniques with scientific precision, and be prepared to discuss limitations and further research opportunities."
        }
    }
    
    # Return specific user tip or a general one if user type not found
    return user_tips.get(user_type, {
        "title": "User-Centered Testing",
        "description": "Conduct basic user testing even within hackathon time constraints.",
        "detail": "Regardless of user type, judges value evidence of user feedback. Test your concept with even 2-3 potential users during the hackathon, document their feedback, and explain how you incorporated their input into your solution."
    })

def suggest_context_aware_hackathon_tips(problem_statement, problem_analysis=None):
    """
    Generate context-aware hackathon tips based on the problem statement.
    
    Args:
        problem_statement (str): The problem statement text
        problem_analysis (dict, optional): Pre-existing problem analysis
        
    Returns:
        dict: Tailored hackathon tips
    """
    # Analyze the problem domain
    domain_analysis = analyze_problem_domain(problem_statement, problem_analysis)
    
    # Get general tips from hackathon_tips module
    planning_tips = get_hackathon_planning_tips()
    tech_strategies = get_technical_execution_strategies()
    presentation_strategies = get_presentation_strategies()
    judge_insights = get_judge_perspective_insights()
    pitfalls = get_pitfall_avoidance_tips()
    
    # Extract key information from problem analysis
    if problem_analysis:
        complexity = problem_analysis.get("complexity", 0.5)
    else:
        # Default complexity if no analysis provided
        complexity = 0.5
    
    # Get domain-specific tip
    domain_tip = get_domain_specific_tip(domain_analysis["primary_domain"])
    
    # Get approach-specific tip
    approach_tip = get_approach_specific_tip(domain_analysis["primary_approach"])
    
    # Get complexity-specific tip
    complexity_tip = get_complexity_specific_tip(complexity)
    
    # Get user-specific tip
    user_tip = get_user_specific_tip(domain_analysis["primary_user"])
    
    # Select most relevant general tips based on domain analysis
    selected_planning_tips = []
    selected_tech_tips = []
    selected_presentation_tips = []
    selected_pitfalls = []
    
    # For each category, select most relevant tips (highest importance first)
    # Planning tips
    selected_planning_tips = sorted(
        planning_tips["pre_event"] + planning_tips["day_of_event"],
        key=lambda x: x["importance"],
        reverse=True
    )[:3]
    
    # Tech tips - focused on primary approach
    all_tech_tips = tech_strategies["development"] + tech_strategies["design"]
    if domain_analysis["primary_approach"] == "mobile" or domain_analysis["primary_approach"] == "web":
        # Prioritize design tips for mobile/web approaches
        selected_tech_tips = [tip for tip in all_tech_tips if "design" in tip["title"].lower() or "user" in tip["title"].lower()][:2]
        if len(selected_tech_tips) < 2:
            selected_tech_tips += [tip for tip in all_tech_tips if tip not in selected_tech_tips][:2 - len(selected_tech_tips)]
    else:
        # Prioritize development tips for other approaches
        selected_tech_tips = [tip for tip in all_tech_tips if "familiar" in tip["title"].lower() or "core" in tip["title"].lower()][:2]
        if len(selected_tech_tips) < 2:
            selected_tech_tips += [tip for tip in all_tech_tips if tip not in selected_tech_tips][:2 - len(selected_tech_tips)]
    
    # Presentation tips - always include demo and pitch tips
    selected_presentation_tips.append(presentation_strategies["demo"][0])  # Fallback demo tip is always valuable
    selected_presentation_tips.append(presentation_strategies["pitch"][0])  # Start with problem tip is always valuable
    
    # Judge insights - select top 2 by importance
    selected_judge_insights = sorted(judge_insights, key=lambda x: x["importance"], reverse=True)[:2]
    
    # Pitfalls - select relevant ones by impact
    high_impact_pitfalls = [pitfall for pitfall in pitfalls if pitfall["impact"] == "High"][:2]
    
    return {
        "domain_analysis": domain_analysis,
        "specialized_tips": {
            "domain_tip": domain_tip,
            "approach_tip": approach_tip,
            "complexity_tip": complexity_tip,
            "user_tip": user_tip
        },
        "selected_tips": {
            "planning_tips": selected_planning_tips,
            "tech_tips": selected_tech_tips,
            "presentation_tips": selected_presentation_tips,
            "judge_insights": selected_judge_insights,
            "pitfalls": high_impact_pitfalls
        }
    }