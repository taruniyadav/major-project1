#  Emotion Aware Intelligent Model (EAIM)



EAIM is an advanced **Adaptive Learning Platform** that leverages real-time emotional intelligence to personalize educational content. By analyzing facial expressions, voice, and text sentiment, the system dynamically adjusts its teaching style, quiz difficulty, and visual aids to match the student's emotional state and interests.

---

##  Key Features

- ** Multi-Modal Emotion Detection**: 
  - Real-time **Facial Expression Analysis** using DeepFace and OpenCV.
  - **Text Sentiment Analysis** to gauge student frustration, engagement, or depressive keywords.
  - **Voice Emotion Analysis** for a holistic view of the learner's state.
- ** Adaptive Engine**:
  - Powered by **Local Ollama (Qwen2:0.5b)** for generating personalized, empathetic responses and educational stories.
  - **Reinforcement Learning (Q-Learning)** for dynamic quiz difficulty adjustment based on student performance and emotion.
- ** Generative Visuals and Offline Assets**:
  - Contextual **Image Generation** using HuggingFace APIs to enhance learning with visual metaphors.
  - Fallbacks to offline local animations and assets to preserve the user experience without internet connectivity.
- **Admin & Student Dashboards**:
  - Student: Personalized learning paths, quiz history, and emotional progress tracking.
  - Admin: Deep metric visualization suite measuring student mental health risk factors (flags `is_depressed` states) and observing performance analytics.
- ** Interest Extraction**: 
  - Extracts user interests from Instagram data (ZIP/JSON) to tailor customized examples and learning analogies.

---

## 🛠️ Technology Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Emotion AI**: OpenCV, DeepFace, NLTK
- **LLM / Adaptive Logic**: Ollama (Qwen2:0.5b), Reinforcement Learning (Custom Q-Learning)
- **Database**: SQLite3 (schema covers sessions, quiz history, RL Q-Table)
- **Image Gen**: HuggingFace Inference API, Pollinations.ai
- **Visuals**: Plotly, Lottie

---

## 🚀Getting Started

### Prerequisites

- Python 3.9+
- [Ollama](https://ollama.ai/) installed and running locally with the `qwen2:0.5b` model (`ollama pull qwen2:0.5b`).
- Webcam and Microphone (for full emotion sensing).

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/emotion-adaptive-learning.git
   cd emotion-adaptive-learning
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the Database**:
   The database is automatically initialized on the first run of `app.py`.

### Running the App

```bash
streamlit run app.py
```

---

##  Project Structure

```text
.
├── adaptive/               # RL Agent and Adaptive LLM logic
├── emotion/                # Face, Text, and Voice emotion sensing
├── database/               # Database management (SQLite)
├── pages/                  # Streamlit pages (Admin Dash, Learning, Quiz, Story)
├── assets/                 # Static assets and offline Lottie animations
├── project_overview.md     # In-depth Workflows and Data Layer Logic
├── system_architecture_design.md # High-level Architecture & Diagrams
├── requirements.txt        # Python dependencies
└── app.py                  # Main entry point (Login/Navigation/Routing)
```

---

##  Architecture

For a deep dive into the system architecture, sequence diagrams, and database schema, please refer to the **[System Architecture Design](system_architecture_design.md)** and **[Project Overview](project_overview.md)**.

---


