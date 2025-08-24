import streamlit as st
import requests
from io import BytesIO
from PIL import Image
import os

# Page config
st.set_page_config(page_title="Stable Diffusion 3 Generator", layout="centered")
st.title("🎨 AI Image Generator (Stability AI - SD3)")

# Load API key
API_KEY = st.secrets.get("STABILITY_API_KEY", os.getenv("STABILITY_API_KEY"))

if not API_KEY:
    st.error("❌ Stability API key not found! Please add it in `.streamlit/secrets.toml` or environment variables.")
    st.stop()

# Prompt input
prompt = st.text_area("Enter your prompt:", placeholder="Lighthouse on a cliff overlooking the ocean")

# Sidebar settings
st.sidebar.header("Advanced Settings")
output_format = st.sidebar.selectbox("Output Format", ["jpeg", "png", "webp"])
image_width = st.sidebar.selectbox("Image Width", [512, 768, 1024])
image_height = st.sidebar.selectbox("Image Height", [512, 768, 1024])

# Generate button
if st.button("Generate Image"):
    if prompt.strip():
        with st.spinner("Generating your image..."):
            response = requests.post(
                "https://api.stability.ai/v2beta/stable-image/generate/sd3",
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Accept": "image/*"
                },
                files={"none": ''},  # required placeholder
                data={
                    "prompt": prompt,
                    "output_format": output_format,
                    "width": image_width,
                    "height": image_height,
                },
            )

            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))

                # Show image
                st.image(image, caption="Generated Image", use_column_width=True)

                # Save image in memory for download
                buf = BytesIO()
                image.save(buf, format=output_format.upper())
                byte_im = buf.getvalue()

                # Download button
                st.download_button(
                    label="Download Image",
                    data=byte_im,
                    file_name=f"generated_image.{output_format}",
                    mime=f"image/{output_format}"
                )
            else:
                st.error(f"❌ Error {response.status_code}: {response.text}")
    else:
        st.warning("⚠️ Please enter a prompt before generating.")
