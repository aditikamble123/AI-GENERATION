
# 🎨 AI Image Generator (Stable Diffusion 3 + Streamlit)

An interactive **AI image generator** built with **Streamlit** and **Stability AI’s Stable Diffusion 3 (SD3)** API.  
Turn your **text prompts** into stunning AI-generated images — with support for custom resolution, formats, and easy downloads.

---

## 🚀 Features
- 📝 Generate images from **text prompts**  
- ⚙️ Adjust **width, height, and output format** (JPEG, PNG, WebP)  
- 💾 One-click **download button**  
- 🔑 Secure API key handling with **Streamlit Secrets Manager**  
- 🌐 Ready to deploy on **Streamlit Cloud** or **Hugging Face Spaces**

---

## 🛠️ Tech Stack
- [Streamlit](https://streamlit.io/) – Web app framework  
- [Stability AI API](https://platform.stability.ai/) – Stable Diffusion 3 model  
- [Pillow (PIL)](https://python-pillow.org/) – Image handling  
- [Requests](https://docs.python-requests.org/) – API communication  

---

## 📂 Project Structure
```

.
├── app.py                 # Main Streamlit app
├── requirements.txt       # Dependencies
└── .streamlit/
└── secrets.toml       # Store your API key (not committed)

````

## 📸 Screenshots
<img width="1920" height="866" alt="Screenshot (543)" src="https://github.com/user-attachments/assets/68e39088-3681-4a4b-87c1-eb7645e124d4" />
<img width="1920" height="843" alt="Screenshot (542)" src="https://github.com/user-attachments/assets/3c2566b9-3e69-420f-88d3-d83d758acce1" />

## ✨ Example Prompts

* `A futuristic city skyline at sunset with flying cars, ultra realistic, 8K`
* `Cute anime-style cat wearing astronaut suit, floating on Mars`
* `A fantasy castle in the sky, highly detailed, concept art`

```
