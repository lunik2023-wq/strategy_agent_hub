import streamlit as st

st.set_page_config(page_title="Strategy Agent Hub", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;600;700&display=swap');

.stApp { background-color: #F7F6F3; font-family: 'Noto Sans KR', sans-serif; }
.hub-header { padding: 28px 0 28px 0; text-align: center; border-bottom: 1px solid #E0DDD6; margin-bottom: 32px; }
.hub-eyebrow { font-size: 11px; font-weight: 600; letter-spacing: 3px; color: #999; text-transform: uppercase; margin-bottom: 12px; }
.hub-title { font-family: 'Noto Sans KR', sans-serif; font-size: 52px; font-weight: 700; color: #1A1A1A; letter-spacing: -1px; }
.hub-title span { color: #002D62; }
.hub-subtitle { margin-top: 12px; font-size: 15px; color: #888; font-weight: 300; }
.section-label { font-size: 10px; font-weight: 700; letter-spacing: 2.5px; color: #BBB; text-transform: uppercase; margin-bottom: 16px; }
.hub-footer { text-align: center; padding: 24px 0 32px 0; font-size: 11px; color: #BBB; letter-spacing: 1px; }

div[data-testid='stButton'] > button {
    width: 100% !important;
    padding: 18px 20px 18px 28px !important;
    background-color: #FFFFFF !important;
    border: 1.5px solid #C8C4BC !important;
    border-radius: 8px !important;
    color: #1A1A1A !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    font-family: 'Noto Sans KR', sans-serif !important;
    text-align: left !important;
    height: auto !important;
    line-height: 1.7 !important;
    margin-bottom: 0 !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.08) !important;
    justify-content: flex-start !important;
    transition: all 0.15s ease !important;
}
div[data-testid='stButton'] > button:hover {
    background-color: #EEF2F8 !important;
    border-color: #002D62 !important;
    color: #002D62 !important;
    box-shadow: 0 4px 12px rgba(0,45,98,0.14) !important;
}
div[data-testid='stButton'] > button > div,
div[data-testid='stButton'] > button > div > p {
    text-align: left !important;
    width: 100% !important;
    font-family: 'Noto Sans KR', sans-serif !important;
    justify-content: flex-start !important;
}

/* 이동 버튼 - 작고 투명하게 */
div[data-testid='stButton'].move-btn > button {
    padding: 4px 8px !important;
    background-color: transparent !important;
    border: 1px solid #E0DDD6 !important;
    border-radius: 4px !important;
    color: #BBB !important;
    font-size: 12px !important;
    font-weight: 400 !important;
    box-shadow: none !important;
    height: 28px !important;
    min-height: unset !important;
    margin: 0 !important;
}
div[data-testid='stButton'].move-btn > button:hover {
    background-color: #F0EEE9 !important;
    border-color: #999 !important;
    color: #555 !important;
    box-shadow: none !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hub-header">
    <div class="hub-eyebrow">E-Land Eats &middot; Strategic Planning Office</div>
    <div class="hub-title">STRATEGY <span>AGENT</span> HUB</div>
    <div class="hub-subtitle">AI-powered decision intelligence for F&amp;B growth strategy</div>
</div>
""", unsafe_allow_html=True)

@st.dialog("Agent Execution Center")
def run_agent_popup(name, desc):
    st.markdown(f"#### {name}")
    st.caption(desc)
    st.divider()
    st.info(f"**{name}** 에이전트를 초기화하는 중이에요.")
    if st.button("닫기"):
        st.rerun()

if "agents" not in st.session_state:
    st.session_state.agents = [
        ("🎙️", "Vocal Strategy Transcriber", "회의·보고 음성을 전략 문서로 자동 변환"),
        ("📊", "Market Intelligence Analyzer", "시장 데이터 수집 및 경쟁 구도 분석"),
        ("🍴", "F&B Trend Forecasting", "외식 트렌드 감지 및 기회 신호 탐지"),
        ("📈", "Growth Adjacency Mapper", "인접 사업 확장 후보 평가 및 우선순위화"),
        ("📝", "Strategic Report Generator", "분석 결과를 컨설팅 보고서 형식으로 자동 생성"),
        ("🔍", "Brand Diagnostic Agent", "브랜드 핵심 진단 및 잠재력 갭 분석"),
    ]

agents = st.session_state.agents
n = len(agents)

st.markdown('<div class="section-label">Available Agents</div>', unsafe_allow_html=True)

agents = st.session_state.agents
n = len(agents)

col1, col2 = st.columns(2)
for i, (icon, title, desc) in enumerate(agents):
    col = col1 if i % 2 == 0 else col2
    with col:
        if st.button(icon + "  " + title + "\n" + desc, key=f"btn_{i}", use_container_width=True):
            run_agent_popup(title, desc)

st.markdown("---")
st.markdown('<div class="hub-footer">© 2026 Jin-seok · Strategic Planning Office · E-Land Eats</div>', unsafe_allow_html=True)
