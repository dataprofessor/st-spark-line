import streamlit as st
from numpy.random import default_rng as rng

# Displays app title and description
st.title(":material/show_chart: Show Sparklines")
st.warning("To show trends over time, add sparklines with the `chart_data` parameter.")

# Display toggable code block
with st.expander(":material/code_blocks: See Code"):
    st.code("""
    changes = list(rng(4).standard_normal(20))
    data = [sum(changes[:i]) for i in range(20)]
    delta = round(data[-1], 2)
    
    row = st.container(horizontal=True)
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

row = st.container(horizontal=True)
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

# Display metrics with sparklines (negative trend)
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
