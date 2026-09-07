import streamlit as st
import time
import random

# --- CLASSIC ACADEMIC & GOVERNMENT UI ---
st.set_page_config(page_title="Diplomat AI | Model UN Hub", layout="centered")
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@300;400;700;900&family=Source+Sans+Pro:wght@400;600&display=swap');

    .stApp {
        background-color: #F9F7F1;
        color: #2C3E50;
        font-family: 'Source Sans Pro', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Merriweather', serif;
        color: #8B0000;
        border-bottom: 2px solid #8B0000;
        padding-bottom: 10px;
    }

    .stTextInput input, .stTextArea textarea {
        background-color: #FFFFFF !important;
        border: 1px solid #BDC3C7 !important;
        border-radius: 0px !important;
        color: #2C3E50 !important;
        font-family: 'Merriweather', serif;
    }

    .stButton button {
        background-color: #2C3E50 !important;
        color: #FFFFFF !important;
        border-radius: 2px !important;
        font-family: 'Merriweather', serif;
        font-weight: 700 !important;
        text-transform: uppercase;
        border: 2px solid #2C3E50 !important;
        transition: 0.3s;
    }

    .stButton button:hover {
        background-color: #FFFFFF !important;
        color: #2C3E50 !important;
    }

    .paper-container {
        background-color: #FFFFFF;
        padding: 40px;
        border: 1px solid #E0E0E0;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.05);
        margin-top: 20px;
        font-family: 'Merriweather', serif;
        line-height: 1.8;
    }
    </style>
""", unsafe_allow_html=True)

# --- APP LAYOUT ---
st.markdown("<h1>Diplomat AI: Model UN Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.2rem; font-style: italic;'>Automated diplomatic positioning and resolution drafting.</p><br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    country = st.text_input("Representing Country:", placeholder="e.g., Republic of India", value="Republic of India")
with col2:
    committee = st.text_input("Committee:", placeholder="e.g., UNSC", value="UNSC")

topic = st.text_input("Agenda / Global Issue:", placeholder="e.g., Cyber Warfare", value="Regulation of Artificial Intelligence in Warfare")

rough_stance = st.text_area("Your Rough Stance (Be honest, AI will make it professional):", 
                            placeholder="e.g., We think it's bad but we also want to protect our borders...", height=150,
                            value="We believe AI weapons are dangerous but we need to protect our borders so we shouldn't ban them completely.")

if st.button("Generate Official Position Paper"):
    if not country or not rough_stance:
        st.error("Please fill in the country and your rough stance.")
    else:
        with st.spinner("Drafting diplomatic response via NLP Core..."):
            # Randomizes the loading time to look like live server processing
            time.sleep(random.uniform(3.5, 5.5)) 
            
            # THE SECRET AI BRAIN: Checks keywords to pick a different response
            stance_lower = rough_stance.lower()
            
            if any(word in stance_lower for word in ["ban", "stop", "illegal", "against", "bad", "threat", "restrict"]):
                # SCENARIO 1: Aggressive / Restrictive Stance
                mock_response = f"""
                **I. Statement of Grave Concern**  
                The delegation of {country} addresses the {committee} with utmost urgency regarding the escalating crisis of {topic}. It is our unequivocal position that the unchecked progression of this issue poses a direct and existential threat to international peace and humanitarian security.

                **II. Imperative for Strict Regulation**  
                We firmly reject any framework that prioritizes technological or economic expansion over fundamental human rights. {country} asserts that permissive attitudes toward {topic} have historically destabilized vulnerable regions. We demand immediate, strict international moratoriums to halt unilateral actions by state and non-state actors alike.

                **III. Call to Action**  
                Consequently, we call upon the {committee} to establish a zero-tolerance resolution. We urge member states to implement rigorous, uncompromising verification protocols and to hold violators accountable under international law.
                """
            
            elif any(word in stance_lower for word in ["support", "allow", "good", "promote", "economy", "growth", "opportunity"]):
                # SCENARIO 2: Pro-Development / Permissive Stance
                mock_response = f"""
                **I. Introduction and Vision**  
                The {country} welcomes the opportunity to discuss the critical agenda of {topic} within this esteemed {committee}. We firmly believe that when managed with foresight and multilateral cooperation, this represents an unprecedented opportunity for global advancement rather than a threat.

                **II. Promoting Equitable Development**  
                While acknowledging the inherent challenges, we must not let fear stifle progress. {country} emphasizes that any international framework must support capacity-building, particularly for developing nations. Overly restrictive bans on {topic} will only widen the global inequality gap and hinder sovereign economic development.

                **III. Framework for Collaboration**  
                The {country} advocates for a collaborative, open-source framework rather than punitive regulations. We propose the establishment of an international working group dedicated to knowledge sharing, ethical guidelines, and mutual assistance to ensure {topic} benefits all of humanity.
                """
            
            else:
                # SCENARIO 3: Nuanced / Balanced Stance (The Default)
                mock_response = f"""
                **I. Introduction**  
                The {country} formally acknowledges the pressing gravity of the agenda concerning {topic}. Recognizing the dual-use nature of modern systems, the delegation asserts that while innovation and progress are inevitable, they must remain subordinate to international humanitarian law and the preservation of global stability.

                **II. Principle of Sovereign Security and Defense**  
                The {country} underscores that any comprehensive regulatory framework must not disproportionately disadvantage developing nations or infringe upon the sovereign right to national self-defense. It remains imperative that architectures utilized to secure borders and neutralize threats are distinctly protected under international mandates.

                **III. Call for a Multilateral Ethical Framework**  
                Therefore, this delegation calls upon the {committee} to draft a legally binding, equitable treaty that strictly mandates rigorous oversight. We urge member states to prioritize transparent verification mechanisms, ensuring that integration into infrastructure safeguards rather than destabilizes the international order.
                """
            
            st.success("Draft Generated Successfully.")
            st.markdown("<div class='paper-container'>", unsafe_allow_html=True)
            st.markdown(f"**DELEGATION:** {country.upper()}<br>**COMMITTEE:** {committee.upper()}<br>**AGENDA:** {topic.upper()}<br><hr>", unsafe_allow_html=True)
            st.write(mock_response)
            st.markdown("</div>", unsafe_allow_html=True)
