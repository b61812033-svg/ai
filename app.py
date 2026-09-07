import streamlit as st
import time
import random

# --- DATA SCIENCE / DEVELOPER UI ---
st.set_page_config(page_title="CycleForge | AI Lifecycle", layout="wide")
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Outfit:wght@400;700;900&display=swap');

    .stApp {
        background-color: #0D1117; /* GitHub Dark Slate */
        color: #C9D1D9;
        font-family: 'Outfit', sans-serif;
    }
    
    h1 {
        font-weight: 900;
        font-size: 3.5rem !important;
        background: -webkit-linear-gradient(45deg, #FF79C6, #8BE9FD);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }

    h3, h4 {
        color: #8BE9FD;
    }

    .stTextInput input, .stTextArea textarea {
        background-color: #161B22 !important;
        border: 1px solid #30363D !important;
        border-radius: 6px !important;
        color: #58A6FF !important;
        font-family: 'Fira Code', monospace;
    }
    
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #FF79C6 !important;
    }

    .stButton button {
        background-color: #238636 !important; /* Hacker Green */
        color: #FFFFFF !important;
        border-radius: 6px !important;
        font-family: 'Fira Code', monospace;
        font-weight: 600 !important;
        border: 1px solid rgba(240, 246, 252, 0.1) !important;
        transition: 0.2s;
        padding: 0.5rem 1rem;
    }

    .stButton button:hover {
        background-color: #2EA043 !important;
        transform: scale(1.02);
    }

    .terminal-box {
        background-color: #010409;
        border: 1px solid #30363D;
        border-radius: 8px;
        padding: 25px;
        font-family: 'Fira Code', monospace;
        font-size: 0.9rem;
        color: #E6EDF3;
        line-height: 1.6;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    
    .highlight { color: #FF79C6; font-weight: bold; }
    .stage { color: #8BE9FD; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- APP LAYOUT ---
st.markdown("<h1>CycleForge AI ⚙️</h1>", unsafe_allow_html=True)
st.markdown("### The automated AI Project Cycle architect for real-world problems.")
st.markdown("<hr style='border-color: #30363D;'>", unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("#### 1. Define the Problem")
    target_problem = st.text_area(
        "Enter a real-world problem to solve:", 
        placeholder="e.g., Heavy traffic congestion outside the school during dismissal time.",
        value="Heavy traffic congestion outside the school during dismissal time.",
        height=100
    )
    
    target_audience = st.text_input("Who is facing this problem?", value="Students, Parents, and Local Commuters")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Initialize AI Project Cycle 🚀"):
        
        # FAKE LOADING ANIMATION (Makes it look incredibly realistic)
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        stages = ["Initializing Problem Scoping...", "Gathering Data Acquisition parameters...", "Simulating Data Exploration...", "Selecting ML Models...", "Finalizing Deployment Architecture..."]
        
        for i in range(100):
            time.sleep(0.04) # Total ~4 seconds
            progress_bar.progress(i + 1)
            if i % 20 == 0:
                status_text.markdown(f"**{stages[i//20]}**")
        
        status_text.empty()
        progress_bar.empty()
        
        # MOCKED DYNAMIC RESPONSE
        mock_roadmap = f"""
        <div class="terminal-box">
            <span style="color: #2EA043;">>> PROJECT CYCLE GENERATED SUCCESSFULLY</span><br><br>
            
            <span class="stage">[STAGE 1] PROBLEM SCOPING (The 4Ws)</span><br>
            - <span class="highlight">Who:</span> {target_audience}.<br>
            - <span class="highlight">What:</span> {target_problem}.<br>
            - <span class="highlight">Where:</span> School zones and surrounding local infrastructure.<br>
            - <span class="highlight">Why:</span> To reduce carbon emissions, save time, and prevent accidents during peak hours.<br><br>
            
            <span class="stage">[STAGE 2] DATA ACQUISITION</span><br>
            - Deploy IoT traffic cameras to count vehicles.<br>
            - Collect school bell timings and weather data via APIs.<br>
            - Ensure data privacy by blurring license plates (Ethical AI constraint).<br><br>
            
            <span class="stage">[STAGE 3] DATA EXPLORATION</span><br>
            - Plotting histograms of traffic volume vs. time of day.<br>
            - Identifying anomalies (e.g., massive spikes on rainy days).<br><br>
            
            <span class="stage">[STAGE 4] MODELLING</span><br>
            - <span class="highlight">Approach:</span> Learning-Based Model.<br>
            - <span class="highlight">Algorithm:</span> Time-Series Forecasting (Predicting future traffic based on past patterns) & Computer Vision (YOLOv8 for vehicle counting).<br><br>
            
            <span class="stage">[STAGE 5] EVALUATION</span><br>
            - Split dataset into 80% Training / 20% Testing.<br>
            - Target Metric: 92% Precision in predicting gridlocks 15 minutes before they happen.<br><br>
            
            <span class="stage">[STAGE 6] DEPLOYMENT</span><br>
            - Integrate predictions into a mobile app for parents.<br>
            - Automate smart traffic lights at the school intersection based on real-time AI predictions.
        </div>
        """
        st.session_state.roadmap = mock_roadmap
        st.toast("Cycle mapping complete!", icon="✅")

with col2:
    st.markdown("#### 2. Lifecycle Output Terminal")
    if "roadmap" in st.session_state:
        st.markdown(st.session_state.roadmap, unsafe_allow_html=True)
    else:
        st.info("Awaiting problem input... Click 'Initialize' to generate the 6-stage lifecycle.")
        
    # Extra flex: A fake model accuracy visualizer
    if "roadmap" in st.session_state:
        st.markdown("<br>#### 📊 Model Accuracy Simulator", unsafe_allow_html=True)
        acc = random.randint(88, 96)
        st.metric(label="Simulated Training Accuracy", value=f"{acc}.4%", delta="+2.1% improvement")    }

    .stButton button {
        background-color: #CCFF00 !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
        border-radius: 12px !important;
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700 !important;
        font-size: 1.2rem !important;
        padding: 10px 20px !important;
        box-shadow: 5px 5px 0px #000000;
        transition: all 0.1s;
    }

    .stButton button:hover {
        box-shadow: 0px 0px 0px #000000;
        transform: translate(5px, 5px);
    }

    .card {
        background-color: #F8FAFC;
        border: 2px solid #000000;
        border-radius: 16px;
        padding: 30px;
        box-shadow: 8px 8px 0px #E2E8F0;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- APP LAYOUT ---
st.markdown("<h1>FinQuest AI 🏦</h1>", unsafe_allow_html=True)
st.markdown("### Master your money. Crush the finance olympiads.")

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 🎯 Your Goal")
    pocket_money = st.number_input("Monthly Pocket Money (₹):", min_value=100, value=1000, step=100)
    goal = st.text_input("What are you saving for?", placeholder="e.g., New headphones", value="New Mechanical Keyboard")
    goal_cost = st.number_input("How much does it cost? (₹):", min_value=100, value=3500, step=100)
    
    if st.button("Generate Strategy"):
        with st.spinner("Crunching financial algorithms..."):
            time.sleep(5)
            
            savings_per_month = pocket_money * 0.2
            months_to_goal = math.ceil(goal_cost / savings_per_month) if savings_per_month > 0 else 0
            
            mock_plan = f"""
            ### 🚀 The Gen-Z Wealth Blueprint
            Yo! You want to secure that **{goal}** without going completely broke? We got you. Here is your roadmap to hitting ₹{goal_cost} while keeping your allowance intact.

            **Step 1: The 50/30/20 Split 🍕**
            *   **50% (₹{int(pocket_money * 0.5)}):** Needs (Transport, mobile recharge, school stuff).
            *   **30% (₹{int(pocket_money * 0.3)}):** Wants (Food with friends, weekend gaming).
            *   **20% (₹{int(savings_per_month)}):** The Lockbox. Put this straight toward the {goal}.

            **Step 2: The Timeline ⏳**
            Saving ₹{int(savings_per_month)} a month means you'll hit your target of ₹{goal_cost} in **about {months_to_goal} months**. Want it faster? Bump that 20% to 40% by cutting back on the "Wants" category.

            **💡 FinLit Concept of the Day: Opportunity Cost**
            Every time you spend ₹500 on fast food, the *opportunity cost* is that you delay buying your {goal} by another week. Every rupee has a job!
            """
            st.session_state.plan = mock_plan
            st.toast("Roadmap Generated!", icon="💸")

with col2:
    if "plan" in st.session_state:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 📈 Your AI Wealth Roadmap")
        st.write(st.session_state.plan)
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><hr style='border: 1px solid #000;'><br>", unsafe_allow_html=True)

st.markdown("### 🧠 Rapid-Fire FinLit Quiz")
if st.button("Generate Random Finance Question"):
    with st.spinner("Fetching Olympiad-level question..."):
        time.sleep(3)
        mock_quiz = """
        **Q: What is the primary advantage of "Compound Interest" over "Simple Interest"?**
        
        A) It guarantees the stock market will go up.  
        B) It calculates interest on both the initial principal and the accumulated interest from previous periods.  
        C) It means you don't have to pay taxes on your earnings.  
        D) It is a fixed rate set by the government.  
        
        *(Scroll down for the answer...)*
        <br><br><br>
        *Answer: B! Your money makes money, and then THAT money makes even MORE money. 💸*
        """
        st.info(mock_quiz)
