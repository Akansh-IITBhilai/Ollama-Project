import streamlit as st
import ollama

# Initialize Ollama client
client = ollama.Client()

# Page configuration
st.set_page_config(
    page_title="AI Assistant - Powered by Ollama",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for background
if 'background_image' not in st.session_state:
    st.session_state.background_image = "https://images.unsplash.com/photo-1557683316-973673baf926?w=1600&h=900&fit=crop"

# Dynamic CSS with background image
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{st.session_state.background_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .main-header {{
        text-align: center;
        color: #ffffff;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 2rem;
        text-shadow:
            -1px -1px 0 #000,
            1px -1px 0 #000,
            -1px 1px 0 #000,
            1px 1px 0 #000,
            0 0 10px rgba(0,0,0,0.8),
            0 0 20px rgba(0,0,0,0.6),
            0 0 30px rgba(0,0,0,0.4);
        -webkit-text-stroke: 1px rgba(0,0,0,0.3);
    }}
    .subtitle {{
        text-align: center;
        color: #ffffff;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        text-shadow:
            -1px -1px 0 #000,
            1px -1px 0 #000,
            -1px 1px 0 #000,
            1px 1px 0 #000,
            0 0 8px rgba(0,0,0,0.8);
        font-weight: 600;
        -webkit-text-stroke: 0.5px rgba(0,0,0,0.2);
    }}
    .chat-container {{
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255,255,255,0.2);
    }}
    .chat-container h3 {{
        color: #2c3e50 !important;
        text-shadow: none !important;
        -webkit-text-stroke: none !important;
        font-weight: bold;
    }}
    .user-message {{
        background: rgba(227, 242, 253, 0.95);
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid #2196f3;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        backdrop-filter: blur(5px);
    }}
    .bot-message {{
        background: rgba(245, 245, 245, 0.95);
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid #4caf50;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        backdrop-filter: blur(5px);
    }}
    .input-container {{
        background: rgba(255, 255, 255, 0.95);
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 16px rgba(0,0,0,0.2);
        margin-top: 2rem;
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255,255,255,0.2);
    }}
    .input-container h3 {{
        color: #2c3e50 !important;
        text-shadow: none !important;
        -webkit-text-stroke: none !important;
        font-weight: bold;
    }}
    .stTextInput > div > div > input {{
        border-radius: 8px;
        border: 2px solid rgba(0,0,0,0.1);
        padding: 0.75rem;
        font-size: 1rem;
        background: rgba(255,255,255,0.9);
        backdrop-filter: blur(5px);
    }}
    .stButton > button {{
        background: linear-gradient(45deg, #2196f3, #21cbf3);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-size: 1rem;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        text-shadow: 0 1px 2px rgba(0,0,0,0.3);
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }}
    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(33, 150, 243, 0.4);
    }}
    .footer {{
        text-align: center;
        color: #ffffff;
        margin-top: 3rem;
        padding: 1rem;
        border-top: 1px solid rgba(255,255,255,0.2);
        text-shadow:
            -1px -1px 0 #000,
            1px -1px 0 #000,
            -1px 1px 0 #000,
            1px 1px 0 #000,
            0 0 8px rgba(0,0,0,0.8);
        font-weight: 500;
        -webkit-text-stroke: 0.5px rgba(0,0,0,0.2);
    }}
    .sidebar-content {{
        background: rgba(255, 255, 255, 0.95);
        padding: 1rem;
        border-radius: 10px;
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255,255,255,0.2);
    }}
    .sidebar-content h1, .sidebar-content h2, .sidebar-content h3 {{
        color: #2c3e50 !important;
        text-shadow: none !important;
        -webkit-text-stroke: none !important;
    }}
    .sidebar-content p {{
        color: #34495e !important;
    }}
    .stSelectbox label, .stTextInput label {{
        color: #2c3e50 !important;
        font-weight: 600 !important;
        text-shadow: none !important;
    }}
    .stSuccess {{
        background: rgba(76, 175, 80, 0.9) !important;
        color: white !important;
        border-radius: 8px;
        backdrop-filter: blur(5px);
    }}
    .stInfo {{
        background: rgba(33, 150, 243, 0.9) !important;
        color: white !important;
        border-radius: 8px;
        backdrop-filter: blur(5px);
    }}
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.title("⚙️ Settings")
    st.markdown("---")

    # Model selection
    available_models = ["tinyllama", "phi", "gemma:2b"]
    selected_model = st.selectbox(
        "Choose AI Model:",
        available_models,
        index=0,
        help="Select the AI model to use for responses"
    )

    st.markdown("---")

    # Background image changer
    st.markdown("### 🎨 Background")
    bg_url = st.text_input(
        "Background Image URL:",
        value=st.session_state.background_image,
        help="Enter a URL for your custom background image"
    )

    if st.button("🔄 Apply Background"):
        st.session_state.background_image = bg_url
        st.success("Background updated! Refreshing...")
        st.rerun()

    # Preset backgrounds
    st.markdown("**Quick Backgrounds:**")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌊 Ocean"):
            st.session_state.background_image = "https://images.unsplash.com/photo-1505142468610-359e7d316be0?w=1600&h=900&fit=crop"
            st.rerun()
        if st.button("🌌 Space"):
            st.session_state.background_image = "https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?w=1600&h=900&fit=crop"
            st.rerun()
    with col2:
        if st.button("🌲 Forest"):
            st.session_state.background_image = "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=1600&h=900&fit=crop"
            st.rerun()
        if st.button("🏙️ City"):
            st.session_state.background_image = "https://images.unsplash.com/photo-1514565131-fce0801e5785?w=1600&h=900&fit=crop"
            st.rerun()

    st.markdown("---")

    # About section
    st.markdown("### 🤖 About")
    st.markdown("This AI assistant is powered by Ollama and runs locally on your machine.")
    st.markdown("**Current Model:** " + selected_model)

    st.markdown("---")
    st.markdown("### 📊 System Info")
    st.markdown(f"**Status:** 🟢 Online")

    st.markdown('</div>', unsafe_allow_html=True)

