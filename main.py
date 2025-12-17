import streamlit as st
from resignation_calculator import ResignationCalculator


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
        background-color: #8b6f47;
        color: #ffffff;
        border: none;
        border-radius: 10px;
        padding: 14px 32px;
        font-weight: 500;
        font-size: 1.05rem;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(139, 111, 71, 0.2);
    }
    
    .step-wrapper .stButton > button:hover {
        background-color: #7a5f3a;
        box-shadow: 0 4px 12px rgba(139, 111, 71, 0.3);
        transform: translateY(-1px);
    }
    
    .stButton > button {
        background-color: #8b6f47;
        color: #ffffff;
        border: none;
        border-radius: 10px;
        padding: 14px 32px;
        font-weight: 500;
        font-size: 1.05rem;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(139, 111, 71, 0.2);
    }
    
    .stButton > button:hover {
        background-color: #7a5f3a;
        box-shadow: 0 4px 12px rgba(139, 111, 71, 0.3);
        transform: translateY(-2px);
    }
    
    .stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 2px 8px rgba(139, 111, 71, 0.2);
    }
    
    .element-container:has(.step-wrapper-header) .stButton > button {
        background-color: #8b6f47;
        color: #ffffff;
        border: none;
        border-radius: 10px;
        padding: 14px 32px;
        font-weight: 500;
        font-size: 1.05rem;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(139, 111, 71, 0.2);
    }
    
    .element-container:has(.step-wrapper-header) .stButton > button:hover {
        background-color: #7a5f3a;
        box-shadow: 0 4px 12px rgba(139, 111, 71, 0.3);
        transform: translateY(-2px);
    }
    
    .element-container:has(.step-wrapper-header) .stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 2px 8px rgba(139, 111, 71, 0.2);
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
        background-color: #8b6f47 !important;
        color: white !important;
        border-radius: 50% !important;
        border: none !important;
        font-size: 24px !important;
        font-weight: bold !important;
        cursor: pointer !important;
        box-shadow: 0 4px 12px rgba(139, 111, 71, 0.3) !important;
        transition: all 0.3s ease !important;
        padding: 0 !important;
        margin: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    .st-key-help_icon button:hover {
        background-color: #7a5f3a !important;
        transform: scale(1.1) !important;
        box-shadow: 0 6px 16px rgba(139, 111, 71, 0.4) !important;
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
    st.session_state.step = 1
    st.session_state.start_date = None
    st.session_state.has_quit_date = None
    st.session_state.quit_date = None
    st.session_state.show_help = False

st.title("轉身日曆")

if st.session_state.step == 1:
    with st.container():
        st.markdown(
            '<div class="step-wrapper-header">把自己還給自己</div>',
            unsafe_allow_html=True,
        )
        start_date = st.date_input("請選擇到職日", value=None)

    if start_date:
        st.session_state.start_date = start_date
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
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
                st.info(
                    f"您的到職日 {st.session_state.start_date.strftime('%Y-%m-%d')} 尚未到來，到職後即可提出離職（預告期為 0 天）"
                )
            else:
                st.success(
                    f"最早可以提離職的時間是: {effective_date.strftime('%Y-%m-%d')}"
                )

            col1, col2, col3 = st.columns([1, 1, 1])
            with col2:
                if st.button("上一步", key="back_1", use_container_width=True):
                    st.session_state.step = 1
                    st.session_state.start_date = None
                    st.session_state.has_quit_date = None
                    st.session_state.quit_date = None
                    st.rerun()

        elif has_quit_date == "是":
            quit_date = st.date_input("請選擇到離職日", value=None)

            if quit_date:
                calculator = ResignationCalculator()
                result = calculator.calculate_resignation_details(
                    st.session_state.start_date, quit_date
                )

                if result["countdown"] > 0:
                    st.success(
                        f"**到職日**：{st.session_state.start_date.strftime('%Y-%m-%d')}  \n"
                        f"**確定離職日**：{result['quit_date'].strftime('%Y-%m-%d')}  \n"
                        f"**預告天數**：{result['notice_days']} 天  \n"
                        f"**倒數天數**：{result['countdown']} 天"
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

                col1, col2, col3 = st.columns([1, 1, 1])
                with col2:
                    if st.button("上一步", key="back_2", use_container_width=True):
                        st.session_state.step = 1
                        st.session_state.start_date = None
                        st.session_state.has_quit_date = None
                        st.session_state.quit_date = None
                        st.rerun()

# 右下角驚嘆號按鈕 - 放在所有內容之後
help_clicked = st.button("!", key="help_icon", help="點擊查看通知天數說明")

# 切換顯示說明
if help_clicked:
    st.session_state.show_help = not st.session_state.get("show_help", False)

# 顯示說明彈窗
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
