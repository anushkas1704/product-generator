

# 🛍️ AI Product Description & Image Generator  

This project is a simple **AI-powered tool** that allows users to:  
- Generate **detailed product descriptions** using **Google Gemini API**  
- Generate **product images** using **Hugging Face FLUX.1-schnell API**  
- Interact with everything via a **Streamlit frontend**  

---

## 🚀 Features  
- Enter a product name/idea and instantly get:  
  ✅ A professional AI-generated product description  
  ✅ A realistic AI-generated product image  
- Clean and interactive UI built with **Streamlit**  
- Free image generation via Hugging Face Inference API  
- Easy to set up and run locally  

---

## 🛠️ Tech Stack  
- **Frontend/UI:** [Streamlit](https://streamlit.io/)  
- **Text Generation (Description):** Google Gemini API (`gemini-pro`)  
- **Image Generation:** Hugging Face FLUX.1-schnell (`black-forest-labs/FLUX.1-schnell`)  

---

## 📂 Project Structure  
```

├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
├── .env                  # API keys (not committed to GitHub)
└── README.md             # Project documentation

````

---

## 🔑 Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/ai-product-generator.git
cd ai-product-generator
````

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add API Keys

Create a `.env` file in the root folder and add your keys:

```env
GEMINI_API_KEY=your_gemini_api_key_here
HF_API_KEY=your_huggingface_api_key_here
```

👉 You can get keys here:

* [Google Gemini API Key](https://aistudio.google.com/app/apikey)
* [Hugging Face API Key](https://huggingface.co/settings/tokens)

⚠️ Note: Make sure your Hugging Face token has **Inference permissions**.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open the local URL (usually `http://localhost:8501/`) in your browser.

---

## 📸 Example Workflow

1. Enter: **"Eco-friendly Water Bottle for Travelers"**
2. The app generates:

   * A professional product description (via Gemini)
   * A product image (via Stable Diffusion)
3. Both are displayed side-by-side in the Streamlit UI.

---



