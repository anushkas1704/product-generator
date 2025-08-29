import streamlit as st
from transformers import pipeline
import requests
from io import BytesIO
from PIL import Image

# -----------------------------
# Hugging Face Setup
# -----------------------------
HF_API_KEY = "YOUR_HUGGINGFACE_API_KEY"  # Replace with your free API key from https://huggingface.co/settings/tokens
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

# Text generation pipeline
text_generator = pipeline("text-generation", model="distilgpt2")

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="AI Product Generator", layout="centered")
st.title("🛍️ AI Product Description + Image Generator")
st.write("Generate product descriptions + images for free using Hugging Face models")

# Input fields
product = st.text_input("Enter product name")
keywords = st.text_input("Enter keywords (comma separated)")
tone = st.selectbox("Choose tone", ["Professional", "Casual", "Persuasive", "Funny"])

if st.button("Generate"):
    # --- Generate Description ---
    with st.spinner("Generating description..."):
        prompt = f"Write a {tone.lower()} product description for {product}. Keywords: {keywords}."
        desc = text_generator(prompt, max_length=80, do_sample=True)[0]["generated_text"]
        st.subheader("📄 Product Description")
        st.write(desc)

    # --- Generate Image ---
    with st.spinner("Generating image..."):
        api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
        payload = {"inputs": f"Product photo of {product}, studio lighting, minimalistic, professional"}
        
        response = requests.post(api_url, headers=headers, json=payload)

        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            st.subheader("🖼️ Product Image")
            st.image(image, caption=product, use_column_width=True)
        else:
            st.error("Image generation failed. Try again.")