# Main content
st.markdown('<h1 class="main-header">🤖 AI Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your intelligent companion powered by local AI models</p>', unsafe_allow_html=True)

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Chat interface
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
st.markdown("### 💬 Chat History")

if st.session_state.chat_history:
    for message in st.session_state.chat_history:
        if message['role'] == 'user':
            st.markdown(f'<div class="user-message"><strong>You:</strong> {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-message"><strong>Assistant:</strong> {message["content"]}</div>', unsafe_allow_html=True)
else:
    st.info("👋 Start a conversation by typing a message below!")

st.markdown('</div>', unsafe_allow_html=True)

# Input section
st.markdown('<div class="input-container">', unsafe_allow_html=True)
st.markdown("### ✍️ Your Message")

col1, col2 = st.columns([4, 1])

with col1:
    user_input = st.text_input(
        "",
        placeholder="Type your message here...",
        key="user_input",
        label_visibility="collapsed"
    )

with col2:
    send_button = st.button("🚀 Send", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# Process user input
if send_button and user_input.strip():
    # Add user message to history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Generate response
    with st.spinner("🤔 Thinking..."):
        try:
            response = client.generate(model=selected_model, prompt=user_input)
            bot_response = response['response']

            # Add bot response to history
            st.session_state.chat_history.append({"role": "assistant", "content": bot_response})

            # Rerun to update chat history display
            st.rerun()

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Clear chat button
if st.session_state.chat_history:
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

# Footer
st.markdown("""
    <div class="footer">
        <p>Created with ❤️ by Akansh Tyagi | Powered by Streamlit & Ollama</p>
        <p>🌟 Dedicated to my family: Hamendra, Shalini, and Aditya Tyagi</p>
    </div>
""", unsafe_allow_html=True)