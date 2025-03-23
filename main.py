from fastapi import FastAPI, UploadFile, Form
import shutil
import requests

app = FastAPI()

AI_API_URL = "https://api.example.com/ai-edit"  # Replace with actual AI service

@app.post("/edit")
async def edit_image(image: UploadFile, keywords: str = Form(...)):
    file_path = f"temp/{image.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # Send to AI API (Example: DALL·E, Stable Diffusion)
    response = requests.post(AI_API_URL, files={"image": open(file_path, "rb")}, data={"keywords": keywords})
    return {"image_url": response.json().get("edited_image_url")}
