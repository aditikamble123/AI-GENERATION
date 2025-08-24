import streamlit as st
import requests
import os
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="Stable Diffusion Generator", layout="centered")
st.title("🎨 AI Image Generator (Stability API)")

API_KEY = st.secrets.get("STABILITY_API_KEY", os.getenv("STABILITY_API_KEY"))

if not API_KEY:
    st.error("❌ API key not found! Add it in `.streamlit/secrets.toml` or environment variables.")
    st.stop()

prompt = st.text_area("Enter your prompt:", placeholder="A futuristic city skyline at sunset with flying cars")

if st.button("Generate Image"):
    if prompt.strip():
        with st.spinner("Generating..."):
            response = requests.post(
                "https://api.stability.ai/v1/generation/stable-diffusion-v1-5/text-to-image",
                headers={
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "text_prompts": [{"text": prompt}],
                    "cfg_scale": 7,
                    "clip_guidance_preset": "FAST_BLUE",
                    "height": 512,
                    "width": 512,
                    "samples": 1,
                    "steps": 30,
                },
            )

            if response.status_code == 200:
                data = response.json()
                image_base64 = data["artifacts"][0]["base64"]
                image = Image.open(BytesIO(base64.b64decode(image_base64)))

                st.image(image, caption="Generated Image", use_column_width=True)

                buf = BytesIO()
                image.save(buf, format="PNG")
                st.download_button(
                    label="Download Image",
                    data=buf.getvalue(),
                    file_name="generated_image.png",
                    mime="image/png"
                )
            else:
                st.error(f"Error: {response.text}")
    else:
        st.warning("⚠️ Please enter a prompt first.")
