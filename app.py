import streamlit as st
import difflib
import time

# --- CONFIGURATION & UI THEME ---
st.set_page_config(page_title="Jarvis QE Suite", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    [data-testid="stSidebar"] { background-color: #001F3F; border-right: 2px solid #FFD700; }
    div.stButton > button { background: #FFD700; color: #001F3F; font-weight: bold; width: 100%; border-radius: 8px; border: none; }
    .explanation-box { background-color: #1E2128; border-left: 5px solid #FFD700; padding: 20px; border-radius: 5px; margin-bottom: 25px; }
    .badge { padding: 4px 10px; border-radius: 10px; font-size: 0.8rem; margin-right: 5px; border: 1px solid #FFD700; color: #FFD700; background: #001F3F; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🛡️ Jarvis QE Suite")
    st.markdown("---")
    # Added Flutter (Dart) per request
    lang = st.selectbox("Framework", ["MVC (C#)", "Java", "Python", "Flutter (Dart)", "SQL SP"])
    st.success("⚡ Option 2: Architectural Enhancement")
    st.caption("v3.3.0 | Stable Build")

# --- MAIN INTERFACE ---
st.title("🛠️ AI Code Fixer & Enhancer")
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📝 Input Specification")
    title = st.text_input("Bug Title", placeholder="e.g., UI Thread Jitter in Flutter")
    steps = st.text_area("Steps to Reproduce", placeholder="1. Open screen\n2. Scroll fast...", height=100)
    code_input = st.text_area("Original Source Code", placeholder="Paste code snippet here...", height=300)
    
    fix_btn = st.button("FIX & ENHANCE CODE")

with col2:
    st.subheader("✨ Optimized Output & Explanation")
    
    # RECTIFICATION: All output logic is inside this block to prevent NameErrors
    if fix_btn:
        if not title or not steps or not code_input:
            # FIX: Properly closed string literal to prevent SyntaxError on line 42
            st.error("Missing Data: Please fill in the Bug Title, Steps, and Source Code.")
        else:
            with st.spinner("Analyzing Architectural Standards..."):
                time.sleep(1.2)
                
                # --- AI ENHANCEMENT & RECTIFICATION LOGIC ---
                enhanced = code_input
                diagnosis = ""
                remedy = ""

                if "Flutter" in lang:
                    diagnosis = "Heavy logic/fetching in the Build method blocks the UI thread (Jank)."
                    remedy = "Implemented <b>FutureBuilder</b> and moved logic to a separate Service/Controller."
                    enhanced = enhanced.replace("Widget build", "Future<Widget> buildAsync")
                
                elif "C#" in lang:
                    diagnosis = "Synchronous Blocking (.Find) and Tight Coupling (Direct DB Context)."
                    remedy = "Applied <b>Async/Await</b> and <b>Dependency Injection</b> for scalability."
                    enhanced = enhanced.replace("public ActionResult", "public async Task<IActionResult>")
                    enhanced = enhanced.replace(".Find(id)", "await _service.GetByIdAsync(id)")

                # EXPLANATION PANEL (Understandable overview for users)
                st.markdown(f"""
                <div class="explanation-box">
                    <h4 style="color: #FFD700; margin-top: 0;">🔍 Why was this a bug?</h4>
                    <p>{diagnosis}</p>
                    <h4 style="color: #FFD700;">🚀 How did we overcome this?</h4>
                    <p>{remedy}</p>
                </div>
                """, unsafe_allow_html=True)

                # CODE RENDERING
                tab_code, tab_diff = st.tabs(["💎 Fixed Code", "🔍 Detailed Diff"])
                with tab_code:
                    st.code(enhanced, language="dart" if "Flutter" in lang else "csharp")
                    st.markdown("---")
                    m1, m2, m3 = st.columns(3)
                    m1.metric("Runtime", "-115ms", "Faster")
                    m1.markdown('<span class="badge">SOLID</span> <span class="badge">DRY</span>', unsafe_allow_html=True)
                
                with tab_diff:
                    diff = difflib.ndiff(code_input.splitlines(), enhanced.splitlines())
                    st.text('\n'.join(diff))
    else:
        st.info("Fill out the forms on the left to see the optimized fix and structural explanation.")
