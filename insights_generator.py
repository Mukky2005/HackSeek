import random
import pandas as pd
from collections import Counter
from domain_knowledge import (
    TECH_DOMAINS, 
    CROSS_DOMAIN_PATTERNS, 
    PROBLEM_SOLVING_METHODOLOGIES, 
    EMERGING_TECHNOLOGIES
)

# Define domain categories
DOMAINS = [
    "Technology", "Healthcare", "Education", "Environment", 
    "Business", "Finance", "Transportation", "Energy",
    "Communication", "Entertainment", "Agriculture", 
    "Manufacturing", "Retail", "Urban Planning", "Sustainability"
]

# Map our DOMAINS to the keys in TECH_DOMAINS for enhanced insights
DOMAIN_MAPPING = {
    "Technology": "artificial_intelligence",
    "Healthcare": "healthcare",
    "Education": "education",
    "Environment": "sustainability",
    "Business": "software_development",
    "Finance": "finance",
    "Transportation": "transportation",
    "Manufacturing": "manufacturing",
    "Sustainability": "sustainability"
}

def generate_insights(problem_analysis, depth=3):
    """
    Generate insights based on the problem analysis.
    
    Args:
        problem_analysis (dict): The problem analysis from analyze_problem
        depth (int): Depth of analysis (1-5, with 5 being deepest)
        
    Returns:
        dict: A dictionary containing insights
    """
    # Extract key information from the problem analysis
    text = problem_analysis['text']
    doc = problem_analysis['doc']
    key_phrases = problem_analysis['key_phrases']
    entities = problem_analysis['entities']
    objectives = problem_analysis['objectives']
    
    # Determine relevant domains based on key phrases and entities
    domain_relevance = calculate_domain_relevance(text, key_phrases, entities)
    
    # Generate trends based on the most relevant domains
    top_domains = sorted(domain_relevance.items(), key=lambda x: x[1], reverse=True)[:3]
    trends = generate_trends(top_domains, objectives, depth)
    
    # Generate patterns based on problem complexity and objectives
    patterns = generate_patterns(problem_analysis, depth)
    
    # Identify potential gaps in current solutions
    gaps = identify_gaps(problem_analysis, domain_relevance, depth)
    
    # Return the insights
    return {
        "domain_relevance": domain_relevance,
        "trends": trends,
        "patterns": patterns,
        "gaps": gaps
    }

def calculate_domain_relevance(text, key_phrases, entities):
    """
    Calculate the relevance of different domains to the problem.
    
    Returns:
        dict: Domain relevance scores
    """
    # Domain keywords dictionary
    domain_keywords = {
        "Technology": ["digital", "tech", "software", "hardware", "app", "online", "internet", "algorithm", "data", "computer", "AI", "artificial intelligence", "machine learning"],
        "Healthcare": ["health", "medical", "patient", "doctor", "hospital", "wellness", "disease", "treatment", "care", "clinical", "diagnosis"],
        "Education": ["education", "learning", "student", "teach", "school", "university", "training", "curriculum", "classroom", "knowledge", "skill"],
        "Environment": ["environment", "sustainability", "climate", "green", "eco", "pollution", "conservation", "waste", "recycling", "natural", "energy"],
        "Business": ["business", "company", "organization", "market", "customer", "product", "service", "strategy", "management", "operation"],
        "Finance": ["finance", "money", "budget", "cost", "investment", "fund", "economic", "profit", "revenue", "expense", "financial"],
        "Transportation": ["transport", "vehicle", "car", "bus", "train", "traffic", "commute", "travel", "mobility", "logistics"],
        "Energy": ["energy", "power", "electricity", "fuel", "renewable", "solar", "wind", "grid", "consumption", "efficiency"],
        "Communication": ["communication", "message", "media", "information", "network", "social", "community", "connect", "interaction"],
        "Entertainment": ["entertainment", "media", "game", "video", "music", "film", "art", "leisure", "play", "creative"],
        "Agriculture": ["agriculture", "farm", "crop", "food", "harvest", "soil", "plant", "livestock", "organic", "cultivation"],
        "Manufacturing": ["manufacturing", "production", "factory", "industry", "assembly", "quality", "product", "process", "automation"],
        "Retail": ["retail", "store", "shop", "consumer", "customer", "product", "sale", "purchase", "e-commerce", "market"],
        "Urban Planning": ["urban", "city", "planning", "infrastructure", "building", "community", "development", "public", "space", "design"],
        "Sustainability": ["sustainable", "renewable", "eco-friendly", "green", "environmental", "conservation", "resource", "efficiency", "circular"]
    }
    
    # Initialize relevance scores
    relevance_scores = {domain: 0 for domain in DOMAINS}
    
    # Count keyword occurrences
    text_lower = text.lower()
    
    for domain, keywords in domain_keywords.items():
        for keyword in keywords:
            if keyword.lower() in text_lower:
                # Count occurrences (more occurrences = higher relevance)
                count = text_lower.count(keyword.lower())
                relevance_scores[domain] += count * 0.5
    
    # Check key phrases for domain relevance
    for phrase in key_phrases:
        phrase_lower = phrase.lower()
        for domain, keywords in domain_keywords.items():
            for keyword in keywords:
                if keyword.lower() in phrase_lower:
                    relevance_scores[domain] += 1
    
    # Check entities for domain relevance
    for entity in entities:
        entity_text = entity['text'].lower()
        for domain, keywords in domain_keywords.items():
            for keyword in keywords:
                if keyword.lower() in entity_text:
                    relevance_scores[domain] += 2  # Entities are more important
    
    # Normalize scores to be between 0 and 10
    max_score = max(relevance_scores.values()) if relevance_scores.values() else 1
    if max_score > 0:
        for domain in relevance_scores:
            relevance_scores[domain] = min(10, (relevance_scores[domain] / max_score) * 10)
    
    # Ensure at least some domains have relevance
    if max_score == 0:
        # Assign random relevance to top 3 domains if no clear relevance found
        for domain in random.sample(DOMAINS, 3):
            relevance_scores[domain] = random.uniform(5, 10)
    
    return relevance_scores

