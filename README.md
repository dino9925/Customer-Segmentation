# 📊 Intelligent Customer Segmentation & Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-FF4B4B.svg)
![Plotly](https://img.shields.io/badge/Plotly-Dash-3F4F75.svg)
![Gemini AI](https://img.shields.io/badge/Google%20Gemini-1.5%20Flash-8E75B2.svg)

## 📖 Overview

The **Intelligent Customer Segmentation & Analytics Dashboard** is a comprehensive B2C analytics platform designed to empower businesses with deep insights into customer behavior.

Built with **Python** and **Streamlit**, this application offers a secure environment to visualize key market trends, demographic distributions, and spending habits using interactive **Plotly** charts. It goes beyond traditional analytics by integrating **Google Gemini AI**, providing a natural language chatbot that allows stakeholders to "talk" to their data and receive instant, context-aware answers.

## ✨ Key Features

-   **🔐 Secure Authentication**: Robust Login and Sign-Up system to protect sensitive business data.
-   **📈 Dynamic Dashboard**: Interactive overview of store performance and key metrics.
-   **📊 Advanced Analytics**:
    -   **Age vs. Spending Score**: Understand how different age groups spend.
    -   **Gender Distribution**: Analyze spending habits by gender.
    -   **Income vs. Spending**: Scatter plots to identify high-value customer segments.
    -   **Demographic Histograms**: Visual distribution of customer ages.
-   **🤖 AI-Powered Chatbot**: Integrated **Google Gemini 1.5 Flash** allows users to ask questions like *"What is the average spending score of customers under 30?"* and get immediate answers.
-   **📂 Data Management**: View and explore processed datasets ("Mall Customers" and "Customer Data") directly within the UI.
-   **📥 Export Options**: Capabilities to export reports and insights (Future Scope).

## 🛠️ Tech Stack

-   **Frontend & Framework**: [Streamlit](https://streamlit.io/)
-   **Data Manipulation**: [Pandas](https://pandas.pydata.org/), [Dask](https://www.dask.org/)
-   **Visualization**: [Plotly Express](https://plotly.com/python/plotly-express/), [Matplotlib](https://matplotlib.org/)
-   **Generative AI**: [Google Generative AI (Gemini)](https://ai.google.dev/)
-   **Authentication**: Custom session-state management utilizing CSV backend.
-   **Utilities**: `fpdf` for reporting, `smtplib` for communications.

## 🚀 Installation & Setup

Follow these steps to get the project running on your local machine.

### Prerequisites

-   Python 3.8 or higher
-   pip (Python package manager)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies

Create a `requirements.txt` file or install directly:

```bash
pip install streamlit streamlit-option-menu pandas plotly matplotlib fpdf google-generativeai dask
```

### 3. Configure Secrets

Create a `.streamlit/secrets.toml` file in the project root directory to store your API keys securely:

```toml
# .streamlit/secrets.toml
GOOGLE_API_KEY = "your_google_gemini_api_key_here"
```

### 4. Run the Application

```bash
streamlit run sample.py
```

## 💡 Usage

1.  **Log In / Sign Up**: Create an account or log in to access the dashboard.
2.  **Navigate**: Use the sidebar to switch between Dashboard, Projects, Datasets, Analytics, and Chatbot.
3.  **Analyze**: Explore the interactive charts in the **Analytics** tab.
4.  **Chat with AI**: Go to the **Chatbot** tab, select a dataset, and ask questions in plain English.
5.  **Logout**: Securely end your session via the Logout option.

## 📂 Project Structure

```
├── sample.py                # Main application entry point
├── Mall_Customers.csv       # Dataset 1
├── Customer Data.csv        # Dataset 2
├── users.csv                # User credentials store
├── README.md                # Project documentation
└── .streamlit/
    └── secrets.toml         # API keys (not committed to repo)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

*Developed by Dhruv*
