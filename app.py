import streamlit as st
from huggingface_hub import InferenceClient
from io import BytesIO
import os

# Page configuration
st.set_page_config(page_title="AI Image Generator", layout="centered")
st.title("🎨 AI Image Generator (Stable Diffusion 3 Medium)")

# Load Hugging Face token (from secrets.toml or env var)
HF_TOKEN = st.secrets.get("HF_TOKEN", os.getenv("HF_TOKEN"))

if not HF_TOKEN:
    st.error("❌ Hugging Face token not found! Add it to `.streamlit/secrets.toml` or set it as an environment variable.")
    st.stop()

# Initialize client
client = InferenceClient("stabilityai/stable-diffusion-3-medium", token=HF_TOKEN)

# Prompt input
prompt = st.text_area("Enter your prompt:", placeholder="A futuristic city skyline at sunset with flying cars")

# Sidebar advanced options
st.sidebar.header("Advanced Settings")
num_inference_steps = st.sidebar.slider("Inference Steps", 10, 50, 28)
guidance_scale = st.sidebar.slider("Guidance Scale", 1.0, 20.0, 7.5)
image_width = st.sidebar.selectbox("Image Width", [512, 768, 1024])
image_height = st.sidebar.selectbox("Image Height", [512, 768, 1024])

# Generate button
if st.button("Generate Image"):
    if prompt.strip():
        with st.spinner("Generating your image..."):
            # Call Hugging Face Inference API
            image = client.text_to_image(
                prompt,
                guidance_scale=guidance_scale,
                num_inference_steps=num_inference_steps,
                width=image_width,
                height=image_height
            )

            # Show image
            st.image(image, caption="Generated Image", use_column_width=True)

            # Convert image to bytes
            buf = BytesIO()
            image.save(buf, format="PNG")
            byte_im = buf.getvalue()

            # Download button
            st.download_button(
                label="Download Image",
                data=byte_im,
                file_name="generated_image.png",
                mime="image/png"
            )
    else:
        st.warning("⚠️ Please enter a prompt before generating.")
