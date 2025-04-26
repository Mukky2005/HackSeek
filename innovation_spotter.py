import random
from domain_knowledge import (
    TECH_DOMAINS, 
    CROSS_DOMAIN_PATTERNS, 
    PROBLEM_SOLVING_METHODOLOGIES, 
    EMERGING_TECHNOLOGIES
)

def generate_innovations(problem_analysis, insights, level=3):
    """
    Generate innovative solutions based on problem analysis and insights.
    
    Args:
        problem_analysis (dict): The problem analysis from analyze_problem
        insights (dict): The insights from generate_insights
        level (int): Innovation level (1-5, with 5 being most innovative)
        
    Returns:
        dict: A dictionary containing innovative solutions
    """
    # Get relevant data
    objectives = problem_analysis['objectives']
    key_phrases = problem_analysis['key_phrases']
    domain_relevance = insights['domain_relevance']
    trends = insights['trends']
    
    # Generate main solutions
    solutions = generate_solutions(problem_analysis, insights, level)
    
    # Generate cross-domain innovation ideas
    cross_domain = generate_cross_domain_ideas(problem_analysis, domain_relevance, level)
    
    # Generate technology suggestions
    technologies = suggest_technologies(problem_analysis, domain_relevance, level)
    
    # Return the innovations
    return {
        "solutions": solutions,
        "cross_domain": cross_domain,
        "technologies": technologies
    }

