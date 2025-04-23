import streamlit as st

st.sidebar.title("📊 Navigation")
page = st.sidebar.radio("Choose a dashboard:", ["Trading Signals", "Fundamentals", "Valuation"])

if page == "Trading Signals":
    import trading_signals
    trading_signals.run()
elif page == "Fundamentals":
    import fundamentals_dashboard
    fundamentals_dashboard.run()
elif page == "Valuation":
    import valuation_tool
    valuation_tool.run()
