import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Zomato Bangalore Market Intelligence",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ Zomato Bangalore Restaurant & Market Intelligence")
st.markdown("Interactive analytics dashboard for market analysis, customer preferences, and site selection.")

# Load cleaned dataset
@st.cache_data
def load_data():
    return pd.read_csv('zomato_cleaned.csv')

df = load_data()

# Sidebar filters
st.sidebar.header("Filter Options")

locations = sorted(df['location'].dropna().unique().tolist())
selected_locations = st.sidebar.multiselect(
    "Select Localities:",
    options=locations,
    default=['Koramangala 5th Block', 'Indiranagar', 'BTM', 'HSR']
)

dining_types = sorted(df['dining_type'].dropna().unique().tolist())
selected_dining = st.sidebar.multiselect(
    "Select Dining Format:",
    options=dining_types,
    default=dining_types
)

min_cost = int(df['cost_two'].min())
max_cost = int(df['cost_two'].max())
selected_cost = st.sidebar.slider(
    "Budget for Two (INR):",
    min_value=min_cost,
    max_value=max_cost,
    value=(min_cost, 2500),
    step=50
)

min_rating = st.sidebar.slider("Minimum Rating:", 1.0, 5.0, 3.8, 0.1)

# Apply filters
filtered_df = df[
    (df['location'].isin(selected_locations)) &
    (df['dining_type'].isin(selected_dining)) &
    (df['cost_two'] >= selected_cost[0]) &
    (df['cost_two'] <= selected_cost[1]) &
    (df['rate'] >= min_rating)
]

# Top KPI metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Restaurants Found", f"{len(filtered_df):,}")
col2.metric("Average Rating", f"{filtered_df['rate'].mean():.2f} / 5.0" if len(filtered_df) > 0 else "N/A")
col3.metric("Avg Cost for Two", f"₹{filtered_df['cost_two'].mean():.0f}" if len(filtered_df) > 0 else "N/A")
col4.metric("Avg Review Count", f"{filtered_df['votes'].mean():.0f}" if len(filtered_df) > 0 else "N/A")

st.markdown("---")

# Visualizations
c1, c2 = st.columns(2)

with c1:
    st.subheader("Top Locations by Outlet Count")
    loc_counts = filtered_df['location'].value_counts().head(10).reset_index()
    loc_counts.columns = ['Location', 'Count']
    fig_loc = px.bar(
        loc_counts,
        x='Count',
        y='Location',
        orientation='h',
        color='Count',
        color_continuous_scale='Blues'
    )
    fig_loc.update_layout(yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig_loc, use_container_width=True)

with c2:
    st.subheader("Cost for Two vs. Customer Rating")
    fig_scatter = px.scatter(
        filtered_df,
        x='cost_two',
        y='rate',
        color='dining_type',
        hover_data=['name', 'location'],
        labels={'cost_two': 'Cost for Two (INR)', 'rate': 'Rating'}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

# Recommendation table
st.subheader("Top Recommended Outlets")
table_cols = ['name', 'location', 'rate', 'cost_two', 'dining_type', 'votes', 'cuisines']
st.dataframe(
    filtered_df[table_cols].sort_values(by=['rate', 'votes'], ascending=[False, False]).head(50),
    use_container_width=True
)
