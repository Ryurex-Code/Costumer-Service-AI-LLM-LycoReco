# Café LycoReco - AI-Powered Customer Service

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Background and Name Reference

This project is inspired by the popular anime "Lycoris Recoil". The name "Café LycoReco" is taken from the name of the café where the main characters work and interact. Just like the café offers various services in the anime, this project aims to provide interactive and informative customer service through an AI-powered chatbot.

## Technologies Used

This project is built using the following technologies:

* **Gradio:** A Python framework that allows for the rapid creation of web-based user interfaces for machine learning models.
* **Groq:** A platform providing access to high-performance large language models (LLMs), in this project utilizing the `llama3-8b-8192` model.
* **Python:** The primary programming language used for development.
* **dotenv:** A Python library to load environment variables from a `.env` file.

## How to Use

Here are the steps to run this customer service application:

1.  **Prerequisites:**
    * Ensure you have **Python** installed on your system.
    * Install `pip` (Python package installer) if it's not already installed.

2.  **Clone the Repository (optional):**
    If this code is in a GitHub repository, you can clone it using the command:
    ```bash
    git clone <repository_URL>
    cd <repository_name>
    ```

3.  **Install Dependencies:**
    Make sure you have installed all the necessary libraries. You can do this by running the following command in your terminal or command prompt:
    ```bash
    pip install gradio groq python-dotenv
    ```

4.  **Configure API Key:**
    * Create a file named `.env` in your project directory.
    * Add your Groq API key to the `.env` file in the following format:
        ```
        GROQ_API_KEY=YOUR_GROQ_API_KEY_HERE
        ```
        Make sure to replace `YOUR_GROQ_API_KEY_HERE` with your actual Groq API key.

5.  **Configure System Prompt (optional):**
    * Ensure you have a file named `prompt.txt` in your project directory.
    * This file contains the system prompt that will guide the chatbot's behavior. You can modify the contents of this file according to your needs.

6.  **Run the Application:**
    Open your terminal or command prompt, navigate to your project directory, and run the following command:
    ```bash
    python <your_python_script_file_name>.py
    ```
    (Replace `<your_python_script_file_name>.py` with the name of your Python script file, for example, `app.py`).

7.  **Access the Interface:**
    Once the application runs successfully, Gradio will provide a local URL (usually starting with `http://localhost:` followed by a port number). Open this URL in your web browser to access the Café LycoReco customer service interface.

8.  **Interact with the Chatbot:**
    On the web interface, you can type your messages in the provided field, and the chatbot will respond based on the system prompt and the `llama3-8b-8192` model from Groq.

## Important Notes

* Keep your Groq API key secure and do not share it publicly.
* The system prompt in the `prompt.txt` file plays a crucial role in determining how the chatbot responds. Experiment with different prompts to achieve optimal results.
* Parameters like `temperature`, `max_tokens`, and `top_p` in the `chatbot_response` function can be adjusted to control the chatbot's creativity and response length.
* This application runs locally on your computer unless you specifically deploy it to a web hosting platform.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Contribution

If you are interested in contributing to this project, feel free to submit pull requests or create issues in the GitHub repository.

## Author

Ryurex Corporation
