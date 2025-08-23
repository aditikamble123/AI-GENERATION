import streamlit as st
import replicate
import requests
from io import BytesIO

# Page configuration
st.set_page_config(page_title="AI Image Generator", layout="centered")

st.title("🎨 AI Image Generator (Fast & GPU Powered)")

# Read API token from secrets
REPLICATE_API_TOKEN = st.secrets["REPLICATE_API_TOKEN"]

# Set token for replicate
import os
os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN

# Prompt input
prompt = st.text_area("Enter your prompt:", placeholder="A futuristic city skyline at sunset with flying cars")

# Additional options (optional)
st.sidebar.header("Advanced Settings")
num_inference_steps = st.sidebar.slider("Inference Steps", 20, 50, 30)
guidance_scale = st.sidebar.slider("Guidance Scale", 1.0, 20.0, 7.5)
image_width = st.sidebar.selectbox("Image Width", [512, 768])
image_height = st.sidebar.selectbox("Image Height", [512, 768])

# Generate button
if st.button("Generate Image"):
    if prompt.strip():
        with st.spinner("Generating your image..."):
            # Call Replicate API
            output = replicate.run(
                "stability-ai/stable-diffusion:db21e45c0a6b0ed052d10a5a0a0f8cfbdbf59e586d2fdb8e7e70f0e2e5c6a6c4",
                input={
                    "prompt": prompt,
                    "image_dimensions": f"{image_width}x{image_height}",
                    "num_inference_steps": num_inference_steps,
                    "guidance_scale": guidance_scale
                }
            )

            # Replicate returns a list of URLs
            image_url = output[0]

            # Display image
            st.image(image_url, caption="Generated Image", use_column_width=True)

            # Download button
            img_data = requests.get(image_url).content
            st.download_button(
                label="Download Image",
                data=img_data,
                file_name="generated_image.png",
                mime="image/png"
            )
    else:
        st.warning("Please enter a prompt before generating.")
