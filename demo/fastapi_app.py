# fastapi_app.py

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import torch
from torchvision import transforms
from torchvision.models import resnet18
from PIL import Image
import io

app = FastAPI(title="Fruit Classifier", version="1.0")

# Load model & checkpoint
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
ckpt = torch.load("exported/resnet18_fruit_inference.pth", map_location=device)
classes = ckpt["classes"]

model = resnet18(num_classes=len(classes))
model.load_state_dict(ckpt["model_state_dict"])
model.eval().to(device)

# Preprocessing (must match training)
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToImage(),
    transforms.ToDtype(torch.float32, scale=True), 
    transforms.Normalize(mean=[0.485,0.456,0.406],
                         std=[0.229,0.224,0.225]),
])

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    try:
        img = Image.open(io.BytesIO(contents)).convert("RGB")
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image file")

    x = preprocess(img).unsqueeze(0).to(device)
    with torch.no_grad():
        logits = model(x)
        idx = torch.argmax(logits, dim=1).item()
        label = classes[idx]
        score = torch.softmax(logits, dim=1)[0, idx].item()

    return JSONResponse({
        "predicted_class": label,
        "confidence": f"{score:.4f}"
    })

# To run: uvicorn fastapi_app:app --host 0.0.0.0 --port 8000
# Or: uvicorn demo.fastapi_app:app --host 0.0.0.0 --port 8000