def generate_trends(top_domains, objectives, depth):
    """
    Generate trends based on top domains and objectives.
    
    Returns:
        list: Trends relevant to the problem
    """
    # Enhanced trends using our domain-specific knowledge
    domain_trends_dict = {}
    
    # Use our existing trend dictionary as baseline
    base_domain_trends = {
        "Technology": [
            "Increasing adoption of AI and machine learning for automation",
            "Growing focus on user experience and interface design",
            "Rising importance of cybersecurity and data privacy",
            "Shift towards cloud-based and distributed computing",
            "Integration of IoT devices in everyday products and services"
        ],
        "Healthcare": [
            "Growing focus on preventive healthcare and wellness",
            "Increasing use of telemedicine and remote monitoring",
            "Rise of personalized medicine and treatment plans",
            "Integration of AI in diagnostics and treatment recommendations",
            "Greater emphasis on mental health and holistic well-being"
        ],
        "Education": [
            "Shift towards personalized and adaptive learning approaches",
            "Integration of technology in classroom and remote education",
            "Growing emphasis on lifelong learning and skill development",
            "Rise of microlearning and bite-sized educational content",
            "Focus on developing critical thinking and problem-solving skills"
        ],
        "Environment": [
            "Increasing focus on circular economy and waste reduction",
            "Growing adoption of renewable energy sources",
            "Rising consumer demand for sustainable products",
            "Development of innovative techniques for carbon capture",
            "Implementation of stricter environmental regulations"
        ],
        "Business": [
            "Shift towards remote and flexible work arrangements",
            "Growing importance of digital transformation",
            "Rise of subscription-based business models",
            "Increasing focus on customer experience and personalization",
            "Growing emphasis on corporate social responsibility"
        ],
        "Finance": [
            "Rise of digital and mobile payment systems",
            "Growing adoption of blockchain and cryptocurrency",
            "Increasing focus on financial inclusion",
            "Development of AI-driven financial advice and services",
            "Shift towards sustainable and ethical investing"
        ],
        "Transportation": [
            "Growing development of autonomous vehicles",
            "Shift towards electric and alternative fuel vehicles",
            "Rise of shared mobility services",
            "Integration of smart technology in transportation infrastructure",
            "Focus on last-mile delivery solutions"
        ],
        "Energy": [
            "Increasing investment in renewable energy sources",
            "Development of more efficient energy storage solutions",
            "Growth of smart grid technology and infrastructure",
            "Focus on decentralized energy production",
            "Rising adoption of energy-efficient technologies"
        ],
        "Communication": [
            "Growing importance of visual communication",
            "Rise of real-time and asynchronous collaboration tools",
            "Increasing personalization of communication channels",
            "Development of more immersive communication technologies",
            "Focus on inclusive and accessible communication"
        ],
        "Entertainment": [
            "Shift towards streaming and on-demand content",
            "Growing integration of AR and VR in entertainment",
            "Rise of interactive and participatory entertainment",
            "Increasing personalization of content recommendations",
            "Development of more immersive gaming experiences"
        ],
        "Agriculture": [
            "Adoption of precision agriculture techniques",
            "Integration of IoT and sensors in farming",
            "Growing focus on sustainable and regenerative practices",
            "Development of vertical and urban farming solutions",
            "Rise of alternative protein sources and lab-grown foods"
        ],
        "Manufacturing": [
            "Increasing automation and use of robotics",
            "Adoption of additive manufacturing (3D printing)",
            "Growing implementation of Industry 4.0 principles",
            "Focus on sustainable and circular manufacturing",
            "Rise of customization and on-demand production"
        ],
        "Retail": [
            "Growing integration of online and offline shopping experiences",
            "Rise of experiential retail and immersive shopping",
            "Increasing use of AI for personalized recommendations",
            "Development of faster and more efficient delivery methods",
            "Focus on sustainability and ethical sourcing"
        ],
        "Urban Planning": [
            "Growing development of smart city infrastructure",
            "Increasing focus on walkability and public spaces",
            "Rise of mixed-use developments and urban villages",
            "Integration of green spaces and natural elements",
            "Focus on resilience and adaptation to climate change"
        ],
        "Sustainability": [
            "Growing implementation of circular economy principles",
            "Rise of sustainable and ethical consumption",
            "Increasing focus on biodiversity and ecosystem preservation",
            "Development of innovative materials and processes",
            "Shift towards measuring and reducing carbon footprints"
        ]
    }
    
    # Initialize with base trends
    domain_trends_dict = base_domain_trends.copy()
    
    # Enhance with domain-specific knowledge from our new dataset
    for domain, domain_key in DOMAIN_MAPPING.items():
        if domain_key in TECH_DOMAINS:
            # Extract trends from enhanced dataset if available
            if "trends" in TECH_DOMAINS[domain_key]:
                # Combine existing trends with enhanced ones
                if domain in domain_trends_dict:
                    domain_trends_dict[domain].extend(TECH_DOMAINS[domain_key]["trends"])
                else:
                    domain_trends_dict[domain] = TECH_DOMAINS[domain_key]["trends"]
    
    # Include relevant emerging technologies as trends
    for tech in EMERGING_TECHNOLOGIES:
        tech_name = tech["technology"]
        applications = tech["applications"]
        
        # Add to relevant domains
        if "Technology" in domain_trends_dict:
            domain_trends_dict["Technology"].append(f"Emergence of {tech_name} with applications in {applications[0]}")
        
        # Add specific applications to relevant domains
        for app in applications:
            app_lower = app.lower()
            for domain in DOMAINS:
                domain_lower = domain.lower()
                if domain_lower in app_lower:
                    if domain in domain_trends_dict:
                        domain_trends_dict[domain].append(f"Application of {tech_name} for {app}")
    
    # Select trends based on top domains and depth
    trends = []
    for domain, score in top_domains:
        # Number of trends to select depends on domain relevance and analysis depth
        num_trends = min(depth + 2, 7)  # Increased for more comprehensive trends
        domain_specific_trends = domain_trends_dict.get(domain, [])
        
        if domain_specific_trends:
            # Select random trends from the domain but avoid duplicates
            unique_domain_trends = list(set(domain_specific_trends))
            selected_trends = random.sample(unique_domain_trends, min(num_trends, len(unique_domain_trends)))
            trends.extend(selected_trends)
    
    # Add some objectives-based trends
    objective_trends = []
    for objective in objectives[:2]:  # Use top 2 objectives
        words = objective.lower().split()
        for domain, domain_trends_list in domain_trends_dict.items():
            for trend in domain_trends_list:
                # Check if objective words appear in trend
                if any(word in trend.lower() for word in words if len(word) > 3):
                    objective_trends.append(trend)
    
    # Add unique objective trends
    for trend in objective_trends:
        if trend not in trends:
            trends.append(trend)
    
    # Add cross-domain application trends based on problem-solving methodologies
    if depth >= 3:
        # Select a relevant methodology based on the problem
        methodology = random.choice(PROBLEM_SOLVING_METHODOLOGIES)
        trends.append(f"Growing application of {methodology['name']} methodology for similar challenges")
            
    # Limit the number of trends based on depth but increased for enhanced analysis
    max_trends = depth + 5
    
    # Make sure we have unique trends
    unique_trends = list(set(trends))
    
    return unique_trends[:max_trends]

