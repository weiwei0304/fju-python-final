import streamlit as st
from resignation_calculator import ResignationCalculator
from quiz import render_quiz_ui, calculate_quiz_score_from_answers


st.markdown(
    """
<style>
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.02);
        }
    }
    
    .stApp {
        background: linear-gradient(135deg, #faf5f0 0%, #f0ebe5 100%);
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Microsoft JhengHei', sans-serif;
        animation: fadeIn 0.6s ease-out;
    }
    
    h1 {
        color: #5d4e37;
        font-weight: 500;
        font-size: 2.2rem;
        letter-spacing: -0.5px;
        margin-bottom: 40px;
        text-align: center;
        animation: fadeIn 0.8s ease-out;
    }
    
    .step-wrapper {
        background-color: #ffffff;
        padding: 45px 35px;
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(93, 78, 55, 0.08);
        margin: 35px auto;
        max-width: 580px;
        border: 1px solid rgba(93, 78, 55, 0.1);
        position: relative;
    }
    
    .step-wrapper::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #d4a574 0%, #c8966a 100%);
        border-radius: 16px 16px 0 0;
    }
    
    .element-container:has(.step-wrapper-header) {
        background-color: #ffffff !important;
        padding: 45px 35px !important;
        border-radius: 16px !important;
        box-shadow: 0 8px 24px rgba(93, 78, 55, 0.08) !important;
        margin: 35px auto !important;
        max-width: 580px !important;
        border: 1px solid rgba(93, 78, 55, 0.1) !important;
        position: relative !important;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .element-container:has(.step-wrapper-header):hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 32px rgba(93, 78, 55, 0.12) !important;
    }
    
    .element-container:has(.step-wrapper-header)::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #d4a574 0%, #c8966a 100%);
        border-radius: 16px 16px 0 0;
    }
    
    .step-wrapper-header {
        text-align: center;
        color: #8b6f47;
        font-size: 1.4rem;
        font-weight: 400;
        font-style: italic;
        margin-bottom: 20px;
        padding-bottom: 18px;
        border-bottom: 1px solid #ede8e1;
        letter-spacing: 1px;
    }
    
    .step-quote {
        text-align: center;
        color: #8b6f47;
        font-size: 1.4rem;
        font-weight: 400;
        font-style: italic;
        margin-bottom: 35px;
        padding-bottom: 25px;
        border-bottom: 1px solid #ede8e1;
        letter-spacing: 1px;
    }
    
    .step-wrapper .stDateInput > div > div {
        background-color: #f8f6f3;
        border: 2px solid #e8ddd0;
        border-radius: 12px;
        padding: 8px;
        transition: all 0.3s ease;
    }
    
    .step-wrapper .stDateInput > div > div:hover {
        border-color: #d4a574;
        background-color: #fffefb;
    }
    
    .step-wrapper .stDateInput label {
        color: #5d4e37;
        font-weight: 500;
        font-size: 1.3rem !important;
        margin-bottom: 8px;
    }
    
    .step-wrapper .stDateInput label p {
        font-size: 1.3rem !important;
    }
    
    .stDateInput > div > div {
        background-color: #f8f6f3;
        border: 2px solid #e8ddd0;
        border-radius: 12px;
        padding: 8px;
    }
    
    .stDateInput label {
        color: #5d4e37;
        font-weight: 500;
        font-size: 1.3rem !important;
    }
    
    .stDateInput label p {
        font-size: 1.3rem !important;
    }
    
    .stDateInput input {
        font-size: 1.05rem;
    }
    
    .element-container:has(.step-wrapper-header) .stDateInput > div > div {
        background-color: #f8f6f3;
        border: 2px solid #e8ddd0;
        border-radius: 12px;
        padding: 8px;
        transition: all 0.3s ease;
    }
    
    .element-container:has(.step-wrapper-header) .stDateInput > div > div:hover {
        border-color: #d4a574;
        background-color: #fffefb;
    }
    
    .element-container:has(.step-wrapper-header) .stDateInput label {
        color: #5d4e37;
        font-weight: 500;
        font-size: 1.3rem !important;
        margin-bottom: 8px;
    }
    
    .element-container:has(.step-wrapper-header) .stDateInput label p {
        font-size: 1.3rem !important;
    }
    
    .element-container:has(.step-wrapper-header) [data-testid="stRadio"] {
        background-color: #faf8f5 !important;
        padding: 30px 40px !important;
        border-radius: 14px !important;
        border: 1px solid #ede8e1 !important;
        margin-bottom: 16px !important;
        width: 100% !important;
        animation: slideUp 0.6s ease-out;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .element-container:has(.step-wrapper-header) [data-testid="stRadio"]:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(237, 232, 225, 0.5);
    }
    
    .element-container:has(.step-wrapper-header) [data-testid="stRadio"] > label[data-testid="stWidgetLabel"] {
        font-size: 1.15rem !important;
        font-weight: 500 !important;
        color: #5d4e37 !important;
        margin-bottom: 14px !important;
        text-align: left !important;
        display: block !important;
    }
    
    .element-container:has(.step-wrapper-header) [data-testid="stRadio"] > label[data-testid="stWidgetLabel"] p {
        font-size: 1.15rem !important;
    }
    
    .element-container:has(.step-wrapper-header) [data-testid="stRadio"] [role="radiogroup"] {
        padding: 10px 0 !important;
        display: flex !important;
        flex-direction: column !important;
    }
    
    .element-container:has(.step-wrapper-header) [data-testid="stRadio"] [role="radiogroup"] label {
        font-size: 1.1rem !important;
    }
    
    .element-container:has(.step-wrapper-header) [data-testid="stRadio"] [role="radiogroup"] label div {
        font-size: 1.1rem !important;
    }
    
    .step-wrapper .stButton {
        margin-top: 28px;
    }
    
    .step-wrapper .stButton > button {
        background: linear-gradient(135deg, #4caf50 0%, #45a049 50%, #3d8b40 100%);
        color: #ffffff;
        border: none;
        border-radius: 10px;
        padding: 14px 32px;
        font-weight: 500;
        font-size: 1.05rem;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(76, 175, 80, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .step-wrapper .stButton > button:hover {
        background: linear-gradient(135deg, #45a049 0%, #3d8b40 50%, #357a38 100%);
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.4);
        transform: translateY(-1px);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #4caf50 0%, #45a049 50%, #3d8b40 100%);
        color: #ffffff;
        border: none;
        border-radius: 10px;
        padding: 14px 32px;
        font-weight: 500;
        font-size: 1.05rem;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(76, 175, 80, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #45a049 0%, #3d8b40 50%, #357a38 100%);
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.4);
        transform: translateY(-2px);
    }
    
    .stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 2px 8px rgba(76, 175, 80, 0.3);
    }
    
    .element-container:has(.step-wrapper-header) .stButton > button {
        background: linear-gradient(135deg, #4caf50 0%, #45a049 50%, #3d8b40 100%);
        color: #ffffff;
        border: none;
        border-radius: 10px;
        padding: 14px 32px;
        font-weight: 500;
        font-size: 1.05rem;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(76, 175, 80, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .element-container:has(.step-wrapper-header) .stButton > button:hover {
        background: linear-gradient(135deg, #45a049 0%, #3d8b40 50%, #357a38 100%);
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.4);
        transform: translateY(-2px);
    }
    
    .element-container:has(.step-wrapper-header) .stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 2px 8px rgba(76, 175, 80, 0.3);
    }
    
    /* Primary 按鈕樣式 */
    .stButton > button[data-testid="stBaseButton-primary"] {
        background: linear-gradient(135deg, #4caf50 0%, #45a049 50%, #3d8b40 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 14px 32px !important;
        font-weight: 500 !important;
        font-size: 1.05rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 8px rgba(76, 175, 80, 0.3) !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .stButton > button[data-testid="stBaseButton-primary"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button[data-testid="stBaseButton-primary"]:hover {
        background: linear-gradient(135deg, #45a049 0%, #3d8b40 50%, #357a38 100%) !important;
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.4) !important;
        transform: translateY(-2px) !important;
    }
    
    .stButton > button[data-testid="stBaseButton-primary"]:hover::before {
        left: 100%;
    }
    
    .stButton > button[data-testid="stBaseButton-primary"]:active {
        transform: translateY(0) !important;
        box-shadow: 0 2px 8px rgba(76, 175, 80, 0.3) !important;
    }
    
    /* Secondary 按鈕樣式 */
    .stButton > button[data-testid="stBaseButton-secondary"] {
        background: linear-gradient(135deg, #dc3545 0%, #c82333 50%, #bd2130 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 14px 32px !important;
        font-weight: 500 !important;
        font-size: 1.05rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 8px rgba(220, 53, 69, 0.3) !important;
        position: relative !important;
        overflow: hidden !important;
    }
    
    .stButton > button[data-testid="stBaseButton-secondary"]::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button[data-testid="stBaseButton-secondary"]:hover {
        background: linear-gradient(135deg, #c82333 0%, #bd2130 50%, #a71e2a 100%) !important;
        box-shadow: 0 4px 12px rgba(220, 53, 69, 0.4) !important;
        transform: translateY(-2px) !important;
    }
    
    .stButton > button[data-testid="stBaseButton-secondary"]:hover::before {
        left: 100%;
    }
    
    .stButton > button[data-testid="stBaseButton-secondary"]:active {
        transform: translateY(0) !important;
        box-shadow: 0 2px 8px rgba(220, 53, 69, 0.3) !important;
    }
    
    .step-wrapper .stSuccess {
        background-color: #f0f7f4;
        border-left: 4px solid #6b9f78;
        color: #2d5a3d;
        border-radius: 8px;
        padding: 20px 24px;
        margin-top: 24px;
        box-shadow: 0 2px 8px rgba(107, 159, 120, 0.1);
    }
    
    .stSuccess {
        background-color: #f0f7f4;
        border-left: 4px solid #6b9f78;
        color: #2d5a3d;
        border-radius: 8px;
        padding: 20px 24px;
        box-shadow: 0 2px 8px rgba(107, 159, 120, 0.1);
    }
    
    .element-container:has(.step-wrapper-header) .stSuccess {
        background-color: #f0f7f4;
        border-left: 4px solid #6b9f78;
        color: #2d5a3d;
        border-radius: 8px;
        padding: 16px 20px;
        margin-top: 16px;
        font-size: 1.05rem;
        box-shadow: 0 2px 8px rgba(107, 159, 120, 0.1);
        animation: slideUp 0.5s ease-out;
    }
    
    .step-wrapper .stError {
        background-color: #fef5f5;
        border-left: 4px solid #d67b7b;
        color: #8b3e3e;
        border-radius: 8px;
        padding: 20px 24px;
        margin-top: 24px;
        box-shadow: 0 2px 8px rgba(214, 123, 123, 0.1);
    }
    
    .stError {
        background-color: #fef5f5;
        border-left: 4px solid #d67b7b;
        color: #8b3e3e;
        border-radius: 8px;
        padding: 20px 24px;
        box-shadow: 0 2px 8px rgba(214, 123, 123, 0.1);
    }
    
    .element-container:has(.step-wrapper-header) .stError {
        background-color: #fef5f5;
        border-left: 4px solid #d67b7b;
        color: #8b3e3e;
        border-radius: 8px;
        padding: 16px 20px;
        margin-top: 16px;
        font-size: 1.05rem;
        box-shadow: 0 2px 8px rgba(214, 123, 123, 0.1);
        animation: slideUp 0.5s ease-out;
    }
    
    .stInfo {
        background-color: #f0f7ff;
        border-left: 4px solid #6b9fcf;
        color: #2d4a5a;
        border-radius: 8px;
        padding: 20px 24px;
        box-shadow: 0 2px 8px rgba(107, 159, 207, 0.1);
    }
    
    .element-container:has(.step-wrapper-header) .stInfo {
        background-color: #f0f7ff;
        border-left: 4px solid #6b9fcf;
        color: #2d4a5a;
        border-radius: 8px;
        padding: 16px 20px;
        margin-top: 16px;
        font-size: 1.05rem;
        box-shadow: 0 2px 8px rgba(107, 159, 207, 0.1);
        animation: slideUp 0.5s ease-out;
    }
    
    .main .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 800px;
        margin: 0 auto;
    }
    
    .stApp {
        font-size: 1.05rem;
    }
    
    .step-wrapper {
        font-size: 1.05rem;
    }
    
    .stDateInput, .stRadio {
        margin-bottom: 0;
    }
    
    .element-container:has(.step-wrapper-header) [data-testid="column"]:has([data-testid="stRadio"]) {
        width: 90% !important;
        max-width: 550px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    .element-container:has(.step-wrapper-header) [data-testid="column"]:has([data-testid="stRadio"]) > div {
        align-items: center !important;
        justify-content: center !important;
    }
    
    .st-emotion-cache-wfksaw:has([data-testid="stRadio"]) {
        align-items: center !important;
        justify-content: center !important;
    }
    
    [data-testid="stRadio"] {
        background-color: #faf8f5 !important;
        padding: 30px 40px !important;
        border-radius: 14px !important;
        border: 1px solid #ede8e1 !important;
        margin-bottom: 16px !important;
        width: 100% !important;
    }
    
    [data-testid="stRadio"] > label[data-testid="stWidgetLabel"] {
        font-size: 1.15rem !important;
        font-weight: 500 !important;
        color: #5d4e37 !important;
        margin-bottom: 14px !important;
        text-align: left !important;
        display: block !important;
    }
    
    [data-testid="stRadio"] > label[data-testid="stWidgetLabel"] p {
        font-size: 1.15rem !important;
    }
    
    [data-testid="stRadio"] [role="radiogroup"] {
        display: flex !important;
        flex-direction: column !important;
    }
    
    [data-testid="stRadio"] [role="radiogroup"] label {
        font-size: 1.1rem !important;
    }
    
    [data-testid="stRadio"] [role="radiogroup"] label div p {
        font-size: 1.1rem !important;
    }
    
    @media (max-width: 640px) {
        .step-wrapper [data-testid="column"] {
            width: 100% !important;
            flex: 1 1 100% !important;
            min-width: 100% !important;
        }
        
        .element-container:has(.step-wrapper-header) [data-testid="column"] {
            width: 100% !important;
            flex: 1 1 100% !important;
            min-width: 100% !important;
        }
    }
    
    .st-key-help_icon,
    [data-testid="stElementContainer"].st-key-help_icon {
        position: fixed !important;
        bottom: 60px !important;
        right: 20px !important;
        z-index: 1000 !important;
        width: 50px !important;
        height: 50px !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    .st-key-help_icon .stButton {
        width: 50px !important;
        height: 50px !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    .st-key-help_icon button {
        width: 50px !important;
        height: 50px !important;
        min-width: 50px !important;
        max-width: 50px !important;
        background: linear-gradient(135deg, #4caf50 0%, #45a049 50%, #3d8b40 100%) !important;
        color: white !important;
        border-radius: 50% !important;
        border: none !important;
        font-size: 24px !important;
        font-weight: bold !important;
        cursor: pointer !important;
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3) !important;
        transition: all 0.3s ease !important;
        padding: 0 !important;
        margin: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    .st-key-help_icon button:hover {
        background: linear-gradient(135deg, #45a049 0%, #3d8b40 50%, #357a38 100%) !important;
        transform: scale(1.1) !important;
        box-shadow: 0 6px 16px rgba(76, 175, 80, 0.4) !important;
    }
    
    .st-key-help_icon button:active {
        transform: scale(0.95) !important;
    }
    
    /* 說明彈窗 */
    .help-popup {
        position: fixed;
        bottom: 80px;
        right: 20px;
        background-color: #ffffff;
        border: 2px solid #8b6f47;
        border-radius: 12px;
        padding: 24px;
        box-shadow: 0 8px 24px rgba(93, 78, 55, 0.2);
        z-index: 1001;
        max-width: 350px;
        animation: slideUp 0.3s ease-out;
    }
    
    .help-popup h3 {
        color: #5d4e37;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 16px;
        margin-top: 0;
    }
    
    .help-popup ul {
        color: #5d4e37;
        font-size: 1rem;
        line-height: 1.8;
        margin: 0;
        padding-left: 20px;
    }
    
    .help-popup li {
        margin-bottom: 8px;
    }
    
    .help-popup .close-btn {
        position: absolute;
        top: 10px;
        right: 10px;
        background: none;
        border: none;
        font-size: 20px;
        cursor: pointer;
        color: #8b6f47;
        padding: 4px 8px;
        border-radius: 4px;
        transition: background-color 0.2s;
    }
    
    .help-popup .close-btn:hover {
        background-color: #f0ebe5;
    }
    
</style>
""",
    unsafe_allow_html=True,
)