def generate_solutions(problem_analysis, insights, level):
    """
    Generate main solutions based on problem analysis and insights.
    
    Returns:
        list: List of solution dictionaries
    """
    # Solution templates based on innovation level
    solution_templates = {
        1: [  # Conservative solutions
            "Optimize existing {process} to improve {outcome}",
            "Enhance {feature} to better meet {need}",
            "Streamline {process} to reduce {problem}",
            "Update {system} to incorporate {trend}"
        ],
        2: [  # Moderate solutions
            "Integrate {technology} into existing {system} to enhance {outcome}",
            "Develop a new approach to {process} that addresses {gap}",
            "Create a platform that connects {stakeholder1} with {stakeholder2}",
            "Implement a feedback system that improves {process} based on {data}"
        ],
        3: [  # Balanced solutions
            "Build a {technology}-powered system that transforms how {stakeholders} approach {problem}",
            "Create an ecosystem where {stakeholder1} and {stakeholder2} collaborate to solve {problem}",
            "Develop a hybrid solution combining {approach1} and {approach2} to address {problem}",
            "Design a modular system that adapts to changing {conditions} while maintaining {outcome}"
        ],
        4: [  # Innovative solutions
            "Leverage {technology1} and {technology2} to create a novel approach to {problem}",
            "Develop an AI-driven platform that continuously optimizes {process} based on {data}",
            "Create a decentralized system where {stakeholders} contribute to solving {problem}",
            "Build a predictive model that identifies potential {problems} before they occur"
        ],
        5: [  # Disruptive solutions
            "Reimagine the entire {industry} paradigm through the integration of {technology1}, {technology2}, and {approach}",
            "Create a self-evolving ecosystem that autonomously adapts to changes in {conditions}",
            "Develop a platform that fundamentally changes how {stakeholders} interact with {system}",
            "Design a solution that eliminates the root cause of {problem} rather than treating symptoms"
        ]
    }
    
    # Solution description templates
    description_templates = [
        "A {adjective} approach that addresses {problem} through innovative use of {technology}",
        "This solution tackles {problem} by {action}, resulting in improved {outcome}",
        "By combining {approach1} with {approach2}, this solution offers a unique way to address {problem}",
        "A {scale} solution designed to transform how {stakeholders} deal with {problem}",
        "An innovative framework that allows {stakeholders} to overcome {problem} through {approach}"
    ]
    
    # Get elements to fill in templates
    processes = extract_processes(problem_analysis)
    problems = extract_problems(problem_analysis)
    technologies = extract_technologies(insights)
    stakeholders = extract_stakeholders(problem_analysis)
    approaches = [
        "data-driven decision making", 
        "user-centered design", 
        "agile implementation", 
        "systems thinking", 
        "collaborative innovation",
        "iterative prototyping",
        "predictive analytics",
        "cross-functional integration"
    ]
    outcomes = [
        "efficiency", "productivity", "user satisfaction", "cost reduction", 
        "quality improvement", "sustainability", "scalability", "innovation"
    ]
    features = [
        "user interface", "analytics dashboard", "automation capabilities", 
        "integration options", "customization features", "reporting tools"
    ]
    systems = [
        "platform", "framework", "application", "algorithm", "ecosystem", 
        "infrastructure", "network", "database"
    ]
    conditions = [
        "market demands", "user needs", "technological advancements", 
        "regulatory requirements", "competitive pressures", "resource constraints"
    ]
    adjectives = [
        "revolutionary", "holistic", "integrated", "scalable", "adaptable",
        "intuitive", "efficient", "sustainable", "intelligent", "resilient"
    ]
    actions = [
        "redefining the workflow", "integrating disparate systems", 
        "applying machine learning algorithms", "enabling real-time collaboration",
        "implementing predictive analytics", "utilizing crowd-sourced data"
    ]
    scales = [
        "enterprise-wide", "community-based", "industry-specific", 
        "globally applicable", "individually tailored", "team-oriented"
    ]
    
    # Select appropriate templates based on innovation level
    templates = solution_templates.get(level, solution_templates[3])
    
    # Number of solutions depends on innovation level
    num_solutions = min(level + 1, 5)
    
    # Generate solutions
    solutions = []
    for i in range(num_solutions):
        # Select random elements for templates
        process = random.choice(processes)
        problem = random.choice(problems)
        technology = random.choice(technologies)
        technology1 = random.choice(technologies)
        technology2 = random.choice([t for t in technologies if t != technology1]) if len(technologies) > 1 else technology1
        approach = random.choice(approaches)
        approach1 = random.choice(approaches)
        approach2 = random.choice([a for a in approaches if a != approach1])
        outcome = random.choice(outcomes)
        feature = random.choice(features)
        system = random.choice(systems)
        stakeholder = random.choice(stakeholders)
        stakeholders_plural = random.choice(stakeholders) + "s"
        stakeholder1 = random.choice(stakeholders)
        stakeholder2 = random.choice([s for s in stakeholders if s != stakeholder1]) if len(stakeholders) > 1 else stakeholder1
        condition = random.choice(conditions)
        gap = random.choice(insights['gaps']) if insights['gaps'] else "identified gaps"
        trend = random.choice(insights['trends']) if insights['trends'] else "emerging trends"
        data = random.choice(["user feedback", "performance metrics", "market data", "analytics"])
        industry = random.choice(["industry", "sector", "market", "field", "domain"])
        
        # Create title
        template = random.choice(templates)
        title = template.format(
            process=process, outcome=outcome, feature=feature, problem=problem,
            system=system, technology=technology, gap=gap, trend=trend,
            stakeholder=stakeholder, stakeholders=stakeholders_plural,
            stakeholder1=stakeholder1, stakeholder2=stakeholder2,
            technology1=technology1, technology2=technology2,
            approach=approach, approach1=approach1, approach2=approach2,
            conditions=condition, data=data, industry=industry
        )
        
        # Create description
        desc_template = random.choice(description_templates)
        adjective = random.choice(adjectives)
        action = random.choice(actions)
        scale = random.choice(scales)
        
        description = desc_template.format(
            adjective=adjective, problem=problem, technology=technology,
            action=action, outcome=outcome, approach1=approach1,
            approach2=approach2, scale=scale, stakeholders=stakeholders_plural,
            approach=approach
        )
        
        # Create approach details
        approach_details = generate_approach(problem, technology, approach, level)
        
        # Add solution
        solutions.append({
            "title": title,
            "description": description,
            "approach": approach_details
        })
    
    return solutions

def extract_processes(problem_analysis):
    """Extract potential processes from problem analysis"""
    processes = []
    
    # Extract from objectives
    for objective in problem_analysis['objectives']:
        words = objective.split()
        if len(words) >= 3:
            processes.append(" ".join(words[:3]))
    
    # Extract from key phrases
    for phrase in problem_analysis['key_phrases']:
        if len(phrase.split()) >= 2:
            processes.append(phrase)
    
    # If not enough processes, add some generic ones
    generic_processes = [
        "data processing", "user management", "resource allocation", 
        "information sharing", "decision making", "task automation",
        "performance monitoring", "quality control", "feedback collection"
    ]
    
    while len(processes) < 5:
        processes.append(random.choice(generic_processes))
    
    # Make unique
    return list(set(processes))