def generate_patterns(problem_analysis, depth):
    """
    Generate patterns based on problem analysis.
    
    Returns:
        list: Identified patterns
    """
    # Pattern templates
    pattern_templates = [
        "The problem exhibits a {cycle} cycle where {factor1} leads to {factor2}",
        "There's a clear correlation between {factor1} and {factor2} in this domain",
        "A common pattern in this area is the relationship between {factor1} and {factor2}",
        "Similar problems often show {factor1} affecting {factor2} in a {relationship} way",
        "Historical data suggests that {factor1} typically precedes changes in {factor2}",
        "The {factor1} follows a predictable pattern when {factor2} changes",
        "Analysis shows a {relationship} relationship between {factor1} and {factor2}"
    ]
    
    # Factors and relationships to use in patterns
    factors = []
    for entity in problem_analysis['entities']:
        factors.append(entity['text'])
    
    for phrase in problem_analysis['key_phrases'][:5]:
        factors.append(phrase)
    
    # If not enough factors, add some from the objectives
    if len(factors) < 5:
        for objective in problem_analysis['objectives']:
            words = objective.split()
            if len(words) >= 3:
                factors.append(" ".join(words[:3]))
    
    # Ensure we have enough factors
    while len(factors) < 5:
        factors.append(f"factor-{len(factors)+1}")
    
    # Make the factors unique
    factors = list(set(factors))
    
    # Relationships and cycles
    relationships = ["direct", "inverse", "complex", "causal", "interdependent"]
    cycles = ["reinforcing", "balancing", "seasonal", "cyclical", "emerging"]
    
    # Generate patterns
    patterns = []
    
    # Include cross-domain patterns from our enhanced dataset
    # The number of cross-domain patterns to include depends on depth
    num_cross_domain = min(depth - 1, 3) if depth > 1 else 0
    
    if num_cross_domain > 0:
        # Select some cross-domain patterns from our knowledge database
        selected_cross_domain = random.sample(CROSS_DOMAIN_PATTERNS, num_cross_domain)
        
        # Add these patterns to our results with appropriate formatting
        for pattern_data in selected_cross_domain:
            pattern_name = pattern_data["pattern"]
            description = pattern_data["description"]
            examples = pattern_data["examples"]
            
            # Format the cross-domain pattern information
            pattern_text = f"The '{pattern_name}' pattern ({description}) may be applicable, as seen in examples like {random.choice(examples)}"
            patterns.append(pattern_text)
    
    # Add traditional patterns
    num_traditional = min(depth + 1, 5) - len(patterns)
    
    for _ in range(num_traditional):
        template = random.choice(pattern_templates)
        relationship = random.choice(relationships)
        cycle = random.choice(cycles)
        
        # Ensure we select different factors for each pattern
        if len(factors) >= 2:
            factor1, factor2 = random.sample(factors, 2)
        else:
            factor1 = factors[0] if factors else "primary factor"
            factor2 = "secondary factor"
        
        # Create the pattern
        pattern = template.format(
            factor1=factor1,
            factor2=factor2,
            relationship=relationship,
            cycle=cycle
        )
        
        patterns.append(pattern)
    
    # For higher depth analysis, suggest methodologies from our database
    if depth >= 4:
        # Select a methodology that matches the problem's characteristics
        methodology = random.choice(PROBLEM_SOLVING_METHODOLOGIES)
        methodology_name = methodology["name"]
        methodology_phases = ", ".join(methodology["phases"])
        methodology_best = methodology["best_for"]
        
        # Create a pattern suggestion based on the methodology
        methodology_pattern = f"Consider applying the {methodology_name} methodology ({methodology_best}) with its phases: {methodology_phases}"
        patterns.append(methodology_pattern)
    
    return patterns

