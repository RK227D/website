import streamlit as st
from PIL import Image

# Set up the page configuration
st.set_page_config(page_title="Logo Design by [Your Name]", page_icon="🎨")

# Load images for the portfolio
portfolio_images = {
    "Logo 1": "path/to/logo1.png",
    "Logo 2": "path/to/logo2.png",
    "Logo 3": "path/to/logo3.png",
}

# Define functions for each page
def home():
    st.title("Welcome to My Logo Design Studio")
    st.image("path/to/hero_image.jpg", use_column_width=True)
    st.write("""
    I specialize in creating unique and memorable logos that truly capture your brand's essence.
    Explore my portfolio to see my work or get in touch to discuss your project!
    """)

def portfolio():
    st.title("My Portfolio")
    cols = st.columns(3)
    for i, (title, img_path) in enumerate(portfolio_images.items()):
        with cols[i % 3]:
            img = Image.open(img_path)
            st.image(img, caption=title, use_column_width=True)

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
