# LinkedIn Job Matcher

## 📌 Overview

This Python script evaluates LinkedIn candidate profiles against job offers using OpenAI's GPT-4o-mini. It extracts textual content from job listings and candidate profiles, then generates an analysis highlighting strengths, gaps, and a suitability score.

## ✨ Features

- **Web Scraping**: Extracts job descriptions and candidate details from LinkedIn.
- **AI-Powered Evaluation**: Compares job requirements with candidate experience.
- **Strengths & Gaps Identification**: Lists matches and missing qualifications.
- **Suitability Score**: Rates candidate fit out of 10.

## 📂 Installation

### 1️⃣ Clone the Repository

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

### 3️⃣ Install Dependencies

### 4️⃣ Set Up Environment Variables

Create a `.env` file and add your OpenAI API key:

## 🚀 Usage

Run the script and input LinkedIn job and candidate profile URLs when prompted.

⚠️ **Note:** LinkedIn has anti-scraping measures that may block some requests, causing the script to fail on certain profiles.

## 🛠 Dependencies

- `openai`
- `beautifulsoup4`
- `requests`
- `python-dotenv`

Install them using:

```bash
pip install -r requirements.txt
```
## 📜 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 👤 Contact

Developed by [David Ruiz Casares](https://www.linkedin.com/in/david-ruiz-casares/).