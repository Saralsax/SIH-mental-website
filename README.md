# MindCare Connect – Comprehensive Mental Health & Wellness Platform

Welcome to **MindCare Connect**, a modern web application designed to support mental health and wellness for students, professionals, families, and seniors. This platform integrates mental health screening tools, counselor booking, real-time chat support, and curated wellness resources, all powered by intuitive HTML/CSS/JS frontends and FastAPI backends.

---

## Features

### 🧠 Mental Health Screening
- **PHQ-9 Depression Test** & **GAD-7 Anxiety Test**: Complete confidential screenings with instant results.
- **Progress Tracking**: Visual progress bar and severity color-coding.
- **Responsive, accessible UI** built in React (see [`App.jsx`](./App.jsx), [`ScreeningPage.jsx`](./ScreeningPage.jsx)).

### 👩‍⚕️ Counselor Booking API
- **Find Counselors** by specialty (Academic Stress, Anxiety, Trauma, etc.)
- **Book Appointments** with available slots.
- **CSV-powered data** for demo & scalability ([`CBA.py`](./CBA.py), [`counselors.csv`](./counselors.csv)).
- **Frontend booking page** ([`CBPage.html`](./CBPage.html)) with specialty selection and live slot display.

### 💬 Chatbot (AI Assistant)
- **Real-time chat** for user queries and mental health support ([`app.py`](./app.py), [`Chatbot.html`](./templates/Chatbot.html)).
- **Ollama/LLM integration** for natural language responses.
- **Floating chat widget** for easy access.

### 🏥 Health & Wellness Portal
- **Homepage** ([`index.html`](./index.html)) with navigation, hero section, journey steps, covered groups, shop, and wellness programs.
- **Virtual Assistant** button and feedback carousel.
- **Modern, mobile-friendly design** with custom styles ([`style.css`](./style.css), [`ScreeningModule.css`](./ScreeningModule.css), [`index.css`](./index.css)).

---

## Getting Started

### Prerequisites
- **Node.js** (for React frontend)
- **Python 3.8+** (for FastAPI backends)
- **Ollama** (for chatbot; see [Ollama](https://ollama.com/) setup)
- **npm/yarn** and **pip** for package management

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Saralsax/SIH-mental-website.git
   cd SIH-mental-website
   ```

2. **Install Frontend Dependencies**
   ```bash
   npm install
   # or
   yarn install
   ```

3. **Install Backend Dependencies**
   ```bash
   pip install fastapi uvicorn pydantic
   ```

4. **Run React Frontend**
   ```bash
   npm start
   # or
   yarn start
   ```

5. **Run FastAPI Backends**
   ```bash
   # For Chatbot
   uvicorn app:app --reload
   # For Counselor Booking API
   uvicorn CBA:app --reload
   ```

---

## Usage

- **Home Page:** Access `index.html` for main navigation and wellness information.
- **Screening:** Use `/screening` (React) for PHQ-9 and GAD-7 self-assessments.
- **Consult Online:** Visit `CBPage.html` to find and book counselors.
- **Chatbot:** Floating chat button or access `/` for the AI assistant.

---

## Project Structure

```
├── index.html                # Main homepage
├── CBPage.html               # Counselor booking page
├── Chatbot.html              # Chatbot UI (served via FastAPI)
├── style.css                 # Styles for chatbot widget
├── counselors.csv            # Demo counselor data
├── app.py                    # FastAPI backend for chatbot
├── CBA.py                    # FastAPI backend for counselor booking
├── App.jsx / main.jsx        # React mental health screening app
├── ScreeningPage.jsx         # Unified screening page
├── PHQ9Module.jsx / GAD7Module.jsx # Screening logic & UI
├── index.css / ScreeningModule.css # Additional global/module 
Screening
├──Node.js(React) Setup       # Screening Purpose
```

---

## Technologies Used

- **React** (Frontend SPA)
- **HTML/CSS/JS** (Landing pages, widgets)
- **FastAPI** (REST APIs for booking, chat)
- **Ollama/LLM** (Chatbot backend)
- **Jinja2 Templates** (Server-side rendering)
- **CSV** (Counselor demo database)

---

## Customization

- **Counselor Data:** Update `counselors.csv` for more counselors/specialties.
- **Styling:** Tweak `style.css`, `ScreeningModule.css`, or `index.css` for branding.
- **Screenings:** Add new modules following the PHQ9/GAD7 pattern.
- **Chatbot Model:** Change Ollama/LLM model in `app.py` as needed.

---

## License

[MIT](LICENSE)

---

## Authors & Acknowledgements

- Developed by **SIH Team** (Shubham, Priyansh, Deviyansh, Lakshyavardhan, Saral, Khushi and contributors)
- Special thanks to mental health professionals and open-source communities.

---

## Disclaimer

This application is for informational and screening purposes only. It is **not** a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified health professional for mental health concerns.

---

## References

- [PHQ-9 & GAD-7 Screeners](https://www.phqscreeners.com)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Ollama LLM](https://ollama.com/)
