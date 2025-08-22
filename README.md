# 🍎🍌 Fruit Classifier

A compact deep learning project for training and deploying a fruit image classifier.  
Trained in PyTorch, evaluated with scikit-learn, and deployed as a web app on **Google Cloud Run**.

---

## ✨ Features
- 📓 End-to-end Jupyter notebook (`fruit_classifier.ipynb`) for training and evaluation  
- 🔬 Confusion matrix & per-class metrics automatically saved to `/images`  
- 🌐 Deployed demo running on **Google Cloud Run**  
- 📦 Reproducible environments with `environment.yml` (Conda) and `requirements.txt` (pip)  
- ⚙️ CI/CD starter pipeline (`cloudbuild.yaml`)  

---

## 🚀 Live Demo
👉 Try the app here:  
**[Fruit Classifier App](https://fruit-classifier-98929583247.europe-west1.run.app)**  

Upload an image of a fruit and get the predicted class in real time. 🍏🍊🍓  

---

## 🗂️ Repository Structure

├── fruit_classifier.ipynb # Main training notebook
├── requirements.txt # pip dependencies
├── environment.yml # conda environment
├── cloudbuild.yaml # optional CI/CD config
├── demo/ # (optional) demo app files
├── images/ # confusion matrices, reports, sample outputs
└── references/ # papers, notes, links

---

## ⚡ Quickstart (Training Locally)

### 1. Clone
```bash
git clone https://github.com/minealsan/fruit_classifier.git
cd fruit_classifier


2. Set up environment

Conda (recommended):
```bash
conda env create -f environment.yml
conda activate fruit-classifier

3. Train
```bash
jupyter lab
# open fruit_classifier.ipynb and run all cells