def extract_problems(problem_analysis):
    """Extract potential problems from problem analysis"""
    problems = []
    
    # Extract from constraints
    for constraint in problem_analysis['constraints']:
        words = constraint.split()
        if len(words) >= 3:
            problems.append(" ".join(words[:3]))
    
    # If not enough problems, extract from objectives as "lack of X"
    if len(problems) < 3:
        for objective in problem_analysis['objectives']:
            words = objective.split()
            if len(words) >= 2:
                problems.append(f"insufficient {' '.join(words[:2])}")
    
    # If still not enough problems, add some generic ones
    generic_problems = [
        "inefficient processes", "data silos", "communication gaps", 
        "resource limitations", "quality inconsistencies", "user adoption",
        "information overload", "system complexity", "scalability issues",
        "security vulnerabilities", "compliance challenges"
    ]
    
    while len(problems) < 5:
        problems.append(random.choice(generic_problems))
    
    # Make unique
    return list(set(problems))

def extract_technologies(insights):
    """Extract potential technologies based on insights"""
    # Get top domains
    top_domains = sorted(insights['domain_relevance'].items(), key=lambda x: x[1], reverse=True)[:3]
    
    # Enhanced domain-technology mapping from our knowledge base
    enhanced_domain_technologies = {
        "Technology": ["cloud computing", "AI", "machine learning", "blockchain", "IoT", "AR/VR", "quantum computing"],
        "Healthcare": ["telehealth", "wearable sensors", "medical imaging", "health informatics", "genomics", "biometrics"],
        "Education": ["e-learning platforms", "adaptive learning", "educational games", "virtual classrooms", "learning analytics"],
        "Environment": ["remote sensing", "environmental monitoring", "clean tech", "GIS mapping", "carbon capture"],
        "Business": ["CRM systems", "ERP solutions", "business intelligence", "process automation", "digital marketing"],
        "Finance": ["fintech", "payment processing", "blockchain", "algorithmic trading", "risk assessment tools"],
        "Transportation": ["route optimization", "telematics", "autonomous vehicles", "traffic management systems", "mobility platforms"],
        "Energy": ["smart grid", "energy storage", "renewable technology", "demand response systems", "energy analytics"],
        "Communication": ["real-time messaging", "video conferencing", "collaborative platforms", "social media analytics", "content management"],
        "Entertainment": ["content streaming", "interactive media", "gaming engines", "recommendation algorithms", "digital rights management"],
        "Agriculture": ["precision farming", "crop monitoring", "agricultural drones", "soil sensors", "farm management software"],
        "Manufacturing": ["robotics", "industrial IoT", "3D printing", "predictive maintenance", "quality control systems"],
        "Retail": ["inventory management", "point of sale", "customer analytics", "omnichannel platforms", "supply chain optimization"],
        "Urban Planning": ["GIS", "traffic simulation", "infrastructure monitoring", "urban analytics", "smart city platforms"],
        "Sustainability": ["lifecycle assessment", "carbon footprint tracking", "resource management", "sustainability reporting", "circular economy tools"]
    }
    
    # Enhance with domain-specific concepts from our knowledge database
    from insights_generator import DOMAIN_MAPPING
    
    for domain, domain_key in DOMAIN_MAPPING.items():
        if domain_key in TECH_DOMAINS and "concepts" in TECH_DOMAINS[domain_key]:
            # Add or extend domain-specific concepts as technologies
            concepts = [concept.lower() for concept in TECH_DOMAINS[domain_key]["concepts"]]
            if domain in enhanced_domain_technologies:
                enhanced_domain_technologies[domain].extend(concepts)
            else:
                enhanced_domain_technologies[domain] = concepts
    
    # Add emerging technologies from our knowledge base
    emerging_tech_list = []
    for tech in EMERGING_TECHNOLOGIES:
        tech_name = tech["technology"]
        tech_maturity = tech["maturity"]
        
        # Only add technology if it's mature enough (not in "Early" stage)
        if tech_maturity != "Early":
            emerging_tech_list.append(tech_name.lower())
    
    # Enhanced cross-domain technologies
    cross_domain_technologies = [
        "data analytics", "cloud computing", "mobile applications", 
        "API integration", "automation tools", "visualization software",
        "collaborative platforms", "AI/ML models", "digital twins"
    ]
    
    # Add emerging technologies to cross-domain list
    cross_domain_technologies.extend(emerging_tech_list)
    
    # Collect technologies based on top domains
    technologies = []
    for domain, score in top_domains:
        domain_techs = enhanced_domain_technologies.get(domain, [])
        if domain_techs:
            # Add more technologies from higher-scoring domains
            num_techs = min(int(score / 2) + 2, len(domain_techs))  # Add more for enhanced diversity
            domain_sample = random.sample(domain_techs, min(num_techs, len(domain_techs)))
            technologies.extend(domain_sample)
    
    # Add some cross-domain technologies
    cross_domain_count = min(5, len(cross_domain_technologies))  # Increased from 3 to 5
    cross_domain_sample = random.sample(cross_domain_technologies, cross_domain_count)
    technologies.extend(cross_domain_sample)
    
    # If applicable, add a disruptive emerging technology with high potential
    high_potential_techs = [
        tech["technology"] for tech in EMERGING_TECHNOLOGIES 
        if tech.get("disruption_potential", "") in ["High", "Very High"]
    ]
    
    if high_potential_techs and random.random() < 0.7:  # 70% chance to include
        disruptive_tech = random.choice(high_potential_techs)
        technologies.append(disruptive_tech.lower())
    
    # Make unique by converting to set and back to list
    return list(set(technologies))

