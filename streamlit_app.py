import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set page config
st.set_page_config(
    page_title="Gender Responsive Workplace",
    page_icon="♀♂",
    layout="wide",
)

# Custom CSS for better appearance
st.markdown("""
<style>
    .main-header {
        font-size: 2.3rem;
        color: #2E7D32;
        text-align: center;
        margin-bottom: 20px;
    }
    .section-header {
        font-size: 1.5rem;
        color: #1565C0;
        margin-top: 25px;
        margin-bottom: 15px;
    }
    .case-box {
        background-color: #E3F2FD;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
        border-left: 5px solid #1565C0;
    }
    .response-box {
        background-color: #FFFDE7;
        padding: 15px;
        border-radius: 10px;
        margin-top: 15px;
        border-left: 5px solid #FBC02D;
    }
    .info-box {
        background-color: #E8F5E9;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    .footer {
        font-size: 0.8rem;
        color: #757575;
        text-align: center;
        margin-top: 50px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.title("Workshop Navigation")
    
    # Simple navigation
    page = st.radio(
        "Select a section:",
        ["Introduction", "Case Studies Explorer", "Quick Gender Audit", "Commitment Wall"]
    )
    
    st.markdown("---")
    st.markdown("**Workshop: Gender, One Health, Safeguarding, and Human Rights Principles Training**")
    st.markdown("**Presenter: Prof. Salome Bukachi**")
    st.markdown("**University of Nairobi**")

# INTRODUCTION PAGE
if page == "Introduction":
    st.markdown('<h1 class="main-header">Gender-Responsive Workplaces</h1>', unsafe_allow_html=True)
    
    # Two-column layout for intro section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<h2 class="section-header">What is a Gender-Responsive Workplace?</h2>', unsafe_allow_html=True)
        
        st.markdown("""
        A gender-responsive workplace:
        
        1. Notices the not-usually-visible needs and problems of women employees
        2. Creates solutions in response to these needs
        3. Takes steps and actions to implement the created solutions
        4. Monitors the results in the long term
        5. Actively endeavors to increase the satisfaction of employees and to remedy complaints
        
        *Source: A Guide for Gender-Responsive Companies and Institutions*
        """)
        
        st.markdown('<h2 class="section-header">Why Gender-Responsive Workplaces Matter</h2>', unsafe_allow_html=True)
        
        st.markdown("""
        • Diverse teams produce more innovative research
        • Better problem-solving through varied perspectives
        • More comprehensive research design
        • Improved community engagement
        • Enhanced research relevance for diverse populations
        """)
    
    with col2:
        # Add a simple illustration or chart
        labels = ['Male', 'Female']
        leadership = [85, 15]  # Example data
        researchers = [55, 45]  # Example data
        
        fig, ax = plt.subplots(figsize=(8, 6))
        x = np.arange(len(labels))
        width = 0.35
        
        ax.bar(x - width/2, leadership, width, label='Leadership Positions', color='#1565C0')
        ax.bar(x + width/2, researchers, width, label='Researchers', color='#2E7D32')
        
        ax.set_ylabel('Percentage')
        ax.set_title('Gender Representation Gap in Research Organizations')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()
        
        st.pyplot(fig)
        
        st.markdown("*Example data showing the gender gap between research staff and leadership positions*")
    
    # Simple interactive reflection element
    st.markdown('<h2 class="section-header">Reflection: Gender Dynamics in Your Workplace</h2>', unsafe_allow_html=True)
    
    st.markdown("Select any statements that reflect your experience or observations:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        reflection1 = st.checkbox("I have witnessed gender bias at work")
        reflection2 = st.checkbox("I know someone who was denied a promotion due to gender")
        reflection3 = st.checkbox("I believe the gender pay gap exists in my organization")
    
    with col2:
        reflection4 = st.checkbox("I have felt unheard in a meeting because of my gender")
        reflection5 = st.checkbox("I think flexible work policies are applied differently for men and women")
        reflection6 = st.checkbox("I've observed different standards for mothers vs. fathers at work")
    
    # Show insights based on selections
    if any([reflection1, reflection2, reflection3, reflection4, reflection5, reflection6]):
        selected = sum([reflection1, reflection2, reflection3, reflection4, reflection5, reflection6])
        
        st.markdown('<div class="response-box">', unsafe_allow_html=True)
        st.markdown(f"You selected {selected} statement(s). These observations are common in many organizations.")
        
        if reflection1:
            st.markdown("**Gender bias** can manifest in subtle ways, from who gets called on in meetings to how performance is evaluated.")
            
        if reflection2:
            st.markdown("**Promotion barriers** often stem from biased perceptions of leadership abilities and potential.")
            
        if reflection3:
            st.markdown("**Pay disparities** persist in many sectors, often beginning with initial salary negotiations and compounding over time.")
            
        if reflection4:
            st.markdown("**Being unheard** in meetings is a common experience, especially for women and those from marginalized groups.")
            
        if reflection5:
            st.markdown("**Flexibility stigma** often affects women more than men, with assumptions about who 'should' use family leave policies.")
            
        if reflection6:
            st.markdown("**Parental double standards** remain prevalent, with different expectations for mothers versus fathers in the workplace.")
            
        st.markdown("</div>", unsafe_allow_html=True)

# CASE STUDIES EXPLORER
elif page == "Case Studies Explorer":
    st.markdown('<h1 class="main-header">Case Studies Explorer</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    Explore these real-world-inspired scenarios and discuss potential solutions with your group.
    Select a case study to view details and discussion questions.
    """)
    
    # Case study selection
    case_study = st.selectbox(
        "Select a case study:",
        [
            "Case 1: The Invisible Candidate",
            "Case 2: The Salary Secret",
            "Case 3: The Broken Ladder",
            "Case 4: The Dedicated Father vs. Distracted Mother",
            "Case 5: The Diversity Hire"
        ]
    )
    
    # Case study content
    cases = {
        "Case 1: The Invisible Candidate": {
            "scenario": """
            Dr. Sarah, a senior researcher with an impressive publication record in entomology, recently applied for the position of Department Head. 
            Despite her strong publication record and successful grant history, she consistently finds herself on the shortlist but never selected. 
            
            During a recent recruitment, she overheard colleagues suggesting she might not be 'assertive enough' to lead the department, and that her family responsibilities might interfere with leadership duties. 
            
            Meanwhile, a male colleague with fewer publications but known for his confident presentation style is being strongly considered for the position.
            """,
            "questions": [
                "What biases are present in this hiring decision?",
                "How do stereotypes about leadership impact women's career growth?",
                "What organizational policies could prevent such biased hiring?"
            ],
            "key_issues": [
                "Gender stereotypes about leadership qualities",
                "Assumptions about family responsibilities",
                "Valuing style over substance in leadership assessment",
                "Implicit bias in evaluation criteria"
            ]
        },
        "Case 2: The Salary Secret": {
            "scenario": """
            During an informal lunch discussion, three researchers at a research organization discover significant differences in their starting salaries despite similar qualifications and experience. 
            
            Dr. James started at $5,000 higher than Dr. Lucy, though both joined the same project last year with comparable expertise. Dr. Lucy learns that James negotiated his salary aggressively while she accepted the first offer, having been previously advised to 'be grateful' for opportunities. 
            
            The conversation reveals a pattern where female colleagues consistently started at lower salary points, creating a compounding effect on their career earnings.
            """,
            "questions": [
                "What structural issues enable gender pay disparities to persist?",
                "Why do women often face challenges in salary negotiations?",
                "What policies could create more equitable compensation?"
            ],
            "key_issues": [
                "Lack of salary transparency",
                "Gendered expectations in negotiation",
                "Socialization differences that affect negotiation behavior",
                "Compounding effects of initial pay disparities"
            ]
        },
        "Case 3: The Broken Ladder": {
            "scenario": """
            At an organization's annual research symposium, Dr. Grace notices that while 45% of junior researchers are women, only 15% of research department heads are female. 
            
            When a leadership position opens in her department, she witnesses a familiar pattern: senior female researchers are directed toward 'support roles' like committee work and mentoring, while male colleagues are encouraged to pursue executive positions. 
            
            Despite her strong track record in both research and team management, she's advised to 'gain more experience' before pursuing leadership roles.
            """,
            "questions": [
                "How do informal mentoring and guidance differ by gender?",
                "What role do institutional networks play in leadership advancement?",
                "How can leadership development be made more inclusive?"
            ],
            "key_issues": [
                "Pipeline problems vs. 'leaky bucket' issues",
                "Gender differences in mentoring and sponsorship",
                "Hidden workload of service activities for women",
                "Moving goalposts for advancement requirements"
            ]
        },
        "Case 4: The Dedicated Father vs. Distracted Mother": {
            "scenario": """
            Two researchers at a research organization, Thomas and Diana, both have young children. 
            
            When Thomas leaves early for his child's school event, colleagues praise him as a 'dedicated father.' When Diana does the same, subtle comments arise about her 'divided priorities.' 
            
            During fieldwork planning, assumptions are made about Diana's availability for extended field visits, while Thomas's parental status is never mentioned. 
            
            The situation intensifies when both apply for project leadership roles, and concerns about Diana's 'reliability' are raised due to her family responsibilities.
            """,
            "questions": [
                "How do gendered expectations about caregiving affect career progression?",
                "Why are similar actions interpreted differently based on gender?",
                "What policies could address these double standards?"
            ],
            "key_issues": [
                "Double standards for parenting responsibilities",
                "Different narratives for the same behavior based on gender",
                "Unexamined assumptions about availability and commitment",
                "How 'ideal worker' norms disadvantage women"
            ]
        },
        "Case 5: The Diversity Hire": {
            "scenario": """
            Dr. Aisha, a young female researcher from Northern Kenya, joins an organization's climate change adaptation project. 
            
            Despite her innovative research approach and strong academic background, she frequently encounters colleagues who assume she was hired to 'tick boxes.' She faces multiple layers of bias - some question her expertise because of her gender, others make assumptions about her background, and she often finds herself having to repeatedly prove her competence. 
            
            During team meetings, she notices her suggestions gain traction only when repeated by others.
            """,
            "questions": [
                "How do multiple aspects of identity impact workplace experiences?",
                "What are the cumulative effects of facing multiple forms of bias?",
                "How can organizations address intersectional challenges?"
            ],
            "key_issues": [
                "Intersectionality of gender, ethnicity, and age biases",
                "Stereotype threat and its impact on performance",
                "Tokenism and its psychological burden",
                "'Prove it again' bias affecting marginalized groups"
            ]
        }
    }
    
    # Display selected case
    selected_case = cases[case_study]
    
    st.markdown('<div class="case-box">', unsafe_allow_html=True)
    st.markdown("### Scenario")
    st.markdown(selected_case["scenario"])
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Display questions and key issues
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Discussion Questions")
        for q in selected_case["questions"]:
            st.markdown(f"- {q}")
    
    with col2:
        st.markdown("### Key Issues to Consider")
        for issue in selected_case["key_issues"]:
            st.markdown(f"- {issue}")
    
    # Simple response section
    st.markdown("### Group Responses")
    
    group_insights = st.text_area("What are your group's key insights about this case?", height=100)
    proposed_solutions = st.text_area("What solutions would your group propose?", height=100)
    
    if st.button("Share with Workshop"):
        if group_insights and proposed_solutions:
            st.markdown('<div class="response-box">', unsafe_allow_html=True)
            st.markdown("#### Thank you for sharing your insights!")
            st.markdown("Your contributions will be included in the workshop discussion. Be prepared to share key points with the larger group.")
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("Please enter both insights and proposed solutions before sharing.")

