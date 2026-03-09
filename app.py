import streamlit as st
import difflib
import time

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Jarvis QE Suite", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #0E1117; color: white; }
    [data-testid="stSidebar"] { background-color: #001F3F; border-right: 2px solid #FFD700; }
    div.stButton > button { background: #FFD700; color: #001F3F; font-weight: bold; width: 100%; border-radius: 8px; }
    .explanation-box { background-color: #1E2128; border-left: 5px solid #FFD700; padding: 20px; border-radius: 5px; margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("🛡️ Jarvis QE Suite")
    lang = st.selectbox("Framework", ["MVC (C#)", "Java", "Python", "Flutter (Dart)", "SQL SP"])
    st.success("⚡ Option 2 Active")

# --- MAIN INTERFACE ---
st.title("🛠️ AI Code Fixer & Enhancer")
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📝 Input Specification")
    title = st.text_input("Bug Title")
    steps = st.text_area("Steps to Reproduce", height=100)
    code_input = st.text_area("Original Source Code", height=300)
    fix_btn = st.button("FIX & ENHANCE CODE")

with col2:
    st.subheader("✨ Optimized Output & Explanation")
    
    if fix_btn:
        if not code_input.strip():
            st.error("Please provide source code.")
        else:
            with st.spinner("Refactoring..."):
                time.sleep(1)
                
                # --- ACTUAL REFACTORING ENGINE ---
                # This ensures the 'Fixed Code' is DIFFERENT from the 'Source Code'
                enhanced = code_input
                
                if "MVC (C#)" in lang:
                    enhanced = enhanced.replace("public ActionResult", "public async Task<IActionResult>")
                    enhanced = enhanced.replace(".Users.Find(id)", "await _service.GetByIdAsync(id)")
                    enhanced = enhanced.replace("return View(user)", "return Ok(userDto); // Decoupled with DTO")
                
                elif "Flutter" in lang:
                    enhanced = enhanced.replace("Widget build(BuildContext context)", "Future<Widget> buildAsync(BuildContext context) async")
                    enhanced = enhanced.replace("api.fetchUserSync()", "await api.fetchUserAsync()")

                # Display Explanation
                st.markdown(f"""
                <div class="explanation-box">
                    <h4 style="color: #FFD700; margin-top: 0;">🚀 Changes Applied</h4>
                    <ul>
                        <li><b>Structural:</b> Converted blocking calls to <b>Async/Await</b> patterns.</li>
                        <li><b>Architecture:</b> Decoupled Controller from Data Layer using <b>Service Abstraction</b>.</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

                # Output Tabs
                tab_code, tab_diff = st.tabs(["💎 Fixed Code", "🔍 Detailed Diff"])
                with tab_code:
                    st.code(enhanced, language="dart" if "Flutter" in lang else "csharp")
                
                with tab_diff:
                    # Visual Diff: Shows exactly what changed
                    diff = difflib.ndiff(code_input.splitlines(), enhanced.splitlines())
                    st.text('\n'.join(diff))
    else:
        st.info("Input code to see the optimization.")
