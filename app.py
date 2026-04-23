import streamlit as st
from streamlit_drawable_canvas import st_canvas

# 🎨 ESTILOS CELESTE + BURBUJAS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #e0f7ff, #bae6fd);
    color: #0f172a;
}

/* TÍTULO */
h1 {
    text-align: center;
    color: #0284c7;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #e0f2fe;
}

/* BURBUJAS */
.bubble {
    position: fixed;
    border-radius: 50%;
    opacity: 0.2;
    background: #38bdf8;
    animation: float 10s infinite;
}

.b1 { width: 80px; height: 80px; left: 10%; bottom: -100px; animation-delay: 0s;}
.b2 { width: 60px; height: 60px; left: 30%; bottom: -100px; animation-delay: 2s;}
.b3 { width: 100px; height: 100px; left: 60%; bottom: -100px; animation-delay: 4s;}
.b4 { width: 50px; height: 50px; left: 80%; bottom: -100px; animation-delay: 6s;}

@keyframes float {
    0% { transform: translateY(0); }
    100% { transform: translateY(-120vh); }
}

/* CANVAS */
canvas {
    border-radius: 15px;
    border: 2px solid #7dd3fc;
}

/* CENTRAR */
.element-container:has(canvas) {
    display: flex;
    justify-content: center;
}
</style>

<div class="bubble b1"></div>
<div class="bubble b2"></div>
<div class="bubble b3"></div>
<div class="bubble b4"></div>

""", unsafe_allow_html=True)

# 🐋 TÍTULO
st.title("🌊 Tablero Creativo")

# SIDEBAR
with st.sidebar:
    st.subheader("⚙️ Propiedades del Tablero")

    st.subheader("📐 Dimensiones")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)

    drawing_mode = st.selectbox(
        "🖌️ Herramienta de dibujo",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    stroke_width = st.slider('✏️ Ancho de línea', 1, 30, 15)
    stroke_color = st.color_picker("🎨 Color de trazo", "#000000")
    bg_color = st.color_picker("🧊 Color de fondo", "#FFFFFF")

# CANVAS
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.2)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}",
)