# QUICK GENDER AUDIT
elif page == "Quick Gender Audit":
    st.markdown('<h1 class="main-header">Quick Gender Audit</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    This simplified gender audit will help you assess the gender-responsiveness of your workplace.
    Rate your department or organization on each dimension, then see your results.
    """)
    
    # Simple form for the gender audit
    with st.form("gender_audit_form"):
        st.markdown("### Rate your workplace on these dimensions (1-5)")
        st.markdown("1 = Needs significant improvement, 5 = Exemplary")
        
        leadership_score = st.slider("Leadership & Decision-Making", 1, 5, 3, 
                                    help="Consider gender balance in leadership positions and decision-making processes")
        
        recruitment_score = st.slider("Recruitment & Promotion Practices", 1, 5, 3,
                                     help="Consider gender fairness in hiring, promotion, and career advancement")
        
        environment_score = st.slider("Work Environment & Culture", 1, 5, 3,
                                     help="Consider gender bias, harassment policies, and inclusive culture")
        
        balance_score = st.slider("Work-Life Balance Support", 1, 5, 3,
                                 help="Consider parental leave, flexible work, and caregiving accommodations")
        
        resources_score = st.slider("Resource Allocation & Opportunities", 1, 5, 3,
                                   help="Consider equitable access to funding, equipment, and professional development")
        
        submit_button = st.form_submit_button("See Results")
    
    # Display results if form submitted
    if submit_button:
        scores = [leadership_score, recruitment_score, environment_score, balance_score, resources_score]
        average_score = sum(scores) / len(scores)
        
        st.markdown("### Your Gender Audit Results")
        
        # Create a simple visualization
        categories = ['Leadership', 'Recruitment', 'Environment', 'Work-Life', 'Resources']
        
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(categories, scores, color=['#1976D2', '#2E7D32', '#7B1FA2', '#C62828', '#F57F17'])
        
        # Add a horizontal line for the average
        ax.axhline(y=3, color='gray', linestyle='--', alpha=0.7)
        
        # Customize the chart
        ax.set_ylim(0, 5.5)
        ax.set_ylabel('Score (1-5)')
        ax.set_title('Gender-Responsiveness by Category')
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{height}',
                    ha='center', va='bottom')
        
        st.pyplot(fig)
        
        # Provide a simple interpretation
        st.markdown(f"**Overall Gender-Responsiveness Score: {average_score:.1f}/5**")
        
        # Simple recommendations based on lowest scores
        lowest_categories = sorted(zip(categories, scores), key=lambda x: x[1])[:2]
        
        st.markdown("### Focus Areas for Improvement")
        st.markdown("Based on your assessment, consider these priority areas:")
        
        for category, score in lowest_categories:
            st.markdown(f"**{category} (Score: {score})**")
            
            if category == 'Leadership':
                st.markdown("""
                • Establish clear, objective criteria for leadership selection
                • Create mentoring programs that connect women with leadership opportunities
                • Review decision-making processes for inclusivity
                """)
            elif category == 'Recruitment':
                st.markdown("""
                • Implement blind resume screening where possible
                • Train hiring committees on recognizing implicit bias
                • Standardize interview questions and evaluation metrics
                """)
            elif category == 'Environment':
                st.markdown("""
                • Develop and enforce clear anti-harassment policies
                • Create channels for reporting bias or discrimination
                • Provide regular gender sensitivity training
                """)
            elif category == 'Work-Life':
                st.markdown("""
                • Review flexible work policies for accessibility to all genders
                • Normalize parental leave for all parents
                • Consider caregiving responsibilities in meeting and travel schedules
                """)
            elif category == 'Resources':
                st.markdown("""
                • Audit resource allocation patterns by gender
                • Create transparent processes for equipment and funding requests
                • Ensure equal access to professional development opportunities
                """)

# COMMITMENT WALL
elif page == "Commitment Wall":
    st.markdown('<h1 class="main-header">Commitment Wall</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    Share one concrete action you commit to taking to help create a more gender-responsive workplace.
    Your commitment will be displayed on our digital commitment wall.
    """)
    
    # Form for commitment submission
    with st.form("commitment_form"):
        name = st.text_input("Your Name (Optional):")
        department = st.text_input("Department/Unit:")
        
        commitment_type = st.selectbox(
            "Type of Commitment:",
            [
                "Personal Practice Change",
                "Advocating for Policy Change",
                "Supporting Colleagues",
                "Challenging Bias",
                "Creating Resources",
                "Other"
            ]
        )
        
        commitment = st.text_area("I commit to:", height=100, 
                                  placeholder="Example: I commit to ensuring gender balance on all hiring committees I participate in...")
        
        submit_commitment = st.form_submit_button("Add My Commitment")
    
    # Display submitted commitment
    if submit_commitment:
        if commitment:
            st.success("Thank you for your commitment!")
            
            # Display the commitment
            st.markdown('<div class="response-box">', unsafe_allow_html=True)
            if name:
                st.markdown(f"**{name}** from **{department}** commits to:")
            else:
                st.markdown(f"A participant from **{department}** commits to:")
            
            st.markdown(f"*{commitment}*")
            st.markdown(f"**Area**: {commitment_type}")
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Simple encouragement
            st.markdown("""
            ### Making Change Happen
            
            Remember that creating a gender-responsive workplace requires both individual and collective action.
            
            Small changes in daily practices can lead to significant shifts in workplace culture over time.
            
            Consider sharing your commitment with colleagues and checking in on progress in 1-2 months.
            """)
        else:
            st.warning("Please enter your commitment before submitting.")
    
    # Display sample commitments
    st.markdown("### Examples from Others")
    
    sample_commitments = [
        {
            "name": "Dr. Thomas Odhiambo",
            "department": "Entomology",
            "type": "Challenging Bias",
            "commitment": "I commit to speaking up when I notice colleagues being interrupted in meetings, ensuring everyone has an equal chance to contribute."
        },
        {
            "name": "Dr. Jane Mwangi",
            "department": "Vector Biology",
            "type": "Supporting Colleagues",
            "commitment": "I commit to mentoring at least two junior female researchers in my field and advocating for their inclusion in key research projects."
        },
        {
            "name": "John Kamau",
            "department": "Human Resources",
            "type": "Advocating for Policy Change",
            "commitment": "I commit to conducting a gender pay analysis within our department and presenting recommendations to leadership."
        }
    ]
    
    for i, comm in enumerate(sample_commitments):
        st.markdown(f"<div class='info-box'>", unsafe_allow_html=True)
        st.markdown(f"**{comm['name']}** from **{comm['department']}** commits to:")
        st.markdown(f"*{comm['commitment']}*")
        st.markdown(f"**Area**: {comm['type']}")
        st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.markdown("Gender, One Health, Safeguarding, and Human Rights Principles Training Workshop")
st.markdown("International Centre of Insect Physiology and Ecology (ICIPE), Nairobi, Kenya • February 2025")
st.markdown("</div>", unsafe_allow_html=True)