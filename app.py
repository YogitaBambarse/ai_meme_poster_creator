import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="AI Meme & Poster Creator", layout="centered")

st.title("🎨 AI Meme & Poster Creator")
st.write("Create posters and memes easily using AI-powered captions")

# -----------------------------
# User Inputs
# -----------------------------
content_type = st.selectbox("Select Content Type", ["Poster", "Meme"])
event_name = st.text_input("Enter Event / Topic Name")
tone = st.selectbox("Select Tone", ["Fun", "Professional"])

# -----------------------------
# AI Caption Generator (Logic)
# -----------------------------
def generate_caption(event, tone):
    if tone == "Fun":
        return f"🔥 Get ready for {event}! 😄🎉"
    else:
        return f"Join us for {event}. Let's innovate together."

# -----------------------------
# Generate Button
# -----------------------------
if st.button("Generate"):
    if event_name == "":
        st.warning("Please enter event or topic name")
    else:
        caption = generate_caption(event_name, tone)

        # Load Template
        if content_type == "Poster":
            template_path = "templates/poster1.png"
        else:
            template_path = "templates/meme1.jpg"

        if not os.path.exists(template_path):
            st.error("Template image not found!")
        else:
            img = Image.open(template_path)
            draw = ImageDraw.Draw(img)

            # Font
            try:
                font = ImageFont.truetype("assets/fonts/arial.ttf", 40)
            except:
                font = ImageFont.load_default()

            # Text Position
            text_x = 50
            text_y = img.height - 100

            # Draw Text
            draw.text((text_x, text_y), caption, fill="black", font=font)

            # Save Output
            output_path = "output.png"
            img.save(output_path)

            # Display Result
            st.success("🎉 Your design is ready!")
            st.image(output_path, use_column_width=True)

            # Download Button
            with open(output_path, "rb") as file:
                st.download_button(
                    label="⬇️ Download Image",
                    data=file,
                    file_name="ai_meme_poster.png",
                    mime="image/png"
                )
