import math
import time
import streamlit as st

# --- GEN-Z FINTECH / NEO-BRUTALISM UI ---
st.set_page_config(page_title="FinQuest AI", layout="wide")
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap');

    .stApp {
        background-color: #FFFFFF;
        color: #000000;
        font-family: 'Space Grotesk', sans-serif;
    }
    
    h1 {
        font-weight: 700;
        font-size: 4rem !important;
        letter-spacing: -2px;
        color: #000000;
    }

    .stTextInput input, .stNumberInput input {
        background-color: #F3F4F6 !important;
        border: 2px solid #000000 !important;
        border-radius: 12px !important;
        color: #000000 !important;
        font-weight: 600;
        box-shadow: 4px 4px 0px #000000;
        transition: 0.2s;
    }
    
    .stTextInput input:focus, .stNumberInput input:focus {
        box-shadow: 2px 2px 0px #000000;
        transform: translate(2px, 2px);
    }

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
