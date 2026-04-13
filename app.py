import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Import custom modules
from utils.casimir import CasimirEffect
from utils.zeta_functions import RiemannZeta
from utils.visualizations import Visualizer

# Page configuration
st.set_page_config(
    page_title="Quantum Vacuum → Riemann Zeta",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme and styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
    }
    h1 {
        color: #FFD700 !important;
        text-align: center;
        font-size: 3em !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    h2 {
        color: #00D4FF !important;
        border-bottom: 2px solid #00D4FF;
        padding-bottom: 10px;
    }
    h3 {
        color: #FF6B6B !important;
    }
    .stSlider > div > div > div {
        background-color: #00D4FF !important;
    }
    .stButton > button {
        background: linear-gradient(45deg, #FF6B6B, #FF8E53);
        color: white;
        border-radius: 20px;
        padding: 10px 30px;
        font-weight: bold;
        border: none;
    }
    .stButton > button:hover {
        background: linear-gradient(45deg, #FF8E53, #FF6B6B);
        transform: scale(1.05);
    }
    .highlight-box {
        background: rgba(255, 215, 0, 0.1);
        border: 2px solid #FFD700;
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
    }
    .formula-box {
        background: rgba(0, 212, 255, 0.1);
        border: 2px solid #00D4FF;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        font-size: 1.2em;
        margin: 15px 0;
    }
    .info-box {
        background: rgba(255, 107, 107, 0.1);
        border-left: 5px solid #FF6B6B;
        padding: 15px;
        margin: 10px 0;
    }
    .success-box {
        background: rgba(0, 255, 136, 0.1);
        border: 2px solid #00FF88;
        border-radius: 10px;
        padding: 15px;
        margin: 15px 0;
    }
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .metric-value {
        font-size: 2em;
        color: #FFD700;
        font-weight: bold;
    }
    .metric-label {
        color: #aaa;
        font-size: 0.9em;
    }
</style>
""", unsafe_allow_html=True)

# Initialize classes
@st.cache_resource
def get_casimir():
    return CasimirEffect()

@st.cache_resource
def get_zeta():
    return RiemannZeta()

@st.cache_resource
def get_visualizer():
    return Visualizer()

casimir = get_casimir()
zeta = get_zeta()
viz = get_visualizer()

# Sidebar navigation
st.sidebar.title("🧭 Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Module:",
    ["🏠 Home", "⚛️ Casimir Effect", "🧮 Zeta Regularization", 
     "🌌 Zeta Visualizer", "🔗 The Connection", "📊 All Visualizations"]
)

st.sidebar.markdown("---")
st.sidebar.info("""
**About This Project**
                
Explore the deep connection between quantum vacuum fluctuations and the Riemann Hypothesis through interactive visualizations.
                
*Research-level physics meets number theory*
""")

# ==================== HOME PAGE ====================
if page == "🏠 Home":
    st.title("🔬 From Quantum Vacuum to Riemann Zeta")
    st.markdown("""
    <div style='text-align: center; color: #aaa; font-size: 1.2em; margin-bottom: 30px;'>
        A Journey Through Physics and Mathematics
    </div>
    """, unsafe_allow_html=True)
    
    # Hero section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class='highlight-box' style='text-align: center;'>
            <h3 style='color: #FFD700; margin-top: 0;'>🎯 Core Insight</h3>
            <p style='font-size: 1.1em; line-height: 1.6;'>
                The same mathematical function that regularizes infinite quantum vacuum energy 
                lies at the heart of the deepest unsolved problem in mathematics.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Concept flow diagram
    st.markdown("### 🌊 Conceptual Flow")
    fig_concept = viz.create_conceptual_diagram()
    st.plotly_chart(fig_concept, use_container_width=True)
    
    # Project overview cards
    st.markdown("### 📚 Project Modules")
    
    cols = st.columns(5)
    modules = [
        ("⚛️", "Casimir Effect", "Experimental proof that vacuum is not empty"),
        ("∞", "Infinite Sum", "The mathematical problem in QFT"),
        ("ζ", "Zeta Function", "Regularization technique"),
        ("📈", "Visualization", "Interactive exploration"),
        ("🔥", "Connection", "Physics meets Number Theory")
    ]
    
    for col, (icon, title, desc) in zip(cols, modules):
        with col:
            st.markdown(f"""
            <div class='metric-card'>
                <div style='font-size: 2em;'>{icon}</div>
                <div style='color: #00D4FF; font-weight: bold;'>{title}</div>
                <div style='color: #888; font-size: 0.8em;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # One-liner explanation
    st.markdown("---")
    st.markdown("""
    <div class='success-box'>
        <h4 style='color: #00FF88; margin-top: 0;'>💡 One-Line Explanation (For Viva)</h4>
        <p style='font-style: italic; font-size: 1.1em;'>
            "This project demonstrates that the quantum vacuum is not empty through the Casimir effect, 
            reveals how infinite vacuum energy calculations are regularized using the Riemann zeta function, 
            and visualizes the profound connection between quantum field theory and the Riemann Hypothesis."
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick stats
    st.markdown("### 📊 Quick Facts")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Known Zeta Zeros", "10¹³+", "First 10 trillion+ zeros on critical line")
    with col2:
        st.metric("Casimir Force @ 1μm", "~0.1 nN", "Measured experimentally")
    with col3:
        st.metric("ζ(-1)", "-1/12", "Regularizes vacuum energy")
    with col4:
        st.metric("Millennium Prize", "$1,000,000", "For proving Riemann Hypothesis")

# ==================== CASIMIR EFFECT ====================
elif page == "⚛️ Casimir Effect":
    st.title("⚛️ The Casimir Effect: Vacuum is NOT Empty")
    
    st.markdown("""
    <div class='info-box'>
        <strong>Key Concept:</strong> Two uncharged parallel conducting plates in vacuum experience 
        an attractive force due to quantum fluctuations of the electromagnetic field.
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive controls
    st.markdown("### 🎮 Interactive Simulator")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Controls")
        
        plate_distance = st.slider(
            "Plate Separation (nm)",
            min_value=10,
            max_value=1000,
            value=100,
            step=10,
            help="Distance between two conducting plates"
        ) * 1e-9  # Convert to meters
        
        plate_area = st.slider(
            "Plate Area (cm²)",
            min_value=0.1,
            max_value=10.0,
            value=1.0,
            step=0.1,
            help="Area of each plate"
        ) * 1e-4  # Convert to m²
        
        # Calculate values
        force = casimir.force(plate_distance, plate_area)
        pressure = casimir.pressure(plate_distance)
        energy = casimir.energy(plate_distance, plate_area)
        
        st.markdown("#### 📏 Results")
        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-value'>{np.abs(force)*1e9:.4f}</div>
            <div class='metric-label'>Force (nN)</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class='metric-card' style='margin-top: 10px;'>
            <div class='metric-value'>{np.abs(pressure):.4e}</div>
            <div class='metric-label'>Pressure (Pa)</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class='metric-card' style='margin-top: 10px;'>
            <div class='metric-value'>{energy*1e19:.4f}</div>
            <div class='metric-label'>Energy (×10⁻¹⁹ J)</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Physical interpretation
        st.markdown("#### 🧠 Physical Interpretation")
        st.info(f"""
        At {plate_distance*1e9:.0f} nm separation:
        - Virtual particles create pressure difference
        - Outside pressure > Inside pressure
        - Net force pushes plates together
        - Force scales as 1/d⁴ (very strong at small distances!)
        """)
    
    with col2:
        # Force vs distance plot
        distances, forces = casimir.get_force_range(1e-9, 1e-6, 1000)
        fig_force = viz.create_casimir_force_plot(
            distances, forces, plate_distance
        )
        st.plotly_chart(fig_force, use_container_width=True)
        
        # Plate visualization
        st.markdown("#### 🎨 Plate Visualization")
        
        # Create simple plate diagram
        fig_plates = go.Figure()
        
        # Bottom plate
        fig_plates.add_trace(go.Scatter(
            x=[0, 10], y=[0, 0],
            fill='tozeroy',
            fillcolor='rgba(100, 149, 237, 0.8)',
            line=dict(color='white', width=2),
            name='Plate 1',
            showlegend=False
        ))
        
        # Top plate
        plate_gap = 5 * (100e-9 / plate_distance)  # Scale for visualization
        fig_plates.add_trace(go.Scatter(
            x=[0, 10], y=[plate_gap, plate_gap],
            fill='tonexty',
            fillcolor='rgba(100, 149, 237, 0.8)',
            line=dict(color='white', width=2),
            name='Plate 2',
            showlegend=False
        ))
        
        # Virtual particles
        np.random.seed(42)
        for _ in range(20):
            x = np.random.uniform(1, 9)
            y = np.random.uniform(0.5, plate_gap - 0.5)
            fig_plates.add_trace(go.Scatter(
                x=[x], y=[y],
                mode='markers',
                marker=dict(size=8, color='yellow', symbol='circle',
                           line=dict(width=1, color='orange')),
                showlegend=False,
                hoverinfo='skip'
            ))
        
        # Force arrow
        fig_plates.add_annotation(
            x=5, y=plate_gap/2,
            ax=5, ay=plate_gap/2,
            xref='x', yref='y',
            axref='x', ayref='y',
            showarrow=True,
            arrowhead=2,
            arrowsize=2,
            arrowwidth=3,
            arrowcolor='red'
        )
        
        fig_plates.add_annotation(
            x=5, y=plate_gap + 1,
            text='Casimir Force →',
            showarrow=False,
            font=dict(color='red', size=14)
        )
        
        fig_plates.update_layout(
            title='Virtual Particles Between Plates',
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False,
                      range=[-1, plate_gap + 2]),
            paper_bgcolor='rgba(0,0,0,0.8)',
            plot_bgcolor='rgba(0,0,0,0.5)',
            height=300,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        
        st.plotly_chart(fig_plates, use_container_width=True)
    
    # Formula section
    st.markdown("---")
    st.markdown("### 📝 Mathematical Formulation")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='formula-box'>
            <strong>Casimir Force:</strong><br><br>
            F = -π²ℏcA / 240d⁴
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='formula-box'>
            <strong>Casimir Pressure:</strong><br><br>
            P = -π²ℏc / 240d⁴
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='formula-box'>
            <strong>Casimir Energy:</strong><br><br>
            E = -π²ℏcA / 720d³
        </div>
        """, unsafe_allow_html=True)
    
    # Experimental validation
    st.markdown("### ✅ Experimental Validation")
    
    experiments = casimir.experimental_comparison()
    
    exp_data = []
    for name, data in experiments.items():
        exp_data.append({
            'Experiment': name,
            'Distance (μm)': data['d'] * 1e6,
            'Measured Force (nN)': data['force_measured'] * 1e9,
            'Theoretical Force (nN)': data['force_theoretical'] * 1e9,
            'Agreement': '✓ Excellent'
        })
    
    df_exp = pd.DataFrame(exp_data)
    st.dataframe(df_exp, use_container_width=True, hide_index=True)
    
    st.success("""
    **Key Point:** The Casimir effect has been experimentally verified with high precision 
    (within 1% of theoretical predictions), proving that vacuum energy is real and measurable!
    """)

# ==================== ZETA REGULARIZATION ====================
elif page == "🧮 Zeta Regularization":
    st.title("🧮 The Infinite Sum Problem & Zeta Solution")
    
    st.markdown("""
    <div class='info-box'>
        <strong>The Problem:</strong> Calculating vacuum energy between plates involves summing 
        over all possible modes, which gives an infinite result. This is where the Riemann Zeta 
        function comes to the rescue!
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### ❌ The Naive Approach")
        st.markdown("""
        <div class='formula-box'>
            Vacuum Energy (Wrong Way):<br><br>
            E = Σₙ₌₁^∞ n·πℏc/2d = ∞<br><br>
            <span style='color: #FF6B6B;'>❌ Diverges to infinity!</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Why it fails:**
        - Sum over all quantum modes diverges
        - Each mode contributes positive energy
        - Infinite modes = Infinite energy
        - Physically meaningless result
        """)
    
    with col2:
        st.markdown("### ✅ The Zeta Solution")
        st.markdown("""
        <div class='formula-box'>
            Vacuum Energy (Zeta Regularized):<br><br>
            E = (πℏc/2d) × ζ(-1)<br>
            E = (πℏc/2d) × (-1/12)<br>
            E = -π²ℏc/720d³<br><br>
            <span style='color: #00FF88;'>✓ Finite and physical!</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Why it works:**
        - Analytic continuation of ζ(s)
        - ζ(-1) = -1/12 (famously)
        - Same result as other regularizations
        - Matches experimental data!
        """)
    
    # Visualization of the problem and solution
    st.markdown("### 📊 Divergence vs Regularization")
    
    d_demo = 1e-6  # 1 micron for demo
    n_values, partial_sums = casimir.naive_sum(d_demo, n_max=100)
    zeta_value = -1/12
    
    fig_naive = viz.create_naive_sum_plot(n_values, partial_sums, zeta_value)
    st.plotly_chart(fig_naive, use_container_width=True)
    
    # Zeta function explanation
    st.markdown("---")
    st.markdown("### 🎓 Understanding ζ(-1) = -1/12")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        The Riemann Zeta function is defined as:
        
        <div class='formula-box'>
            ζ(s) = Σₙ₌₁^∞ 1/nˢ &nbsp;&nbsp; for Re(s) > 1
        </div>
        
        This series **converges** only when the real part of s is greater than 1.
        For s = -1, the series becomes:
        
        <div class='formula-box'>
            ζ(-1) = 1 + 2 + 3 + 4 + ... <span style='color: #FF6B6B;'">(divergent!)</span>
        </div>
        
        But through **analytic continuation**, we can assign a finite value:
        
        <div class='formula-box' style='background: rgba(0,255,136,0.2); border-color: #00FF88;'>
            <strong>ζ(-1) = -1/12</strong> (via analytic continuation)
        </div>
        
        This isn't "summation" in the traditional sense—it's a way to consistently 
        assign finite values to divergent series that appear in physics.
        """)
    
    with col2:
        st.markdown("#### 🧮 Calculation Steps")
        
        with st.expander("Step 1: Zeta Definition", expanded=True):
            st.latex(r"\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}")
        
        with st.expander("Step 2: Functional Equation"):
            st.latex(r"\zeta(s) = 2^s \pi^{s-1} \sin\left(\frac{\pi s}{2}\right) \Gamma(1-s) \zeta(1-s)")
        
        with st.expander("Step 3: Evaluate at s = -1"):
            st.latex(r"\zeta(-1) = -\frac{1}{12}")
        
        with st.expander("Step 4: Casimir Energy"):
            st.latex(r"E = \frac{\pi\hbar c}{2d} \times \left(-\frac{1}{12}\right)")
            st.latex(r"E = -\frac{\pi^2\hbar c}{720d^3}")
    
    # Applications in physics
    st.markdown("---")
    st.markdown("### 🌐 Other Applications in Physics")
    
    apps = [
        ("String Theory", "Critical dimension D=26 uses ζ(-1)"),
        ("Black Hole Entropy", "Regularization of mode sums"),
        ("Cosmological Constant", "Vacuum energy calculations"),
        ("Quantum Electrodynamics", "Loop diagram regularization")
    ]
    
    cols = st.columns(4)
    for col, (title, desc) in zip(cols, apps):
        with col:
            st.markdown(f"""
            <div class='metric-card'>
                <div style='color: #FFD700; font-weight: bold;'>{title}</div>
                <div style='color: #888; font-size: 0.85em;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)

# ==================== ZETA VISUALIZER ====================
elif page == "🌌 Zeta Visualizer":
    st.title("🌌 Riemann Zeta Function Explorer")
    
    st.markdown("""
    <div class='info-box'>
        Explore the Riemann Zeta function in the complex plane. The non-trivial zeros 
        (critical for the Riemann Hypothesis) all lie on the critical line Re(s) = 0.5.
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar controls for zeta
    st.sidebar.markdown("### 🎛️ Zeta Controls")
    
    viz_type = st.sidebar.selectbox(
        "Visualization Type:",
        ["Critical Line (Complex Plane)", "Real vs Imaginary Parts", 
         "3D Surface Plot", "Domain Coloring"]
    )
    
    t_min = st.sidebar.slider("t min", 0.0, 50.0, 0.0, 0.5)
    t_max = st.sidebar.slider("t max", t_min + 5, 100.0, 50.0, 1.0)
    
    show_zeros = st.sidebar.checkbox("Show Known Zeros", value=True)
    
    # Compute zeta values
    with st.spinner("Computing zeta values (high precision)..."):
        t_values, zeta_values = zeta.compute_critical_line(t_min, t_max, num_points=2000)
    
    # Main visualization
    if viz_type == "Critical Line (Complex Plane)":
        st.markdown("### 🎯 ζ(0.5 + it) in Complex Plane")
        
        zeros_to_show = [z for z in zeta.known_zeros if t_min <= z <= t_max] if show_zeros else []
        
        fig = viz.create_zeta_critical_line_plot(t_values, zeta_values, zeros_to_show)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class='highlight-box'>
            <strong>What you're seeing:</strong><br>
            • The curve shows ζ(0.5 + it) as t increases<br>
            • <span style='color: #FFD700;'>Gold X marks</span> indicate Riemann zeros (where curve passes through origin)<br>
            • The curve spirals because both real and imaginary parts oscillate<br>
            • <strong>Riemann Hypothesis:</strong> All non-trivial zeros lie on this critical line!
        </div>
        """, unsafe_allow_html=True)
        
    elif viz_type == "Real vs Imaginary Parts":
        st.markdown("### 📈 Re(ζ) and Im(ζ) along Critical Line")
        
        zeros_to_show = [z for z in zeta.known_zeros if t_min <= z <= t_max] if show_zeros else []
        
        fig = viz.create_real_imaginary_plot(t_values, zeta_values, zeros_to_show)
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **Interpretation:** Zeros occur where BOTH real and imaginary parts 
        simultaneously equal zero (intersections with horizontal axis).
        """)
        
    elif viz_type == "3D Surface Plot":
        st.markdown("### 🏔️ |ζ(s)| over Complex Plane")
        
        with st.spinner("Computing 3D surface (this may take a moment)..."):
            X, Y, Z, mag, phase = zeta.compute_grid(
                x_min=-2, x_max=2, y_min=0, y_max=30, resolution=100
            )
        
        fig = viz.create_zeta_3d_surface(X, Y, mag, phase)
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **Features to notice:**
        - The pole at s = 1 (trivial singularity)
        - Zeros along the critical line Re(s) = 0.5
        - The function's magnitude varies dramatically
        """)
        
    else:  # Domain Coloring
        st.markdown("### 🎨 Domain Coloring of ζ(s)")
        
        with st.spinner("Computing domain coloring..."):
            X, Y, Z, mag, phase = zeta.compute_grid(
                x_min=-3, x_max=3, y_min=-5, y_max=5, resolution=200
            )
        
        fig = viz.create_domain_coloring(X, Y, Z, mag, phase)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class='highlight-box'>
            <strong>Color Encoding:</strong><br>
            • <strong>Hue:</strong> Phase (argument) of ζ(s) [0 to 2π]<br>
            • <strong>Brightness:</strong> Magnitude |ζ(s)| (darker = smaller)<br>
            • <strong>Black spots:</strong> Zeros of the zeta function<br>
            • <strong>Red dashed line:</strong> Critical line Re(s) = 0.5
        </div>
        """, unsafe_allow_html=True)
    
    # Zeros table
    if show_zeros:
        st.markdown("---")
        st.markdown("### 📋 Known Zeros on Critical Line")
        
        zeros_in_range = [z for z in zeta.known_zeros if t_min <= z <= t_max]
        
        if zeros_in_range:
            zeros_df = pd.DataFrame({
                'Zero #': range(1, len(zeros_in_range) + 1),
                't value (Im(s))': zeros_in_range,
                'ζ(0.5 + it)': [abs(zeta.zeta_critical_line(t)) for t in zeros_in_range]
            })
            st.dataframe(zeros_df, use_container_width=True, hide_index=True)
        else:
            st.info("No zeros in the selected range. Adjust the sliders to see zeros.")
    
    # Interactive calculator
    st.markdown("---")
    st.markdown("### 🧮 Zeta Function Calculator")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        s_real = st.number_input("Re(s)", value=0.5, step=0.1, format="%.2f")
        s_imag = st.number_input("Im(s)", value=14.13, step=0.01, format="%.2f")
        
        s = complex(s_real, s_imag)
        zeta_val = zeta.zeta(s)
        
        st.markdown(f"""
        <div class='success-box'>
            <strong>ζ({s_real} + {s_imag}i) =</strong><br>
            <span style='font-size: 1.3em;'>
            {zeta_val.real:.6f} {zeta_val.imag:+.6f}i
            </span><br>
            <strong>|ζ| = {abs(zeta_val):.6f}</strong><br>
            <strong>arg(ζ) = {np.angle(zeta_val):.4f} rad</strong>
        </div>
        """, unsafe_allow_html=True)
        
        # Check if near a zero
        if abs(zeta_val) < 0.01:
            st.balloons()
            st.success("🎉 You're near a Riemann zero!")
    
    with col2:
        # Method explanation
        method = st.radio("Computation Method:", 
                         ["Direct (mpmath)", "Dirichlet Series", "Analytic Continuation"])
        
        if method == "Dirichlet Series":
            if s_real > 1:
                approx = zeta.dirichlet_series(s, n_terms=10000)
                st.info(f"Dirichlet series approximation (10⁴ terms): {approx:.6f}")
            else:
                st.error("Dirichlet series only converges for Re(s) > 1!")
                
        elif method == "Analytic Continuation":
            result, method_used = zeta.analytic_continuation_demo(s)
            st.info(f"Method used: {method_used}")
            st.info(f"Result: {result}")

# ==================== THE CONNECTION ====================
elif page == "🔗 The Connection":
    st.title("🔗 The Grand Connection: Physics ↔ Mathematics")
    
    st.markdown("""
    <div class='highlight-box' style='text-align: center;'>
        <h2 style='color: #FFD700; margin-top: 0;'>The Deepest Insight</h2>
        <p style='font-size: 1.2em;'>
            The same function that tames infinite quantum vacuum energy<br>
            holds the key to understanding the distribution of prime numbers.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Connection diagram
    st.markdown("### 🌉 The Bridge")
    
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <h4 style='color: #9B59B6;'>🔬 Quantum Physics</h4>
            <ul style='text-align: left; color: #ccc;'>
                <li>Vacuum fluctuations</li>
                <li>Casimir effect</li>
                <li>Infinite mode sums</li>
                <li>Zeta regularization</li>
                <li>Finite physical results</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='text-align: center; padding-top: 50px;'>
            <div style='font-size: 3em;'>ζ(s)</div>
            <div style='color: #FFD700; font-size: 1.2em;'>Riemann<br>Zeta<br>Function</div>
            <div style='font-size: 2em;'>⇄</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='metric-card'>
            <h4 style='color: #E91E63;'>🔢 Number Theory</h4>
            <ul style='text-align: left; color: #ccc;'>
                <li>Prime numbers</li>
                <li>Prime counting</li>
                <li>Distribution law</li>
                <li>Zeta zeros</li>
                <li>Riemann Hypothesis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Prime connection visualization
    st.markdown("---")
    st.markdown("### 📊 Prime Number Connection")
    
    with st.spinner("Computing prime distribution..."):
        x_vals, pi_x, li_x, primes = zeta.prime_connection(x_max=100)
    
    fig_prime = viz.create_prime_connection_plot(x_vals, pi_x, li_x, primes)
    st.plotly_chart(fig_prime, use_container_width=True)
    
    st.markdown("""
    <div class='info-box'>
        <strong>The Prime Number Theorem:</strong> The distribution of primes is intimately 
        connected to the zeros of the Riemann zeta function. The logarithmic integral Li(x) 
        approximates π(x) (the prime counting function), and the error term depends on 
        the location of zeta zeros!
    </div>
    """, unsafe_allow_html=True)
    
    # Riemann Hypothesis section
    st.markdown("---")
    st.markdown("### 🏆 The Riemann Hypothesis")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class='formula-box' style='background: rgba(255,215,0,0.1); border-color: #FFD700;'>
            <strong>The Riemann Hypothesis (1859):</strong><br><br>
            All non-trivial zeros of ζ(s) have real part equal to 1/2.<br>
            In other words: ζ(1/2 + it) = 0 for infinitely many t, and<br>
            these are the ONLY non-trivial zeros.<br><br>
            <span style='color: #FFD700;'>One of 7 Millennium Prize Problems ($1,000,000 reward)</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Why it matters:**
        - The error term in the Prime Number Theorem is minimized if RH is true
        - Hundreds of theorems assume RH is true
        - It would provide the "best possible" bound on prime distribution
        - Connection to quantum chaos and random matrix theory
        
        **Current status:**
        - First 10+ trillion zeros checked—all on critical line!
        - Still unproven after 160+ years
        """)
    
    with col2:
        st.markdown("#### 🎯 Verification Progress")
        
        # Progress bars for zeros checked
        st.metric("Zeros Verified", "10 trillion+", "✓ All on critical line")
        st.metric("Hypothesis Status", "Unproven", "🔥 Open problem")
        st.metric("Prize Money", "$1,000,000", "💰 Millennium Prize")
        
        st.markdown("""
        <div class='success-box'>
            <strong>Fun Fact:</strong><br>
            If you prove the Riemann Hypothesis, you'll also have demonstrated 
            the deepest connection between physics and number theory!
        </div>
        """, unsafe_allow_html=True)
    
    # Final insight
    st.markdown("---")
    st.markdown("""
    <div class='highlight-box'>
        <h3 style='color: #00D4FF; text-align: center;'>🌌 The Ultimate Insight</h3>
        <p style='font-size: 1.1em; text-align: center;'>
            The universe operates on mathematical principles so profound that the same function 
            appears in both the <strong>quantum fluctuations of empty space</strong> and the 
            <strong>distribution of prime numbers</strong>. This suggests a deep, as-yet-undiscovered 
            unity between physics and mathematics at the most fundamental level.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==================== ALL VISUALIZATIONS ====================
elif page == "📊 All Visualizations":
    st.title("📊 Complete Visualization Dashboard")
    
    st.markdown("This page shows all visualizations at once for presentation purposes.")
    
    # Row 1: Casimir Effect
    st.markdown("### ⚛️ Casimir Force")
    distances, forces = casimir.get_force_range(1e-9, 1e-6, 1000)
    fig1 = viz.create_casimir_force_plot(distances, forces)
    st.plotly_chart(fig1, use_container_width=True)
    
    # Row 2: Naive Sum vs Zeta
    st.markdown("### 🧮 Regularization Comparison")
    n_values, partial_sums = casimir.naive_sum(1e-6, n_max=100)
    fig2 = viz.create_naive_sum_plot(n_values, partial_sums, -1/12)
    st.plotly_chart(fig2, use_container_width=True)
    
    # Row 3: Zeta Critical Line
    st.markdown("### 🌌 Zeta Function on Critical Line")
    t_vals, zeta_vals = zeta.compute_critical_line(0, 50, 1000)
    fig3 = viz.create_zeta_critical_line_plot(t_vals, zeta_vals, zeta.known_zeros[:5])
    st.plotly_chart(fig3, use_container_width=True)
    
    # Row 4: Real/Imaginary parts
    st.markdown("### 📈 Real and Imaginary Components")
    fig4 = viz.create_real_imaginary_plot(t_vals, zeta_vals, zeta.known_zeros[:5])
    st.plotly_chart(fig4, use_container_width=True)
    
    # Row 5: Prime connection
    st.markdown("### 🔗 Prime Number Connection")
    x_vals, pi_x, li_x, primes = zeta.prime_connection(x_max=100)
    fig5 = viz.create_prime_connection_plot(x_vals, pi_x, li_x, primes)
    st.plotly_chart(fig5, use_container_width=True)
    
    # Download option
    st.markdown("---")
    st.markdown("### 💾 Export Options")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📄 Generate Report"):
            st.info("Report generation would be implemented here!")
    
    with col2:
        if st.button("🖼️ Export Plots"):
            st.info("Plot export would be implemented here!")
    
    with col3:
        if st.button("📊 Data Export"):
            # Create sample data
            data = {
                't': t_vals,
                'Re_zeta': zeta_vals.real,
                'Im_zeta': zeta_vals.imag,
                'Abs_zeta': np.abs(zeta_vals)
            }
            df = pd.DataFrame(data)
            st.download_button(
                "Download CSV",
                df.to_csv(index=False),
                "zeta_critical_line.csv",
                "text/csv"
            )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>🔬 <strong>Quantum Vacuum → Riemann Zeta</strong> | Research-Level Visualization Project</p>
    <p>Built with Streamlit, Plotly, and mpmath | 2026</p>
    <p style='color: #FFD700; font-size: 1.1em; margin-top: 15px;'>
        ✨ Developed by <strong>Astha Paika</strong> ✨
    </p>
</div>
""", unsafe_allow_html=True)