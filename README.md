# 🎯 Multimodal AI Meeting Intelligence System (Audio, Video & Text)

## 📌 Overview

The **Multimodal AI Meeting Intelligence System** is an end-to-end AI-powered application designed to transform raw meeting recordings (audio/video) into structured, actionable insights.

This system automatically converts speech into text, generates concise summaries, extracts action items, and enables intelligent interaction with meeting content.

It is built using modern NLP, Speech AI, and Transformer-based architectures to simulate real-world enterprise meeting analytics solutions.

---

## 🚀 Problem Statement

Meetings often contain critical information such as decisions, tasks, and deadlines, but:

* Important points are easily missed
* Manual note-taking is inefficient
* Tracking action items is difficult
* Revisiting past meetings is time-consuming

There is a need for an automated system that can convert meeting recordings into structured, searchable insights.

---

## 🎯 Objectives

* Convert audio/video meetings into text
* Generate concise and meaningful summaries
* Extract actionable tasks with context
* Enable semantic understanding of meeting content
* Provide an easy-to-use interface for users

---

## 🧠 Key Features

### ✅ Core Features (MVP)

* 🎥 Accepts **audio (.mp3, .wav) and video (.mp4)** inputs
* 🗣️ Speech-to-text conversion using Whisper
* 📝 Automatic meeting summarization using Transformer models

### 🔥 Advanced Features

* 📌 Action Item Extraction (who, what, deadline)
* 🧠 Named Entity Recognition (NER) for participants/tasks
* 🔍 Semantic search over meeting content
* 💬 Q&A over meetings (RAG-based system)

### ⭐ Additional Enhancements (Optional)

* Speaker identification
* Deadline detection
* Export summaries (PDF/Markdown)
* Highlight key sentences

---

## 🏗️ System Architecture

```
Audio/Video Input
        ↓
Audio Extraction (for video files)
        ↓
Speech-to-Text (Whisper)
        ↓
Text Preprocessing (spaCy/NLTK)
        ↓
Summarization (BART/T5 - Transformers)
        ↓
Action Item Extraction (Rules + NER)
        ↓
Semantic Layer (Sentence-BERT)
        ↓
Q&A System (FAISS - RAG)
        ↓
Frontend UI (Streamlit)
```

---

## 🛠️ Tech Stack

### 💻 Core Technologies

* **Python 3.x**

### 🧠 AI / NLP

* **OpenAI Whisper** – Speech-to-text
* **spaCy, NLTK** – Text preprocessing
* **Hugging Face Transformers (BART/T5)** – Summarization
* **Sentence-BERT** – Semantic embeddings
* **KeyBERT** – Keyword extraction

### 🔍 Retrieval & Search

* **FAISS** – Vector similarity search (RAG)

### 📊 Data Processing

* **Pandas, NumPy**

### 🌐 Frontend

* **Streamlit**

### ☁️ Deployment

* **GitHub**
* **Streamlit Community Cloud**

---

## 📂 Project Structure

```
ai-meeting-intelligence/
│
├── data/                # Input files (audio/video)
├── models/              # Model-related files
├── preprocessing/       # Text cleaning and processing
├── pipeline/            # Core pipeline logic
├── extraction/          # Action item extraction logic
├── embeddings/          # Semantic search & vector logic
├── ui/                  # Streamlit frontend
├── utils/               # Helper functions
│
├── app.py               # Main application entry point
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## 🧪 Development Approach

This project follows a **modular and incremental development strategy**:

### 🔹 Phase 1

* Audio/Video → Text conversion (Whisper)

### 🔹 Phase 2

* Text → Summary generation

### 🔹 Phase 3

* Action item extraction

### 🔹 Phase 4

* Frontend integration (Streamlit)

### 🔹 Phase 5

* Semantic search & Q&A (RAG)

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/NikhilMadiri/ai-meeting-intelligence.git
cd ai-meeting-intelligence
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
streamlit run app.py
```

---

## 📊 Expected Output

* 📄 Clean transcript of meeting
* 📝 Concise summary
* 📌 Extracted action items
* 🔍 Searchable meeting insights

---

## 🧾 Resume Description (Use This)

> Built a **Multimodal AI Meeting Intelligence System** that processes audio and video inputs to generate summaries, extract action items, and enable semantic search using NLP, Transformer models, and Speech AI.

---

## 🔥 Future Scope

* Real-time meeting processing
* Integration with Zoom/Google Meet
* Multi-language support
* Improved speaker diarization
* Cloud-based scalable deployment

---

## 👨‍💻 Author

Developed as part of an advanced AI/NLP project to simulate real-world enterprise systems.

---

## ⭐ Final Note

This project is designed not just as a model implementation, but as a **complete AI product**, following industry-level architecture, modular design, and deployment practices.
