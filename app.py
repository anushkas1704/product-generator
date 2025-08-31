# app.py
import os
from dotenv import load_dotenv
import streamlit as st
from huggingface_hub import InferenceClient
import google.generativeai as genai
from PIL import Image

# Load env 
load_dotenv()
HF_TOKEN = os.getenv("HF_API_KEY")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

# Hugging Face client (Flux model)
hf_client = InferenceClient(
    "black-forest-labs/FLUX.1-schnell",
    token=HF_TOKEN
)

# Gemini config
genai.configure(api_key=GEMINI_KEY)

# Streamlit UI
st.set_page_config(page_title="AI Product Generator", page_icon="✨")
st.title("✨ AI Product Generator")

st.write("Enter your product idea and let AI generate a description & an image.")

# Input
product_name = st.text_input("🛍️ Product Name", placeholder="Eco-friendly water bottle for travelers")
generate_btn = st.button("Generate")

if generate_btn and product_name:
    with st.spinner("Generating product description..."):
        # Gemini text generation
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Generate a creative, marketing-friendly product description for: {product_name}"
        response = model.generate_content(prompt)
        description = response.text
    
    st.subheader("📄 Product Description")
    st.write(description)

    with st.spinner("Generating product image..."):
        # Flux image gen
        image = hf_client.text_to_image(product_name)
    
    st.subheader("🖼️ Product Image")
    st.image(image, caption=product_name)