def extract_stakeholders(problem_analysis):
    """Extract potential stakeholders from problem analysis"""
    stakeholders = []
    
    # Extract from entities
    for entity in problem_analysis['entities']:
        if entity['label'] in ['PERSON', 'ORG', 'NORP']:
            stakeholders.append(entity['text'])
    
    # Generic stakeholders
    generic_stakeholders = [
        "user", "customer", "provider", "manager", "developer", 
        "administrator", "stakeholder", "client", "partner", "community member"
    ]
    
    # Add domain-specific stakeholders based on keywords in the problem
    text = problem_analysis['text'].lower()
    
    if any(word in text for word in ["health", "medical", "patient", "doctor"]):
        stakeholders.extend(["patient", "healthcare provider", "medical researcher"])
    
    if any(word in text for word in ["education", "learn", "student", "teach"]):
        stakeholders.extend(["student", "educator", "administrator"])
    
    if any(word in text for word in ["business", "company", "market", "product"]):
        stakeholders.extend(["business owner", "customer", "employee"])
    
    if any(word in text for word in ["environment", "sustainability", "climate"]):
        stakeholders.extend(["community", "policymaker", "environmental scientist"])
    
    # If not enough stakeholders, add some generic ones
    while len(stakeholders) < 5:
        stakeholders.append(random.choice(generic_stakeholders))
    
    # Make unique
    return list(set(stakeholders))

def generate_approach(problem, technology, approach, level):
    """
    Generate detailed approach for a solution.
    
    Returns:
        str: Detailed approach
    """
    # Approach components
    components = [
        f"1. **Analysis Phase**: Begin with a thorough assessment of the {problem} to understand root causes and key requirements.",
        f"2. **Design Phase**: Develop a {['basic', 'comprehensive', 'innovative', 'transformative', 'revolutionary'][level-1]} solution architecture integrating {technology}.",
        f"3. **Implementation Strategy**: Use {approach} to build the solution in {['sequential', 'phased', 'iterative', 'adaptive', 'continuous'][level-1]} stages.",
        f"4. **Integration Plan**: Ensure seamless connection with existing systems and workflows.",
        f"5. **Validation Approach**: Implement {['standard', 'enhanced', 'multi-dimensional', 'predictive', 'autonomous'][level-1]} testing and validation protocols.",
        f"6. **Deployment Framework**: Roll out the solution using a {['controlled', 'staged', 'agile', 'dynamic', 'self-optimizing'][level-1]} deployment strategy.",
        f"7. **Feedback Mechanism**: Establish {['basic', 'comprehensive', 'real-time', 'AI-powered', 'predictive'][level-1]} feedback channels to continuously improve the solution."
    ]
    
    # Select number of components based on level
    num_components = min(level + 2, 7)
    selected_components = components[:num_components]
    
    # Join components
    return "\n".join(selected_components)

