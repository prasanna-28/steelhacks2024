# PantherNotes

## Authors

Prasanna Pantha (ppantha@andrew.cmu.edu), Owen Lalis (olalis@andrew.cmu.edu), Tyler Jacobus (tjacobus@andrew.cmu.edu), Aaron HuSun (ahusun@andrew.cmu.edu)

## Table of Contents

- [About the Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)

## About the Project

PantherNotes revolutionizes the way students at the University of Pittsburgh engage with their study materials. By simply uploading your handwritten notes and specifying your course, the platform provides a suite of AI powered tools to enhance your learning journey:

1. **Elegant Notes Conversion**: Transforms your handwritten notes into a clean, professionally typeset PDF using LaTeX.

2. **Integrated Textbook Access**: Searches the University of Pittsburgh's PittAPI for the course's textbook and ISBN. It then locates the textbook (or a relevant alternative) in the public domain and directs you to the relevant  sections.

3. **Interactive Quizzes**: Generates quizzes based on your notes to test and reinforce your understanding of the material.

4. **Curated Video Content**: Provides multiple YouTube videos related to your topic for additional learning resources.

5. **AI-Powered Chatbot Assistance**: Enables you to ask questions about the material and receive answers from an intelligent chatbot.

### Built With

- [React.js](https://reactjs.org/) - Frontend library for building user interfaces
- [Flask](https://flask.palletsprojects.com/) - Lightweight backend framework
- [LaTeX](https://www.latex-project.org/) - High-quality typesetting system
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework
- [Google Generative AI](https://ai.google/) - Powers AI functionalities
- [YouTube Data API](https://developers.google.com/youtube/v3) - Retrieves relevant video content
- [PittAPI](https://pypi.org/project/pittapi/) - University of Pittsburgh's API

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- **Node.js and npm**
  - Install Node.js from [here](https://nodejs.org/).
  - Update npm to the latest version:
    ```
    npm install npm@latest -g
    ```
- **Python 3.10+**
  - Download Python from [here](https://www.python.org/downloads/).
- **pip**
  - Upgrade pip:
    ```
    pip install --upgrade pip
    ```
- **LaTeX distribution**
  - Install TeX Live (Linux/macOS) or MiKTeX (Windows).

### Installation

1. **Clone the repository**
2. **Navigate to the project directory**
3. **Install frontend dependencies**
```
cd frontend
npm install
```
4. **Install backend dependencies**
```
pip install -r requirements.txt
```
5. **Set up environment variables**
- Create a `.env` file in the `backend` directory with your API keys:
  ```
  GEMINI_API=your_gemini_api_key
  YOUTUBE_KEY=your_youtube_api_key
  ```
- Replace `your_gemini_api_key` and `your_youtube_api_key` with your actual API keys.

## Usage

1. **Start the Flask backend server**
```
cd backend
python app/routes.py
```
2. **Start the React frontend server**
```
cd frontend
npm start
```
3. **Access the application**
- Open your browser and navigate to `http://localhost:3000`.

## Features

- **Handwritten Notes Conversion**: Upload your handwritten notes in PDF format to receive a neatly formatted LaTeX PDF, enhancing readability and professionalism.
- **Textbook Integration**: Automatically finds and links to the relevant sections of your course's textbook, providing quick access to additional information.
- **Interactive Quizzes**: Generates custom quizzes based on your notes, allowing you to assess your understanding and identify areas for improvement.
- **Video Recommendations**: Offers a selection of YouTube videos tailored to your subject matter, supporting varied learning styles.
- **AI Chatbot Assistance**: Engage with an intelligent chatbot to ask questions and receive explanations, simulating a one-on-one tutoring experience.

## License

This project is licensed under the MIT License - see the `LICENSE.txt` file for details.