if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.quiz_score = 0
    st.session_state.quiz_completed = False
    st.session_state.start_date = None
    st.session_state.has_quit_date = None
    st.session_state.quit_date = None
    st.session_state.show_help = False
    st.session_state.quiz_validation_error = False

def load_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

if st.session_state.step == 0:
    st.title("我該離職嗎？")
    
    with st.container():
        st.markdown(
            '<div class="step-wrapper-header">先了解自己的狀態</div>',
            unsafe_allow_html=True,
        )
        
        q1, q2, q3 = render_quiz_ui()
        
        st.markdown("---")
        
        all_answered = q1 is not None and q2 is not None and q3 is not None
        
        # 提示
        if not all_answered or st.session_state.quiz_validation_error:
            st.error("⚠️ 請回答所有問題後才能完成測驗")
            st.session_state.quiz_validation_error = False  # 重置錯誤狀態
        
        # 提交按鈕
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("完成測驗", key="submit_quiz", use_container_width=True):
                # 驗證是否所有問題都已回答
                if all_answered:
                    st.session_state.quiz_score = calculate_quiz_score_from_answers(q1, q2, q3)
                    st.session_state.quiz_completed = True
                    st.session_state.quiz_validation_error = False
                    st.session_state.step = 1
                    st.rerun()
                else:
                    
                    st.session_state.quiz_validation_error = True
                    st.rerun()

