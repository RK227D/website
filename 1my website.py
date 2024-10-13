import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Logo Design by [Your Name]", page_icon="🎨")

# Define functions for each page
def home():
    st.title("Welcome to My Logo Design Studio")
    st.write("""
    I specialize in creating unique and memorable logos that truly capture your brand's essence.
    Explore my portfolio to see my work or get in touch to discuss your project!
    """)

def portfolio():
    st.title("My Portfolio")
    st.write("""
    Here are some of the logos I have designed:
    
    - **Logo 1**: A modern take on a classic design.
    - **Logo 2**: A minimalistic approach that stands out.
    - **Logo 3**: A vibrant and colorful representation of creativity.
    
    Feel free to ask about any of these designs!
    """)

def about():
    st.title("About Me")
    st.write("""
    I'm [Your Name], a passionate logo designer with a love for creativity and branding. 
    My design philosophy combines research, creativity, and collaboration to deliver logos that 
    resonate with your audience.
    """)

def contact():
    st.title("Contact Me")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    
    if st.button("Send"):
        st.success("Message sent! I'll get back to you soon.")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Portfolio", "About", "Contact"])

# Render the selected page
if page == "Home":
    home()
elif page == "Portfolio":
    portfolio()
elif page == "About":
    about()
elif page == "Contact":
    contact()
