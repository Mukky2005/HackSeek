import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import json
import os
from dotenv import load_dotenv  
load_dotenv()
import psycopg2
from problem_analyzer import analyze_problem
from insights_generator import generate_insights
from innovation_spotter import generate_innovations
from prioritization_system import prioritize_actions
from sample_problems import sample_problems
from context_aware_tips import suggest_context_aware_hackathon_tips

# Import auth modules
from auth_interface import render_auth_ui
from auth_utils import save_user_search, save_user_solution
from timeline import render_timeline
from sample_problems import get_sample_problems, problem_templates, generate_problem
from hackathon_tips import (get_hackathon_planning_tips, get_technical_execution_strategies,
                           get_presentation_strategies, get_judge_perspective_insights,
                           get_hackathon_categories_info, get_pitfall_avoidance_tips,
                           get_hackathon_success_stories, get_post_hackathon_strategies)

# Import AI Enhancement modules
from ai_enhancement import render_ai_enhancement_tab



# Set page configuration
st.set_page_config(
    page_title="HACKSEEK",
    page_icon="🧠",
    layout="wide",
    menu_items={}
)

# Hide hamburger menu and footer
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Apply theme if user has set one
if 'theme' in st.session_state and st.session_state.theme == 'dark':
    # Apply dark theme
    st.markdown("""
    <style>
    :root {
        --main-bg-color: #111111;
        --text-color: #EEEEEE;
        --sidebar-bg-color: #333333;
        --card-bg-color: #222222;
        --highlight-color: #4CAF50;
    }
    
    .stApp {
        background-color: var(--main-bg-color);
        color: var(--text-color);
    }
    
    .stSidebar {
        background-color: var(--sidebar-bg-color);
    }
    
    .stTextInput, .stNumberInput, .stTextArea {
        background-color: var(--card-bg-color);
        color: var(--text-color);
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: var(--highlight-color);
    }
    
    .stButton > button {
        background-color: var(--highlight-color);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize view state if not exists
if 'current_view' not in st.session_state:
    st.session_state.current_view = "main"  # Options: main, timeline, hackathon_tips, ai_enhancement

# Initialize session state for analysis
if 'analyzed' not in st.session_state:
    st.session_state.analyzed = False

# Initialize processing variables
if 'processing_started' not in st.session_state:
    st.session_state.processing_started = False
    
# Initialize analysis parameters with defaults
if 'analysis_depth' not in st.session_state:
    st.session_state.analysis_depth = 3
if 'innovation_level' not in st.session_state:
    st.session_state.innovation_level = 3
if 'problem_input' not in st.session_state:
    st.session_state.problem_input = ""
    
# Initialize session state for hackathon tips
if 'context_aware_tips' not in st.session_state:
    st.session_state.context_aware_tips = None
if 'problem_input_for_tips' not in st.session_state:
    st.session_state.problem_input_for_tips = ""
    
# Function to handle sample problem selection change
def on_category_select():
    """Regenerate problem when category changes"""
    if 'previous_category' in st.session_state and st.session_state.selected_category != "None" and st.session_state.selected_category != st.session_state.previous_category:
        # Category has changed, generate a new problem for this category
        if 'dynamic_problems' in st.session_state:
            # Only regenerate the problem for this specific category
            st.session_state.dynamic_problems[st.session_state.selected_category] = generate_problem(st.session_state.selected_category)
    
    # Update previous category
    st.session_state.previous_category = st.session_state.selected_category

# Render authentication UI and check if user is authenticated
user_is_authenticated = render_auth_ui()

# Only show the main content if user is authenticated
if user_is_authenticated:
    # Navigation menu in sidebar
    st.sidebar.title("Navigation")
    
    nav_options = ["Solution Generator", "Your Timeline", "Hackathon Tips", "AI Enhancement"]
    selected_nav = st.sidebar.radio("Go to:", nav_options)
    
    if selected_nav == "Solution Generator":
        st.session_state.current_view = "main"
    elif selected_nav == "Your Timeline":
        st.session_state.current_view = "timeline"
    elif selected_nav == "Hackathon Tips":
        st.session_state.current_view = "hackathon_tips"
    elif selected_nav == "AI Enhancement":
        st.session_state.current_view = "ai_enhancement"
    
    # Display the appropriate view based on current selection
    if st.session_state.current_view == "timeline":
        render_timeline()
    elif st.session_state.current_view == "ai_enhancement":
        try:
            st.write("Attempting to render AI Enhancement tab...")
            render_ai_enhancement_tab()
        except Exception as e:
            st.error(f"Error rendering AI Enhancement tab: {str(e)}")
            import traceback
            st.code(traceback.format_exc())
    elif st.session_state.current_view == "hackathon_tips":
        # Hackathon Tips view
        st.title("Hackathon Tips & Winning Strategies")
        
        st.markdown("""
        Welcome to the Hackathon Tips section! Here you'll find comprehensive strategies, insights, and advice 
        to help you succeed in hackathons. From planning and execution to presentation and post-event follow-up, 
        these tips will give you a competitive edge.
        """)
        
        # Create tabs for different sections of hackathon tips
        tips_tabs = st.tabs([
            "Problem-Specific Tips",
            "Planning", 
            "Technical Execution", 
            "Presentation", 
            "Judge Perspective", 
            "Hackathon Categories", 
            "Common Pitfalls", 
            "Success Stories", 
            "Post-Hackathon"
        ])
        
        # Problem-Specific Tips tab
        with tips_tabs[0]:
            st.subheader("Tips Based on Your Problem")
            
            # Input area for problem statement
            problem_statement_for_tips = st.text_area(
                "Enter your problem statement to get tailored hackathon tips",
                "",
                height=120,
                key="problem_input_for_tips"
            )
            
            # Generate button
            if st.button("Generate Customized Tips"):
                if problem_statement_for_tips.strip():
                    with st.spinner("Analyzing your problem statement..."):
                        # Analyze problem and suggest tips
                        problem_analysis = analyze_problem(problem_statement_for_tips)
                        context_aware_tips = suggest_context_aware_hackathon_tips(problem_statement_for_tips, problem_analysis)
                        
                        # Store in session state
                        st.session_state.context_aware_tips = context_aware_tips
                
            # Display context-aware tips if available
            if st.session_state.get('context_aware_tips'):
                tips = st.session_state.context_aware_tips
                
                # Display domain analysis
                st.markdown("### Domain Analysis")
                domain_analysis = tips["domain_analysis"]
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("#### Primary Focus Areas")
                    st.markdown(f"**Domain:** {domain_analysis['primary_domain'].replace('_', ' ').title()}")
                    st.markdown(f"**Technical Approach:** {domain_analysis['primary_approach'].replace('_', ' ').title()}")
                    st.markdown(f"**Target Users:** {domain_analysis['primary_user'].replace('_', ' ').title()}")
                
                with col2:
                    # Create a bar chart for top domain scores
                    domain_scores = domain_analysis["domain_scores"]
                    top_domains = sorted(domain_scores.items(), key=lambda x: x[1], reverse=True)[:5]
                    
                    if any(score > 0 for _, score in top_domains):
                        st.markdown("#### Top Domain Relevance")
                        domain_df = pd.DataFrame(top_domains, columns=['Domain', 'Score'])
                        domain_df['Domain'] = domain_df['Domain'].apply(lambda x: x.replace('_', ' ').title())
                        domain_fig = px.bar(domain_df, x='Domain', y='Score', title='Domain Relevance')
                        st.plotly_chart(domain_fig, use_container_width=True)
                
                # Specialized tips section
                st.markdown("### Specialized Tips for Your Problem")
                specialized_tips = tips["specialized_tips"]
                
                with st.expander(f"Domain-Specific: {specialized_tips['domain_tip']['title']}"):
                    st.markdown(f"**{specialized_tips['domain_tip']['description']}**")
                    st.markdown(specialized_tips['domain_tip']['detail'])
                
                with st.expander(f"Technical Approach: {specialized_tips['approach_tip']['title']}"):
                    st.markdown(f"**{specialized_tips['approach_tip']['description']}**")
                    st.markdown(specialized_tips['approach_tip']['detail'])
                
                with st.expander(f"Complexity Strategy: {specialized_tips['complexity_tip']['title']}"):
                    st.markdown(f"**{specialized_tips['complexity_tip']['description']}**")
                    st.markdown(specialized_tips['complexity_tip']['detail'])
                
                with st.expander(f"User Focus: {specialized_tips['user_tip']['title']}"):
                    st.markdown(f"**{specialized_tips['user_tip']['description']}**")
                    st.markdown(specialized_tips['user_tip']['detail'])
                
                # Selected tips section
                st.markdown("### Most Relevant General Tips")
                
                st.markdown("#### Planning Tips")
                for tip in tips["selected_tips"]["planning_tips"]:
                    with st.expander(f"{tip['title']} (Importance: {tip['importance']}/10)"):
                        st.markdown(f"**{tip['description']}**")
                        st.markdown(tip['detail'])
                
                st.markdown("#### Technical Tips")
                for tip in tips["selected_tips"]["tech_tips"]:
                    with st.expander(f"{tip['title']} (Importance: {tip['importance']}/10)"):
                        st.markdown(f"**{tip['description']}**")
                        st.markdown(tip['detail'])
                
                st.markdown("#### Presentation Tips")
                for tip in tips["selected_tips"]["presentation_tips"]:
                    with st.expander(f"{tip['title']} (Importance: {tip['importance']}/10)"):
                        st.markdown(f"**{tip['description']}**")
                        st.markdown(tip['detail'])
                
                st.markdown("#### Judge Insights")
                for insight in tips["selected_tips"]["judge_insights"]:
                    with st.expander(f"{insight['title']} (Importance: {insight['importance']}/10)"):
                        st.markdown(f"**{insight['description']}**")
                        st.markdown(insight['detail'])
                
                st.markdown("#### Pitfalls to Avoid")
                for pitfall in tips["selected_tips"]["pitfalls"]:
                    with st.expander(f"{pitfall['title']} (Impact: {pitfall['impact']})"):
                        st.markdown(f"**Issue:** {pitfall['description']}")
                        st.markdown(f"**How to avoid:** {pitfall['avoidance_strategy']}")
                        st.markdown(f"**Details:** {pitfall['detail']}")
            else:
                st.info("Enter your problem statement and click 'Generate Customized Tips' to get hackathon tips tailored to your specific problem.")
        
        # Planning tab
        with tips_tabs[1]:
            st.subheader("Planning & Preparation Tips")
            
            planning_tips = get_hackathon_planning_tips()
            
            # Pre-event tips
            st.markdown("### Before the Hackathon")
            for idx, tip in enumerate(planning_tips["pre_event"]):
                with st.expander(f"{tip['title']} (Importance: {tip['importance']}/10)"):
                    st.markdown(f"**{tip['description']}**")
                    st.markdown(tip['detail'])
                    
            # Day-of-event tips
            st.markdown("### During the Hackathon")
            for idx, tip in enumerate(planning_tips["day_of_event"]):
                with st.expander(f"{tip['title']} (Importance: {tip['importance']}/10)"):
                    st.markdown(f"**{tip['description']}**")
                    st.markdown(tip['detail'])
        
        # Technical Execution tab
        with tips_tabs[2]:
            st.subheader("Technical Execution Strategies")
            
            tech_strategies = get_technical_execution_strategies()
            
            # Development tips
            st.markdown("### Development Strategies")
            for idx, strategy in enumerate(tech_strategies["development"]):
                with st.expander(f"{strategy['title']} (Importance: {strategy['importance']}/10)"):
                    st.markdown(f"**{strategy['description']}**")
                    st.markdown(strategy['detail'])
                    
            # Design tips
            st.markdown("### Design Strategies")
            for idx, strategy in enumerate(tech_strategies["design"]):
                with st.expander(f"{strategy['title']} (Importance: {strategy['importance']}/10)"):
                    st.markdown(f"**{strategy['description']}**")
                    st.markdown(strategy['detail'])
        
        # Presentation tab
        with tips_tabs[3]:
            st.subheader("Presentation Strategies")
            
            presentation_strategies = get_presentation_strategies()
            
            # Pitch tips
            st.markdown("### Pitch Techniques")
            for idx, strategy in enumerate(presentation_strategies["pitch"]):
                with st.expander(f"{strategy['title']} (Importance: {strategy['importance']}/10)"):
                    st.markdown(f"**{strategy['description']}**")
                    st.markdown(strategy['detail'])
                    
            # Demo tips
            st.markdown("### Demo Best Practices")
            for idx, strategy in enumerate(presentation_strategies["demo"]):
                with st.expander(f"{strategy['title']} (Importance: {strategy['importance']}/10)"):
                    st.markdown(f"**{strategy['description']}**")
                    st.markdown(strategy['detail'])
                    
            # Q&A tips
            st.markdown("### Q&A Preparation")
            for idx, strategy in enumerate(presentation_strategies["q_and_a"]):
                with st.expander(f"{strategy['title']} (Importance: {strategy['importance']}/10)"):
                    st.markdown(f"**{strategy['description']}**")
                    st.markdown(strategy['detail'])
        
        # Judge Perspective tab
        with tips_tabs[4]:
            st.subheader("Understanding the Judge's Perspective")
            
            judge_insights = get_judge_perspective_insights()
            
            for idx, insight in enumerate(judge_insights):
                with st.expander(f"{insight['title']} (Importance: {insight['importance']}/10)"):
                    st.markdown(f"**{insight['description']}**")
                    st.markdown(insight['detail'])
                    
            # Create a radar chart for judges' priorities
            judge_df = pd.DataFrame(judge_insights)
            
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(
                r=judge_df['importance'],
                theta=judge_df['title'],
                fill='toself',
                name='Judge Priorities'
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 10]
                    )),
                showlegend=False,
                title="What Judges Prioritize"
            )
            
            st.plotly_chart(fig)
        
        # Hackathon Categories tab
        with tips_tabs[5]:
            st.subheader("Strategies by Hackathon Category")
            
            categories = get_hackathon_categories_info()
            
            for category, info in categories.items():
                with st.expander(f"{category.replace('_', ' ').title()} Hackathons"):
                    st.markdown(f"**Description:** {info['description']}")
                    st.markdown("### Key Strategies:")
                    for idx, strategy in enumerate(info['key_strategies']):
                        st.markdown(f"- {strategy}")
        
        # Common Pitfalls tab
        with tips_tabs[6]:
            st.subheader("Common Pitfalls to Avoid")
            
            pitfalls = get_pitfall_avoidance_tips()
            
            # Sort pitfalls by impact
            sorted_pitfalls = sorted(pitfalls, key=lambda x: x['impact'] == "High", reverse=True)
            
            for idx, pitfall in enumerate(sorted_pitfalls):
                with st.expander(f"{pitfall['title']} (Impact: {pitfall['impact']})"):
                    st.markdown(f"**Issue:** {pitfall['description']}")
                    st.markdown(f"**How to avoid:** {pitfall['avoidance_strategy']}")
                    st.markdown(f"**Details:** {pitfall['detail']}")
        
        # Success Stories tab
        with tips_tabs[7]:
            st.subheader("Hackathon Success Stories")
            
            success_stories = get_hackathon_success_stories()
            
            for idx, story in enumerate(success_stories):
                with st.expander(f"{story['name']}"):
                    st.markdown(f"**Project:** {story['description']}")
                    st.markdown(f"**Outcome:** {story['outcome']}")
                    st.markdown("### Key Lessons:")
                    for lesson in story['key_lessons']:
                        st.markdown(f"- {lesson}")
                    st.markdown(f"**The Story:** {story['detail']}")
        
        # Post-Hackathon tab
        with tips_tabs[8]:
            st.subheader("Post-Hackathon Strategies")
            
            post_strategies = get_post_hackathon_strategies()
            
            # Product Development strategies
            st.markdown("### Product Development Path")
            for idx, strategy in enumerate(post_strategies["product_development"]):
                with st.expander(f"{strategy['title']} (Importance: {strategy['importance']}/10)"):
                    st.markdown(f"**{strategy['description']}**")
                    st.markdown(strategy['detail'])
            
            # Funding strategies
            st.markdown("### Funding & Support Path")
            for idx, strategy in enumerate(post_strategies["funding_and_support"]):
                with st.expander(f"{strategy['title']} (Importance: {strategy['importance']}/10)"):
                    st.markdown(f"**{strategy['description']}**")
                    st.markdown(strategy['detail'])
            
            # Team Development strategies
            st.markdown("### Team Development Path")
            for idx, strategy in enumerate(post_strategies["team_development"]):
                with st.expander(f"{strategy['title']} (Importance: {strategy['importance']}/10)"):
                    st.markdown(f"**{strategy['description']}**")
                    st.markdown(strategy['detail'])
            
            # Personal Growth strategies
            st.markdown("### Personal Growth Path")
            for idx, strategy in enumerate(post_strategies["personal_growth"]):
                with st.expander(f"{strategy['title']} (Importance: {strategy['importance']}/10)"):
                    st.markdown(f"**{strategy['description']}**")
                    st.markdown(strategy['detail'])
    else:
        # Main app view
        # App title and description
        st.title("HACKSEEK")
        st.markdown("""
        This system analyzes problem statements and generates innovative solutions with prioritized action steps.
        Simply enter your problem statement, and the AI will help break it down, generate insights, 
        suggest innovative approaches, and prioritize action steps.
        """)
        
        # Sidebar with options
        st.sidebar.title("Options")
        st.session_state.analysis_depth = st.sidebar.slider("Analysis Depth", 1, 5, st.session_state.analysis_depth)
        st.session_state.innovation_level = st.sidebar.slider("Innovation Level", 1, 5, st.session_state.innovation_level)
        
        # Sample problem selection
        st.sidebar.subheader("Try a Sample Problem")
        
        # Get category options - same as before
        problem_categories = ["None"] + list(problem_templates.keys())
        
        # Add a refresh button to generate a new problem
        col1, col2 = st.sidebar.columns([3, 1])
        with col1:
            selected_sample = st.selectbox(
                "Select a problem category",
                problem_categories,
                key="selected_category",
                on_change=on_category_select
            )
        
        with col2:
            if st.button("🔄 New", help="Generate a new random problem in the selected category"):
                # Generate a new set of problems when refresh is clicked
                if selected_sample != "None" and 'dynamic_problems' in st.session_state:
                    # Regenerate only the selected problem
                    st.session_state.dynamic_problems[selected_sample] = generate_problem(selected_sample)
                elif 'dynamic_problems' in st.session_state:
                    # Regenerate all problems
                    del st.session_state.dynamic_problems
        
        # Main input area
        st.subheader("Enter Your Problem Statement")
        
        # Generate fresh problems if needed
        if 'dynamic_problems' not in st.session_state:
            st.session_state.dynamic_problems = get_sample_problems()
        
        # Load sample or get user input
        if selected_sample != "None":
            # Use the dynamically generated problem
            problem_statement = st.session_state.dynamic_problems[selected_sample]
            st.text_area("Problem Statement", problem_statement, height=150, key="problem_input")
        else:
            problem_statement = st.text_area(
                "Describe the problem you want to solve in detail...", 
                "", 
                height=150,
                key="problem_input"
            )
        
        # Get the problem statement from session state
        if 'problem_input' in st.session_state:
            problem_statement = st.session_state.problem_input
        
        # Process button
        if st.button("Analyze & Generate Solutions"):
            st.session_state.processing_started = True

# Process the problem when button is clicked (inside main view)
if user_is_authenticated and st.session_state.current_view == "main":
    # Check if processing has been triggered
    if st.session_state.processing_started and st.session_state.problem_input:
        problem_statement = st.session_state.problem_input
        st.session_state.processing_started = False
        st.session_state.analyzed = True
        
        with st.spinner("Analyzing problem statement..."):
            # Analyze problem statement
            problem_analysis = analyze_problem(problem_statement)
            
            # Generate domain insights
            insights = generate_insights(problem_analysis, depth=st.session_state.analysis_depth)
            
            # Generate innovation suggestions
            innovations = generate_innovations(problem_analysis, insights, level=st.session_state.innovation_level)
            
            # Prioritize actions
            prioritized_actions = prioritize_actions(innovations)
        
        # Store results in session state
        st.session_state.problem_analysis = problem_analysis
        st.session_state.insights = insights
        st.session_state.innovations = innovations
        st.session_state.prioritized_actions = prioritized_actions
        
        # Save the search to the database
        if st.session_state.get('user_info'):
            user_id = st.session_state.user_info['id']
            search_id = save_user_search(user_id, problem_statement)
            
            if search_id:
                # Create a JSON-serializable copy of the solution data
                # Remove spaCy doc from problem_analysis as it's not JSON serializable
                serializable_problem_analysis = problem_analysis.copy()
                if 'doc' in serializable_problem_analysis:
                    del serializable_problem_analysis['doc']
                
                # Save the solution data
                solution_data = {
                    'problem_analysis': serializable_problem_analysis,
                    'insights': insights, 
                    'innovations': innovations,
                    'prioritized_actions': prioritized_actions
                }
                save_user_solution(user_id, search_id, solution_data)
    elif not user_is_authenticated and st.session_state.processing_started and st.session_state.problem_input:
        st.session_state.processing_started = False
        st.warning("Please log in to analyze problems and save your solutions.")

# Display results if analysis has been performed
if st.session_state.get('analyzed', False) and st.session_state.problem_input:
    st.success("Analysis complete! Here are your results:")
    
    # Create tabs for different sections of the output
    tabs = st.tabs(["Problem Analysis", "Domain Insights", "Innovation Suggestions", "Action Plan"])
    
    # Problem Analysis tab
    with tabs[0]:
        st.subheader("Problem Analysis")
        st.markdown("### Key Objectives")
        for idx, obj in enumerate(st.session_state.problem_analysis['objectives']):
            st.markdown(f"**{idx+1}.** {obj}")
            
        st.markdown("### Constraints")
        for idx, constraint in enumerate(st.session_state.problem_analysis['constraints']):
            st.markdown(f"**{idx+1}.** {constraint}")
            
        st.markdown("### Key Entities")
        entities_df = pd.DataFrame(st.session_state.problem_analysis['entities'])
        if not entities_df.empty:
            st.dataframe(entities_df)
        
        # Visualization for sentiment and complexity
        col1, col2 = st.columns(2)
        with col1:
            sentiment = st.session_state.problem_analysis['sentiment']
            # Create a gauge chart for sentiment
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=sentiment * 100,
                title={'text': "Problem Statement Sentiment"},
                gauge={
                    'axis': {'range': [-100, 100]},
                    'bar': {'color': "gray"},
                    'steps': [
                        {'range': [-100, -33], 'color': "red"},
                        {'range': [-33, 33], 'color': "yellow"},
                        {'range': [33, 100], 'color': "green"}
                    ]
                }
            ))
            st.plotly_chart(fig)
            
        with col2:
            complexity = st.session_state.problem_analysis['complexity']
            # Create a gauge chart for complexity
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=complexity * 100,
                title={'text': "Problem Complexity"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "gray"},
                    'steps': [
                        {'range': [0, 33], 'color': "green"},
                        {'range': [33, 66], 'color': "yellow"},
                        {'range': [66, 100], 'color': "red"}
                    ]
                }
            ))
            st.plotly_chart(fig)
    
    # Domain Insights tab
    with tabs[1]:
        st.subheader("Domain Insights")
        
        # Display trends
        st.markdown("### Key Trends")
        for idx, trend in enumerate(st.session_state.insights['trends']):
            st.markdown(f"**{idx+1}.** {trend}")
        
        # Display patterns
        st.markdown("### Identified Patterns")
        for idx, pattern in enumerate(st.session_state.insights['patterns']):
            st.markdown(f"**{idx+1}.** {pattern}")
        
        # Display gaps
        st.markdown("### Potential Gaps")
        for idx, gap in enumerate(st.session_state.insights['gaps']):
            st.markdown(f"**{idx+1}.** {gap}")
            
        # Display relevance scores
        st.markdown("### Domain Relevance")
        relevance_data = st.session_state.insights['domain_relevance']
        df = pd.DataFrame(list(relevance_data.items()), columns=['Domain', 'Relevance'])
        df = df.sort_values('Relevance', ascending=False)
        
        fig = px.bar(df, x='Domain', y='Relevance', title="Domain Relevance Scores")
        st.plotly_chart(fig)
    
    # Innovation Suggestions tab
    with tabs[2]:
        st.subheader("Innovation Suggestions")
        
        # Main solutions
        st.markdown("### Proposed Solutions")
        for idx, solution in enumerate(st.session_state.innovations['solutions']):
            st.markdown(f"**Solution {idx+1}:** {solution['title']}")
            st.markdown(f"*{solution['description']}*")
            st.markdown("**Approach:**")
            st.markdown(solution['approach'])
            st.markdown("---")
        
        # Cross-domain innovations
        st.markdown("### Cross-Domain Innovation Ideas")
        for idx, idea in enumerate(st.session_state.innovations['cross_domain']):
            st.markdown(f"**{idx+1}.** {idea}")
        
        # Technology suggestions
        st.markdown("### Suggested Technologies")
        tech_data = st.session_state.innovations['technologies']
        tech_df = pd.DataFrame(tech_data)
        
        # Create column chart for technology relevance
        fig = px.bar(
            tech_df, 
            x='technology', 
            y='relevance', 
            color='category',
            title="Suggested Technologies by Relevance"
        )
        st.plotly_chart(fig)
    
    # Action Plan tab
    with tabs[3]:
        st.subheader("Prioritized Action Plan")
        
        # Display the prioritized actions
        actions = st.session_state.prioritized_actions
        
        # Create a dataframe for the actions
        actions_df = pd.DataFrame(actions)
        
        # Display as a bubble chart
        fig = px.scatter(
            actions_df, 
            x='difficulty', 
            y='impact', 
            size='priority_score',
            color='priority_score',
            hover_name='action',
            size_max=60,
            title="Action Priority Matrix",
            labels={'difficulty': 'Difficulty (Lower is Easier)', 'impact': 'Impact (Higher is Better)'}
        )
        st.plotly_chart(fig)
        
        # Display as a table
        st.markdown("### Prioritized Steps")
        for idx, action in enumerate(actions):
            with st.expander(f"Step {idx+1}: {action['action']} (Score: {action['priority_score']:.1f})"):
                st.markdown(f"**Description:** {action['description']}")
                st.markdown(f"**Impact:** {action['impact']}/10")
                st.markdown(f"**Difficulty:** {action['difficulty']}/10")
                st.markdown(f"**Timeframe:** {action['timeframe']}")
                st.markdown(f"**Resources needed:** {action['resources']}")

elif st.session_state.get('analyzed', False) and not st.session_state.problem_input:
    st.warning("Please enter a problem statement or select a sample problem.")

# Footer
st.markdown("---")
st.markdown("**HACKSEEK** | Powering Innovative Problem Solving")