elif st.session_state.step == 1:
    st.title("測驗結果")
    
    with st.container():
        st.markdown(
            '<div class="step-wrapper-header">了解自己的狀態</div>',
            unsafe_allow_html=True,
        )
        
        if st.session_state.quiz_score >= 2:
            st.markdown("### 別再撐了，離職吧！")
            result_text = load_text_file('quitYourJob.txt')
            result_text_html = result_text.replace('\n', '<br>')
            st.markdown(
                f'<div style="background-color: #f0f7f4; border-left: 4px solid #6b9f78; color: #2d5a3d; border-radius: 8px; padding: 20px 24px; margin-top: 16px; font-size: 1.05rem; line-height: 1.8;">{result_text_html}</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown("### 你正在遭遇轉型瓶頸，或許可以再多考慮一下～")
            result_text = load_text_file('betterToStay.txt')
            result_text_html = result_text.replace('\n', '<br>')
            st.markdown(
                f'<div style="background-color: #f0f7ff; border-left: 4px solid #6b9fcf; color: #2d4a5a; border-radius: 8px; padding: 20px 24px; margin-top: 16px; font-size: 1.05rem; line-height: 1.8;">{result_text_html}</div>',
                unsafe_allow_html=True
            )
        
        st.markdown("---")
        st.markdown("### 接下來，讓我們幫你計算離職日期")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("開始計算離職日期", key="go_to_calculator", use_container_width=True, type="primary"):
                st.session_state.step = 2
                st.rerun()
        with col2:
            if st.button("重新測驗", key="retake_quiz", use_container_width=True, type="secondary"):
                st.session_state.step = 0
                st.session_state.quiz_completed = False
                if "quiz_q1_radio" in st.session_state:
                    del st.session_state.quiz_q1_radio
                if "quiz_q2_radio" in st.session_state:
                    del st.session_state.quiz_q2_radio
                if "quiz_q3_radio" in st.session_state:
                    del st.session_state.quiz_q3_radio
                st.rerun()

elif st.session_state.step == 2:
    st.title("轉身日曆")
    
    with st.container():
        st.markdown(
            '<div class="step-wrapper-header">把自己還給自己</div>',
            unsafe_allow_html=True,
        )
        start_date = st.date_input("請選擇目前工作到職日", value=None)

    if start_date:
        st.session_state.start_date = start_date
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    st.title("轉身日曆")
    
    with st.container():
        st.markdown(
            '<div class="step-wrapper-header">把自己還給自己</div>',
            unsafe_allow_html=True,
        )

        col_left, col_center, col_right = st.columns([0.5, 9, 0.5])
        with col_center:
            has_quit_date = st.radio(
                "是否有確定離職日期?",
                options=["是", "否"],
                index=(
                    0
                    if st.session_state.has_quit_date == "是"
                    else 1 if st.session_state.has_quit_date == "否" else None
                ),
            )

        if has_quit_date == "否":
            from datetime import date

            calculator = ResignationCalculator()
            effective_date = calculator.calculate_earliest_effective_date(
                st.session_state.start_date
            )

            if st.session_state.start_date > date.today():
                st.success(
                    f"**到職日**：{st.session_state.start_date.strftime('%Y-%m-%d')}"
                )
                st.info(
                    f"您的到職日尚未到來，到職後即可提出離職（預告期為 0 天）"
                )
            else:
                # 計算預告天數
                work_months = calculator._calculate_work_months(st.session_state.start_date)
                notice_days = calculator._get_notice_days(work_months)
                
                st.success(
                    f"**到職日**：{st.session_state.start_date.strftime('%Y-%m-%d')}"
                )
                
                # 建議提辭呈時間區塊
                st.info(
                    f"**預告天數**：{notice_days} 天  \n"
                    f"**建議提辭呈時間**：{effective_date.strftime('%Y-%m-%d')}前"
                )

            # 三個按鈕：重返測驗、重計日期、結束視窗
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                if st.button("重返測驗", key="back_to_quiz_1", use_container_width=True, type="primary"):
                    st.session_state.step = 0
                    st.session_state.quiz_completed = False
                    st.session_state.start_date = None
                    st.session_state.has_quit_date = None
                    st.session_state.quit_date = None
                    # 清除問卷相關的 session_state
                    if "quiz_q1_radio" in st.session_state:
                        del st.session_state.quiz_q1_radio
                    if "quiz_q2_radio" in st.session_state:
                        del st.session_state.quiz_q2_radio
                    if "quiz_q3_radio" in st.session_state:
                        del st.session_state.quiz_q3_radio
                    st.rerun()
            with col2:
                if st.button("重計日期", key="recalculate_date_1", use_container_width=True, type="primary"):
                    st.session_state.step = 2
                    st.session_state.start_date = None
                    st.session_state.has_quit_date = None
                    st.session_state.quit_date = None
                    st.rerun()
                with col3:
                    if st.button("結束視窗", key="end_1", use_container_width=True, type="secondary"):
                        st.session_state.step = 4
                        st.rerun()

        elif has_quit_date == "是":
            quit_date = st.date_input("請選擇離職日", value=None)

            if quit_date:
                calculator = ResignationCalculator()
                result = calculator.calculate_resignation_details(
                    st.session_state.start_date, quit_date
                )

                if result["countdown"] > 0:
                    st.success(
                        f"**到職日**：{st.session_state.start_date.strftime('%Y-%m-%d')}  \n"
                        f"**目標離職日**：{result['quit_date'].strftime('%Y-%m-%d')}  \n"
                        f"**自由日倒數**：{result['countdown']} 天"
                    )
                    
                    # 建議提辭呈時間區塊
                    st.info(
                        f"**預告天數**：{result['notice_days']} 天  \n"
                        f"**建議提辭呈時間**：{result['notice_date'].strftime('%Y-%m-%d')}前"
                    )

                    animation_key = (
                        f"animation_{st.session_state.start_date}_{quit_date}"
                    )
                    if animation_key not in st.session_state:
                        st.session_state[animation_key] = True
                        if result["countdown"] <= 30:
                            st.balloons()
                        elif result["countdown"] <= 60:
                            st.snow()

                else:
                    st.error("已經超過今日日期，請重新選擇離職日期")

                # 三個按鈕：重返測驗、重計日期、結束視窗
                col1, col2, col3 = st.columns([1, 1, 1])
                with col1:
                    if st.button("重返測驗", key="back_to_quiz_2", use_container_width=True, type="primary"):
                        st.session_state.step = 0
                        st.session_state.quiz_completed = False
                        st.session_state.start_date = None
                        st.session_state.has_quit_date = None
                        st.session_state.quit_date = None
                        # 清除問卷相關的 session_state
                        if "quiz_q1_radio" in st.session_state:
                            del st.session_state.quiz_q1_radio
                        if "quiz_q2_radio" in st.session_state:
                            del st.session_state.quiz_q2_radio
                        if "quiz_q3_radio" in st.session_state:
                            del st.session_state.quiz_q3_radio
                        st.rerun()
                with col2:
                    if st.button("重計日期", key="recalculate_date_2", use_container_width=True, type="primary"):
                        st.session_state.step = 2
                        st.session_state.start_date = None
                        st.session_state.has_quit_date = None
                        st.session_state.quit_date = None
                        st.rerun()
                with col3:
                    if st.button("結束視窗", key="end_2", use_container_width=True, type="secondary"):
                        st.session_state.step = 4
                        st.rerun()

# 結束視窗頁面 (step 4)
elif st.session_state.step == 4:
    st.title("")
    
    with st.container():
        st.markdown(
            '<div class="step-wrapper-header">感謝使用</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div style="text-align: center; padding: 80px 20px; font-size: 3rem; color: #5d4e37; font-weight: 300; letter-spacing: 4px; line-height: 1.5;">
                To be continued...
            </div>
            """,
            unsafe_allow_html=True
        )
        
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("返回", key="back_from_end", use_container_width=True, type="primary"):
                st.session_state.step = 3
                st.rerun()


if st.session_state.step != 4:
    help_clicked = st.button("!", key="help_icon", help="點擊查看通知天數說明")

    if help_clicked:
        st.session_state.show_help = not st.session_state.get("show_help", False)

    if st.session_state.get("show_help", False):
        st.markdown(
            """
        <div class="help-popup" style="display: block;">
            <h3>預告天數說明</h3>
            <ul>
                <li><strong>工作未滿 3 個月</strong>：無需預告（0 天）</li>
                <li><strong>工作 3 個月以上，未滿 1 年</strong>：需提前 10 天預告</li>
                <li><strong>工作 1 年以上，未滿 3 年</strong>：需提前 20 天預告</li>
                <li><strong>工作 3 年以上</strong>：需提前 30 天預告</li>
            </ul>
        </div>
        """,
            unsafe_allow_html=True,
        )
