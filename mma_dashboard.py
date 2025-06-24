import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="MMA Intelligence Dashboard", layout="wide")

np.random.seed(42)

fighters = pd.DataFrame({
    'Name': ['Jack Miller', 'Carlos Vega', 'Darren Ho', 'Ali Rami', 'Sasha Petrov'],
    'Wins': np.random.randint(3, 12, 5),
    'Losses': np.random.randint(0, 4, 5),
    'IG Followers': np.random.randint(10000, 50000, 5),
    'Engagement Rate (%)': np.random.uniform(2.1, 9.5, 5),
    'Sentiment Score': np.random.uniform(-1, 1, 5)
})

fighters['Win %'] = (fighters['Wins'] / (fighters['Wins'] + fighters['Losses'])) * 100

events = pd.DataFrame({
    'Event': ['LFA 186', 'Fury FC 79', 'CFFC 129'],
    'Views': [52000, 48000, 56000],
    'Shares': [1100, 890, 1320],
    'Avg Sentiment': [0.35, 0.15, 0.50],
    'Top Fighter': ['Jack Miller', 'Ali Rami', 'Sasha Petrov']
})

st.title("🥊 MMA Intelligence Dashboard")

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Top Fighters")
    fig1 = px.bar(fighters, x='Name', y='IG Followers', color='Sentiment Score', 
                  color_continuous_scale='RdYlGn', title="Follower Count vs Sentiment")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Fighter Performance")
    fig2 = px.scatter(fighters, x='Engagement Rate (%)', y='Win %', color='Name', 
                     size='IG Followers', hover_name='Name', title="Performance vs Fan Engagement")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

st.subheader("📈 Event Metrics")
fig3 = px.bar(events, x='Event', y='Views', text='Top Fighter', title="Event Reach by Views")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("📊 Fan Sentiment Breakdown")
st.dataframe(events[['Event', 'Avg Sentiment', 'Top Fighter']])

st.markdown("---")

st.subheader("🔎 Growth Strategy Insights")
st.markdown("""
- **Push Jack Miller**: High engagement + top sentiment. Ideal for hero campaign.
- **Focus on Instagram reels for Sasha Petrov**: High growth fighter with a striking-heavy style.
- **Ali Rami**: Sentiment is low. Create redemption arc content or post more training lifestyle to humanize him.
- **Fury FC** needs share-optimized highlight clips — underperforming despite decent fights.
""")

st.markdown("---")

st.caption("Prototype by MMA Intelligence Systems — 'Combat data, reimagined.'")