def identify_gaps(problem_analysis, domain_relevance, depth):
    """
    Identify potential gaps in current solutions.
    
    Returns:
        list: Identified gaps
    """
    # Gap templates
    gap_templates = [
        "Current solutions often lack {aspect}, which is essential for addressing {issue}",
        "There's a significant gap in {domain} regarding {aspect} implementation",
        "Most approaches fail to consider the importance of {aspect} in solving {issue}",
        "The connection between {aspect1} and {aspect2} is often overlooked in existing solutions",
        "Existing frameworks don't adequately address the {issue} from a {aspect} perspective",
        "There's an opportunity to bridge the gap between {aspect1} and {aspect2} in this domain",
        "Current {domain} solutions lack integration with {aspect}, limiting their effectiveness"
    ]
    
    # Base aspects to use in gaps
    base_aspects = [
        "user experience", "data integration", "sustainability", "scalability", 
        "accessibility", "personalization", "real-time feedback", "automation",
        "cross-functional collaboration", "long-term planning", "resource optimization"
    ]
    
    # Enhanced aspects with domain-specific challenges from our knowledge base
    enhanced_aspects = base_aspects.copy()
    
    # Get the top domains to focus on
    top_domains = [domain for domain, score in sorted(domain_relevance.items(), key=lambda x: x[1], reverse=True)[:3]]
    
    # Add domain-specific challenges from our enhanced knowledge base
    for domain in top_domains:
        if domain in DOMAIN_MAPPING:
            domain_key = DOMAIN_MAPPING[domain]
            if domain_key in TECH_DOMAINS and "challenges" in TECH_DOMAINS[domain_key]:
                # Add domain-specific challenges as aspects
                for challenge in TECH_DOMAINS[domain_key]["challenges"]:
                    enhanced_aspects.append(challenge.lower())
    
    # Get issues from objectives and constraints
    issues = []
    for objective in problem_analysis['objectives']:
        issues.append(objective)
    
    for constraint in problem_analysis['constraints']:
        issues.append(constraint)
    
    # If not enough issues, add some generic ones
    while len(issues) < 5:
        issues.append(f"key challenge {len(issues)+1}")
    
    # Generate gaps
    gaps = []
    
    # First, add domain-specific gaps based on our knowledge base
    for domain in top_domains:
        if domain in DOMAIN_MAPPING:
            domain_key = DOMAIN_MAPPING[domain]
            
            # If we have domain-specific challenges, use them to generate targeted gaps
            if domain_key in TECH_DOMAINS and "challenges" in TECH_DOMAINS[domain_key]:
                challenges = TECH_DOMAINS[domain_key]["challenges"]
                
                # Select a few challenges based on depth
                num_challenges = min(depth, len(challenges))
                selected_challenges = random.sample(challenges, num_challenges)
                
                for challenge in selected_challenges:
                    # Format a domain-specific gap
                    issue = random.choice(issues)
                    gap = f"In the {domain} domain, {challenge} remains a critical gap that affects {issue}"
                    if gap not in gaps:
                        gaps.append(gap)
    
    # Add technology-specific gaps for deeper analysis
    if depth >= 3:
        # Select a relevant emerging technology
        tech = random.choice(EMERGING_TECHNOLOGIES)
        tech_name = tech["technology"]
        tech_maturity = tech["maturity"]
        applications = tech["applications"]
        
        # Create a gap related to this emerging technology
        gap = f"While {tech_name} ({tech_maturity} maturity) offers potential for {random.choice(applications)}, integration gaps exist in current solutions"
        gaps.append(gap)
    
    # Add general template-based gaps to fill out the required number
    num_template_gaps = min(depth + 1, 5) - len(gaps)
    
    for _ in range(num_template_gaps):
        template = random.choice(gap_templates)
        aspect = random.choice(enhanced_aspects)
        aspect1 = random.choice(enhanced_aspects)
        aspect2 = random.choice([a for a in enhanced_aspects if a != aspect1])
        issue = random.choice(issues)
        domain = random.choice(top_domains)
        
        # Create the gap
        gap = template.format(
            aspect=aspect,
            aspect1=aspect1,
            aspect2=aspect2,
            issue=issue,
            domain=domain
        )
        
        if gap not in gaps:
            gaps.append(gap)
    
    # For advanced depth, suggest methodological gaps
    if depth >= 4:
        # Select a relevant methodology
        methodology = random.choice(PROBLEM_SOLVING_METHODOLOGIES)
        method_name = methodology["name"]
        method_techniques = random.sample(methodology["techniques"], 2)
        
        # Create a methodology-specific gap
        gap = f"Current approaches rarely incorporate the {method_name} methodology's techniques like {method_techniques[0]} and {method_techniques[1]}, leaving a methodological gap"
        if gap not in gaps:
            gaps.append(gap)
    
    # Limit gaps to a reasonable number based on depth
    max_gaps = depth + 2
    
    return gaps[:max_gaps]
