import streamlit as st
from numpy.random import default_rng as rng

st.set_page_config(
    page_title="Show Sparklines",
    page_icon=":material/show_chart:",
    layout="wide")

# Displays app title and description
st.title(":material/show_chart: Show Sparklines")
st.warning("To show trends over time, add sparklines with the `chart_data` parameter for `st.metric()`.")

# Display toggable code block
with st.expander(":material/code_blocks: See Code"):
    st.code("""
    changes = list(rng(4).standard_normal(20))
    data = [sum(changes[:i]) for i in range(20)]
    delta = round(data[-1], 2)
    
    row = st.container(horizontal_alignment="distributed")
    with row:
        st.metric(
            "Line", 10, delta, chart_data=data, chart_type="line", border=True
        )
        st.metric(
            "Area", 10, delta, chart_data=data, chart_type="area", border=True
        )
        st.metric(
            "Bar", 10, delta, chart_data=data, chart_type="bar", border=True
        )
    
    changes2 = list(-rng(4).standard_normal(20))
    data2 = [sum(changes2[:i]) for i in range(20)]
    delta2 = round(data2[-1], 2)
    
    row2 = st.container(horizontal=True)
    with row2:
        st.metric(
            "Line", 20, delta2, chart_data=data2, chart_type="line", border=True
        )
        st.metric(
            "Area", 20, delta2, chart_data=data2, chart_type="area", border=True
        )
        st.metric(
            "Bar", 20, delta2, chart_data=data2, chart_type="bar", border=True
        )
    """)

# Display metrics with sparklines (positive trend)
changes = list(rng(4).standard_normal(20))
data = [sum(changes[:i]) for i in range(20)]
delta = round(data[-1], 2)

# Display metrics with sparklines (negative trend)
changes2 = list(-rng(4).standard_normal(20))
data2 = [sum(changes2[:i]) for i in range(20)]
delta2 = round(data2[-1], 2)

# Define the chart types in a simple list
chart_types = ["line", "area", "bar"]

# Display metrics with sparklines
# Row 1
row1 = st.columns(3)

for col, chart_type in zip(row1, chart_types):
    with col:
        st.metric(
            label=chart_type.capitalize(), # Create the label from the string
            value=10,
            delta=delta,
            chart_data=data,
            chart_type=chart_type,
            border=True,
        )

# Row 2
row2 = st.columns(3)

for col, chart_type in zip(row2, chart_types):
    with col:
        st.metric(
            label=chart_type.capitalize(), # Create the label from the string
            value=20,
            delta=delta2,
            chart_data=data2,
            chart_type=chart_type,
            border=True,
        )