def generate_cross_domain_ideas(problem_analysis, domain_relevance, level):
    """
    Generate cross-domain innovation ideas.
    
    Returns:
        list: Cross-domain innovation ideas
    """
    # Get top domains
    top_domains = sorted(domain_relevance.items(), key=lambda x: x[1], reverse=True)[:3]
    top_domain_names = [domain for domain, _ in top_domains]
    
    # Domain-specific innovation concepts
    domain_concepts = {
        "Technology": ["algorithmic approach", "digital platform", "automated system", "data-driven solution"],
        "Healthcare": ["preventive model", "wellness approach", "patient-centered design", "remote monitoring"],
        "Education": ["learner-centered model", "adaptive curriculum", "competency-based framework", "peer learning"],
        "Environment": ["circular economy", "zero-waste approach", "ecosystem thinking", "regenerative design"],
        "Business": ["value chain optimization", "customer journey mapping", "agile organization", "sustainable business model"],
        "Finance": ["risk distribution", "value exchange", "resource allocation", "portfolio approach"],
        "Transportation": ["mobility as a service", "hub-and-spoke model", "intelligent routing", "demand prediction"],
        "Energy": ["decentralized production", "demand response", "energy arbitrage", "load balancing"],
        "Communication": ["network effects", "viral distribution", "peer-to-peer exchange", "information cascade"],
        "Entertainment": ["user-generated content", "immersive experience", "gamification", "narrative structure"],
        "Agriculture": ["precision techniques", "crop rotation", "companion planting", "integrated pest management"],
        "Manufacturing": ["just-in-time production", "modular design", "quality circles", "continuous improvement"],
        "Retail": ["omnichannel strategy", "experiential retail", "personalized marketing", "inventory optimization"],
        "Urban Planning": ["mixed-use development", "transit-oriented design", "walkable communities", "green infrastructure"],
        "Sustainability": ["cradle-to-cradle design", "resource efficiency", "systems thinking", "impact assessment"]
    }
    
    # Enhance domain concepts with our knowledge base
    from insights_generator import DOMAIN_MAPPING
    
    for domain, domain_key in DOMAIN_MAPPING.items():
        if domain_key in TECH_DOMAINS and "concepts" in TECH_DOMAINS[domain_key]:
            # Select a few concepts to add
            key_concepts = []
            for concept in TECH_DOMAINS[domain_key]["concepts"]:
                # Format concept as a solution approach
                formatted_concept = concept.lower().replace(" ", "-") + " approach"
                key_concepts.append(formatted_concept)
            
            # Add concepts to domain
            if domain in domain_concepts:
                domain_concepts[domain].extend(key_concepts)
            else:
                domain_concepts[domain] = key_concepts
    
    # Cross-domain idea templates
    standard_templates = [
        "Apply {concept1} from {domain1} to solve {problem} in {domain2}",
        "Combine {concept1} from {domain1} with {concept2} from {domain2} to create a novel solution",
        "Use {domain1}'s approach to {action} as inspiration for addressing {problem}",
        "Adapt the concept of {concept1} from {domain1} to revolutionize how {problem} is approached",
        "Implement a hybrid model combining {concept1} from {domain1} and {concept2} from {domain2}"
    ]
    
    # Generate ideas
    ideas = []
    
    # First, include ideas based on cross-domain patterns from our knowledge base
    num_pattern_ideas = min(level, len(CROSS_DOMAIN_PATTERNS))
    
    if num_pattern_ideas > 0:
        # Select cross-domain patterns based on level 
        selected_patterns = random.sample(CROSS_DOMAIN_PATTERNS, num_pattern_ideas)
        
        for pattern in selected_patterns:
            pattern_name = pattern["pattern"]
            description = pattern["description"]
            examples = pattern["examples"]
            
            # Get a relevant problem
            if problem_analysis['objectives']:
                problem = random.choice(problem_analysis['objectives'])
            else:
                problem = "the core challenge"
            
            # Create idea based on the pattern
            if len(top_domain_names) > 0:
                domain = random.choice(top_domain_names)
                idea = f"Apply the '{pattern_name}' pattern ({description}) to {problem} in the {domain} domain, similar to {random.choice(examples)}"
            else:
                idea = f"Use the '{pattern_name}' pattern ({description}) to address {problem}, drawing inspiration from {random.choice(examples)}"
            
            ideas.append(idea)
    
    # Add methodology-based cross-domain ideas for higher-level innovation
    if level >= 4:
        # Select a problem-solving methodology
        methodology = random.choice(PROBLEM_SOLVING_METHODOLOGIES)
        methodology_name = methodology["name"]
        techniques = methodology["techniques"]
        best_for = methodology["best_for"]
        
        # Select two techniques from the methodology
        selected_techniques = random.sample(techniques, min(2, len(techniques)))
        
        # Create the idea
        if problem_analysis['objectives']:
            problem = random.choice(problem_analysis['objectives'])
        else:
            problem = "the core challenge"
            
        idea = f"Implement the {methodology_name} methodology ({best_for}) to address {problem}, specifically using {selected_techniques[0]} and {selected_techniques[1]}"
        ideas.append(idea)
    
    # Add standard cross-domain ideas to fill out the required number
    num_standard_ideas = min(level + 2, 5) - len(ideas)
    
    # For each idea, select two different domains
    for _ in range(num_standard_ideas):
        # Select two different domains
        if len(top_domain_names) >= 2:
            domain1, domain2 = random.sample(top_domain_names, 2)
        else:
            # If we don't have enough domains, select one from top and one random
            domain1 = top_domain_names[0] if top_domain_names else random.choice(list(domain_concepts.keys()))
            domain2 = random.choice([d for d in domain_relevance.keys() if d != domain1])
        
        # Get concepts from each domain (ensuring they exist in our dictionary)
        concept1 = random.choice(domain_concepts.get(domain1, ["innovative approach"]))
        concept2 = random.choice(domain_concepts.get(domain2, ["novel methodology"]))
        
        # Select template and fill in
        template = random.choice(standard_templates)
        
        # Get problem
        if problem_analysis['objectives']:
            problem = random.choice(problem_analysis['objectives'])
        else:
            problem = "the core challenge"
        
        # Actions
        actions = ["optimize resources", "enhance user experience", "improve efficiency", 
                  "reduce complexity", "increase adoption", "foster innovation"]
        action = random.choice(actions)
        
        # Create idea
        idea = template.format(
            concept1=concept1,
            concept2=concept2,
            domain1=domain1,
            domain2=domain2,
            problem=problem,
            action=action
        )
        
        ideas.append(idea)
    
    # Ensure ideas are unique
    unique_ideas = list(set(ideas))
    
    # For very high innovation levels, add an emerging technology cross-domain idea
    if level >= 5 and len(unique_ideas) < 7:
        # Select a high-potential emerging technology
        high_potential_techs = [
            tech for tech in EMERGING_TECHNOLOGIES 
            if tech.get("disruption_potential", "") in ["High", "Very High"]
        ]
        
        if high_potential_techs:
            tech = random.choice(high_potential_techs)
            tech_name = tech["technology"]
            applications = tech["applications"]
            
            # Create a cross-domain idea that combines the technology with a relevant domain
            if top_domain_names:
                domain = random.choice(top_domain_names)
                application = random.choice(applications)
                
                idea = f"Explore how {tech_name} could revolutionize {domain} through {application}, creating entirely new possibilities"
                unique_ideas.append(idea)
    
    return unique_ideas

