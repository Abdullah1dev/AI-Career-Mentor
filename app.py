import streamlit as st
from chatbot import AICareerMentor


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Career Mentor",
    page_icon="🎓",
    layout="centered"
)


# -----------------------------
# Initialize Chatbot
# -----------------------------

@st.cache_resource
def get_chatbot():
    return AICareerMentor()


chatbot = get_chatbot()


# -----------------------------
# Session State
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Header
# -----------------------------

st.title("🎓 AI Career Mentor")

st.write(
    "Your AI-powered career assistant for learning roadmaps, "
    "AI/tech career guidance, projects, and interview preparation."
)


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.header("About AI Career Mentor")

    st.write(
        "AI Career Mentor is designed to help students and "
        "early-career developers make better decisions about "
        "their technology careers."
    )

    st.divider()

    st.subheader("I can help you with:")

    st.write("🎯 Career planning")
    st.write("📚 Learning roadmaps")
    st.write("💻 Project ideas")
    st.write("🧠 AI/ML skills")
    st.write("📝 Interview preparation")
    st.write("💼 Internship preparation")

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# -----------------------------
# Display Previous Messages
# -----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# -----------------------------
# User Input
# -----------------------------

user_input = st.chat_input(
    "Ask me anything about your tech career..."
)


# -----------------------------
# Generate Response
# -----------------------------

if user_input:

    # Display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = chatbot.chat(user_input)

                st.markdown(response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )

            except Exception as e:

                error_message = (
                    "Sorry, something went wrong while "
                    "connecting to the AI mentor."
                )

                st.error(error_message)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message
                    }
                )