import streamlit as st
import pandas as pd
import plotly.express as px

# Configure the page
st.set_page_config(
    page_title="Data Canvas",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with animations and background
st.markdown("""
<style>
    /* Animation Keyframes */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes slideIn {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }

    @keyframes slideInRight {
        from { transform: translateX(20px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    @keyframes gradientFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Background styling */
    .stApp {
        background: linear-gradient(135deg, rgba(15,23,42,0.97), rgba(23,49,77,0.98)), 
                    url('data:image/svg+xml,%3Csvg width="100" height="100" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"%3E%3Cpath d="M11 18c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm48 25c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm-43-7c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm63 31c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM34 90c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm56-76c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM12 86c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm28-65c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm23-11c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-6 60c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm29 22c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zM32 63c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm57-13c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5z" fill="rgba(255,255,255,0.03)" fill-rule="evenodd"/%3E%3C/svg%3E'),
                    linear-gradient(135deg, #0f172a, #17314d);
        background-attachment: fixed;
        background-size: cover, 800px 800px, cover;
        background-position: center;
            font-size: "2rem"
    }
            
            

    /* Glass morphism effects */
    # .glass-container {
    #     background: rgba(255, 255, 255, 0.05);
    #     backdrop-filter: blur(10px);
    #     -webkit-backdrop-filter: blur(10px);
    #     border: 1px solid rgba(255, 255, 255, 0.1);
    #     border-radius: 15px;
    #     padding: 20px;
    #     margin-bottom: 20px;
    #     box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.1);
    # }

    /* Logo and header styling */
    .logo-text {
        font-size: 6rem;
        font-weight: bold;
        background: linear-gradient(45deg, #ffd100, #ff6b6b, #4361ee, #06d6a0);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientFlow 5s ease infinite;
        text-align: center;
    }

    .tagline {
        color: rgba(255,255,255,0.8);
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        animation: fadeIn 1s ease-out;
    }

    /* Search container styling */
  .search-container {
    max-width: 800px;
    margin: auto;
    margin-top:15%;
    padding: 3px;
    
    /* background: linear-gradient(90deg, #ffd100, #ff6b6b, #4361ee, #06d6a0); */
    border-radius: 20px;
    /* animation: gradientFlow 5s ease infinite; */
}

.search-input {
    display: flex;
    # align-items: center;
    background:#334254;
    backdrop-filter: blur(10px);
    border: 3.5px solid transparent;
    border-image: linear-gradient(45deg, red, orange, yellow, green, blue, indigo, violet,red, orange, yellow, green, blue, indigo, violet) 1;
    border-radius: 28px;
    padding: 10px 20px;
}

.search-input input {
    flex: 1;
    background: transparent;
    border: none; /* Removes the border */
    outline: none; /* Removes the outline */
    color: white;
    padding: 10px;
    font-size: 1rem;
}

.search-input input::placeholder {
    color: rgba(255, 255, 255, 0.6);
}

    /* Feature items styling */
    .feature-item {
        text-align: center;
        padding: 20px;
        animation: fadeIn 0.5s ease-out;
    }

    .feature-item .icon {
        font-size: 3rem;
        margin-bottom: 10px;
        animation: float 3s ease-in-out infinite;
    }

    /* Button styling */
    button {
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.1);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        cursor: pointer;
        transition: all 0.3s ease;
            border:"none",
            outline:"none"
    }


    /* Metric styling */
    [data-testid="stMetricValue"] {
        font-size: 1.8rem !important;
        color: white !important;
        text-shadow: 0 0 10px rgba(255,255,255,0.2);
    }

    /* Chart styling */
    .js-plotly-plot {
        background: rgba(255,255,255,0.05) !important;
        border-radius: 15px;
        padding: 20px;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "data" not in st.session_state:
    st.session_state["data"] = None

    
# Inject CSS to increase tab text size
st.markdown(
    """
    <style>
    .st-ar{
    top:105%;
    right:31.5%;
    # left:40%;
    position: absolute;
    }

    button[data-baseweb="tab"] {
        font-size: 50px; /* Adjust font size here */
        padding: 10px 20px; /* Adjust padding for better spacing */
        color: black; /* Text color */
        background-color: #ffffff; /* Background color for the tabs */
        border: none;
        border-radius: 10px;
    }

    /* Highlight the active tab */
    button[data-baseweb="tab"][aria-selected="true"] {
        font-size: 10px; /* Slightly larger font for active tab */
        font-weight: bold;
        # color: white;
        # background-color: #4CAF50; /* Active tab background */
        border: none;
    }

    .st-c6{
    height: 0;
    }
    .st-c7{
    height: 0;
    }

    .st-emotion-cache-bm2z3a {
    overflow: hidden;
    }

    .st-emotion-cache-1jicfl2{
    height:100vh;
    padding: 6rem 6rem 0 6rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Main content
tabs = st.tabs(["🏠 Home", "📤 Upload", "📊 Analysis", "🤖 AI Insights", "🎯 Presentation"])

# Home Tab
with tabs[0]:
    st.markdown('<h1 class="logo-text">Data Canvas</h1>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">Transform Your Data into Dynamic Stories</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="search-container">
        <div class="search-input">
            <input type="text" placeholder="Ask anything about your data...">
            <button>Ask AI</button>
        </div>
    </div>

    """, unsafe_allow_html=True)

# Upload Tab
# with tabs[1]:
#     st.markdown('<div class="glass-container">', unsafe_allow_html=True)
#     st.title("Upload Your Data")
#     uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])
    
#     if uploaded_file:
#         try:
#             if uploaded_file.name.endswith(".csv"):
#                 st.session_state.data = pd.read_csv(uploaded_file)
#             else:
#                 st.session_state.data = pd.read_excel(uploaded_file)
            
#             st.success("✨ File uploaded successfully!")
#             st.markdown("### Preview of your data")
#             st.dataframe(st.session_state.data.head(), use_container_width=True)
            
#             col1, col2, col3 = st.columns(3)
#             with col1:
#                 st.metric("Rows", f"{len(st.session_state.data):,}")
#             with col2:
#                 st.metric("Columns", f"{len(st.session_state.data.columns):,}")
#             with col3:
#                 st.metric("Data Points", f"{st.session_state.data.size:,}")
                
#         except Exception as e:
#             st.error(f"Error: {str(e)}")
#     st.markdown('</div>', unsafe_allow_html=True)

# Analysis Tab
# with tabs[2]:
#     if st.session_state.data is not None:
#         st.markdown('<div class="glass-container">', unsafe_allow_html=True)
#         st.title("Data Analysis")
        
#         st.markdown("### 📊 Summary Statistics")
#         st.dataframe(st.session_state.data.describe(), use_container_width=True)
        
#         st.markdown("### 📈 Data Visualization")
#         col_select, chart_select = st.columns([2, 2])
        
#         with col_select:
#             selected_col = st.selectbox("Select Column", st.session_state.data.columns)
#         with chart_select:
#             chart_type = st.selectbox("Select Chart Type", ["Histogram", "Box Plot", "Bar Chart"])
            
#         if chart_type == "Histogram":
#             fig = px.histogram(st.session_state.data, x=selected_col, 
#                              template="plotly_dark",
#                              color_discrete_sequence=['rgba(67,97,238,0.7)'])
#         elif chart_type == "Box Plot":
#             fig = px.box(st.session_state.data, y=selected_col,
#                         template="plotly_dark",
#                         color_discrete_sequence=['rgba(67,97,238,0.7)'])
#         else:
#             fig = px.bar(st.session_state.data[selected_col].value_counts().reset_index(),
#                         x='index', y=selected_col,
#                         template="plotly_dark",
#                         color_discrete_sequence=['rgba(67,97,238,0.7)'])
            
#         fig.update_layout(
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#             font_color='white'
#         )
#         st.plotly_chart(fig, use_container_width=True)
#         st.markdown('</div>', unsafe_allow_html=True)


# AI Insights Tab
# with tabs[3]:
#     if st.session_state.data is not None:
#         st.markdown('<div class="glass-container">', unsafe_allow_html=True)
#         st.title("🤖 AI Insights")
        
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.markdown("#### Numerical Analysis")
#             num_cols = st.session_state.data.select_dtypes(include=['number']).columns
#             for col in num_cols[:3]:  # Show first 3 columns
#                 st.write(f"{col}")
#                 st.write(f"- Mean: {st.session_state.data[col].mean():.2f}")
#                 st.write(f"- Median: {st.session_state.data[col].median():.2f}")
        
#         with col2:
#             st.markdown("#### Categorical Analysis")
#             cat_cols = st.session_state.data.select_dtypes(exclude=['number']).columns
#             for col in cat_cols[:3]:  # Show first 3 columns
#                 st.write(f"{col}")
#                 st.write(f"- Unique values: {st.session_state.data[col].nunique()}")
#                 st.write(f"- Most common: {st.session_state.data[col].mode().iloc[0]}")
        
#         st.markdown('</div>', unsafe_allow_html=True)


# Presentation Tab
# with tabs[4]:
    if st.session_state.data is not None:
        st.markdown('<div class="glass-container">', unsafe_allow_html=True)
        st.title("🎯 Presentation")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Records", f"{len(st.session_state.data):,}", "+12%")
        with col2:
            st.metric("Data Quality", "98%", "+5%")
        with col3:
            st.metric("Insights Generated", "24", "+8")
            
        st.markdown("### Key Visualizations")
        if len(st.session_state.data.select_dtypes(include=['number']).columns) >= 2:
            num_cols = st.session_state.data.select_dtypes(include=['number']).columns[:2]
            fig = px.scatter(st.session_state.data, x=num_cols[0], y=num_cols[1],
                           template="plotly_dark",
                           color_discrete_sequence=['rgba(67,97,238,0.7)'])
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='white'
            )
            st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="position: fixed; bottom: 0; left: 0; right: 0; background: rgba(255,255,255,0.05); backdrop-filter: blur(10px); padding: 10px; text-align: center; color: rgba(255,255,255,0.7);">
    © 2024 Data Canvas • Powered by AI
</div>
""", unsafe_allow_html=True)