def suggest_technologies(problem_analysis, domain_relevance, level):
    """
    Suggest technologies relevant to the problem.
    
    Returns:
        list: Technology suggestions with relevance scores
    """
    # Domain-specific technologies with categories
    domain_technologies = {
        "Technology": [
            {"technology": "Machine Learning", "category": "AI & Analytics"},
            {"technology": "Big Data Analytics", "category": "AI & Analytics"},
            {"technology": "Cloud Computing", "category": "Infrastructure"},
            {"technology": "Blockchain", "category": "Security & Trust"},
            {"technology": "Internet of Things", "category": "Connected Systems"},
            {"technology": "Augmented Reality", "category": "User Experience"},
            {"technology": "Natural Language Processing", "category": "AI & Analytics"}
        ],
        "Healthcare": [
            {"technology": "Telemedicine", "category": "Service Delivery"},
            {"technology": "Electronic Health Records", "category": "Data Management"},
            {"technology": "Wearable Health Monitors", "category": "Monitoring"},
            {"technology": "Medical Imaging AI", "category": "Diagnostics"},
            {"technology": "Health Analytics", "category": "AI & Analytics"},
            {"technology": "3D Bioprinting", "category": "Manufacturing"}
        ],
        "Education": [
            {"technology": "Learning Management Systems", "category": "Platforms"},
            {"technology": "Adaptive Learning Software", "category": "Personalization"},
            {"technology": "Educational Analytics", "category": "AI & Analytics"},
            {"technology": "Virtual Classrooms", "category": "Service Delivery"},
            {"technology": "Gamified Learning", "category": "User Experience"}
        ],
        "Environment": [
            {"technology": "Environmental Monitoring", "category": "Monitoring"},
            {"technology": "Geographic Information Systems", "category": "Mapping & Analysis"},
            {"technology": "Clean Tech", "category": "Sustainability"},
            {"technology": "Waste Management Systems", "category": "Sustainability"},
            {"technology": "Climate Modeling", "category": "AI & Analytics"}
        ],
        "Business": [
            {"technology": "CRM Systems", "category": "Customer Management"},
            {"technology": "ERP Solutions", "category": "Operations"},
            {"technology": "Business Intelligence", "category": "AI & Analytics"},
            {"technology": "Process Automation", "category": "Automation"},
            {"technology": "Digital Marketing Tools", "category": "Marketing"}
        ],
        "Finance": [
            {"technology": "Payment Processing", "category": "Transactions"},
            {"technology": "Algorithmic Trading", "category": "Investment"},
            {"technology": "Blockchain Ledgers", "category": "Security & Trust"},
            {"technology": "Fraud Detection", "category": "Security & Trust"},
            {"technology": "Financial Analytics", "category": "AI & Analytics"}
        ],
        "Transportation": [
            {"technology": "Route Optimization", "category": "Logistics"},
            {"technology": "Autonomous Vehicles", "category": "Automation"},
            {"technology": "Traffic Management Systems", "category": "Infrastructure"},
            {"technology": "Fleet Telematics", "category": "Monitoring"},
            {"technology": "Mobility Platforms", "category": "Service Delivery"}
        ],
        "Energy": [
            {"technology": "Smart Grid", "category": "Infrastructure"},
            {"technology": "Energy Storage", "category": "Storage"},
            {"technology": "Renewable Energy Tech", "category": "Generation"},
            {"technology": "Energy Analytics", "category": "AI & Analytics"},
            {"technology": "Building Management Systems", "category": "Automation"}
        ],
        "Communication": [
            {"technology": "Real-time Messaging", "category": "Service Delivery"},
            {"technology": "Video Conferencing", "category": "Service Delivery"},
            {"technology": "Collaborative Platforms", "category": "Collaboration"},
            {"technology": "Content Management", "category": "Data Management"},
            {"technology": "Language Translation", "category": "AI & Analytics"}
        ]
    }
    
    # Enhance with domain-specific technologies from our knowledge database
    from insights_generator import DOMAIN_MAPPING
    
    for domain, domain_key in DOMAIN_MAPPING.items():
        if domain_key in TECH_DOMAINS and "concepts" in TECH_DOMAINS[domain_key]:
            # Create a list of technology entries from concepts
            enhanced_technologies = []
            
            # Define appropriate categories based on domain
            if domain == "Technology":
                categories = ["AI & Analytics", "Infrastructure", "Connected Systems", "Security & Trust"]
            elif domain == "Healthcare":
                categories = ["Diagnostics", "Monitoring", "Data Management", "Service Delivery"]
            elif domain == "Education":
                categories = ["Platforms", "Personalization", "Content Delivery", "Assessment Tools"]
            elif domain == "Business" or domain == "Finance":
                categories = ["Operations", "Analytics", "Security", "Automation", "Customer Management"]
            elif domain == "Manufacturing":
                categories = ["Automation", "Quality Control", "Supply Chain", "Production"]
            elif domain == "Sustainability" or domain == "Environment":
                categories = ["Monitoring", "Resource Management", "Sustainability", "Analytics"]
            elif domain == "Transportation":
                categories = ["Logistics", "Safety", "Infrastructure", "Automation"]
            else:
                categories = ["Core Technology", "Integration", "Analytics", "Automation"]
            
            # Create technology entries from concepts
            for concept in TECH_DOMAINS[domain_key]["concepts"]:
                category = random.choice(categories)
                tech_entry = {
                    "technology": concept,
                    "category": category
                }
                enhanced_technologies.append(tech_entry)
            
            # Add or update domain technologies
            if domain in domain_technologies:
                domain_technologies[domain].extend(enhanced_technologies)
            else:
                domain_technologies[domain] = enhanced_technologies
    
    # Add emerging technologies from our knowledge base
    emerging_tech_entries = []
    
    for tech in EMERGING_TECHNOLOGIES:
        tech_name = tech["technology"]
        maturity = tech["maturity"]
        disruption = tech.get("disruption_potential", "Medium")
        
        # Skip very early-stage technologies for lower innovation levels
        if maturity == "Early" and level < 4:
            continue
            
        # Determine appropriate category based on technology
        if "Computing" in tech_name or "AI" in tech_name:
            category = "Advanced Computing"
        elif "Energy" in tech_name:
            category = "Energy Innovation"
        elif "Reality" in tech_name or "Interface" in tech_name:
            category = "Human-Computer Interaction"
        elif "Biology" in tech_name:
            category = "Biotechnology"
        else:
            category = "Emerging Technology"
        
        tech_entry = {
            "technology": tech_name,
            "category": category
        }
        emerging_tech_entries.append(tech_entry)
    
    # Cross-domain technologies
    cross_domain_technologies = [
        {"technology": "Data Visualization", "category": "Presentation"},
        {"technology": "API Integration", "category": "Connectivity"},
        {"technology": "Mobile Applications", "category": "Service Delivery"},
        {"technology": "Cloud Services", "category": "Infrastructure"},
        {"technology": "Automation Workflows", "category": "Automation"},
        {"technology": "Digital Twin Systems", "category": "Simulation"},
        {"technology": "Edge Computing", "category": "Infrastructure"},
        {"technology": "Knowledge Graphs", "category": "Data Management"},
        {"technology": "Progressive Web Apps", "category": "Service Delivery"},
        {"technology": "Low-Code Platforms", "category": "Development"}
    ]
    
    # Get top domains
    top_domains = sorted(domain_relevance.items(), key=lambda x: x[1], reverse=True)[:3]
    
    # Select technologies based on domains and level
    suggested_technologies = []
    
    # Add domain-specific technologies
    for domain, score in top_domains:
        domain_techs = domain_technologies.get(domain, [])
        if domain_techs:
            # Number of technologies depends on domain relevance and level
            num_techs = min(level + 2, len(domain_techs))
            selected_techs = random.sample(domain_techs, min(num_techs, len(domain_techs)))
            
            for tech in selected_techs:
                # Calculate relevance based on domain score and add small variation
                relevance = score * random.uniform(0.7, 1.0)
                tech_entry = tech.copy()
                tech_entry["relevance"] = float(min(10.0, max(1.0, relevance)))
                suggested_technologies.append(tech_entry)
    
    # Add cross-domain technologies
    num_cross_domain = min(level + 1, len(cross_domain_technologies))
    selected_cross_domain = random.sample(cross_domain_technologies, min(num_cross_domain, len(cross_domain_technologies)))
    
    for tech in selected_cross_domain:
        # Random relevance for cross-domain technologies
        relevance = random.uniform(5, 8)
        tech_entry = tech.copy()
        tech_entry["relevance"] = relevance
        suggested_technologies.append(tech_entry)
    
    # For higher innovation levels, add emerging technologies
    if level >= 3:
        # Number of emerging technologies depends on innovation level
        num_emerging = min(level - 1, len(emerging_tech_entries))
        
        if num_emerging > 0 and emerging_tech_entries:
            selected_emerging = random.sample(emerging_tech_entries, min(num_emerging, len(emerging_tech_entries)))
            
            for tech in selected_emerging:
                # Emerging technologies have higher variability in relevance
                relevance = random.uniform(7, 10) if level >= 4 else random.uniform(4, 8)
                tech_entry = tech.copy()
                tech_entry["relevance"] = relevance
                suggested_technologies.append(tech_entry)
    
    # For highest innovation level, ensure a breakthrough technology is included
    if level == 5:
        # Look for high disruption potential technologies
        high_potential_techs = [
            tech for tech in EMERGING_TECHNOLOGIES 
            if tech.get("disruption_potential", "") in ["High", "Very High"]
        ]
        
        if high_potential_techs:
            selected_tech = random.choice(high_potential_techs)
            tech_name = selected_tech["technology"]
            
            # Check if this technology is already included
            if not any(t["technology"] == tech_name for t in suggested_technologies):
                category = "Breakthrough Technology"
                tech_entry = {
                    "technology": tech_name,
                    "category": category,
                    "relevance": 10.0  # Maximum relevance for breakthrough technology
                }
                suggested_technologies.append(tech_entry)
    
    return suggested_technologies
