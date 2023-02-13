
# ChatGPT-BingChat Prompt Generator

Generates ChatGPT/BingChat & GPT-3 prompts using [this](https://huggingface.co/merve/chatgpt-prompts-bart-long) model trained by Merve.

Enter a role and a prompt will be generated based on it.

# Web App
Click [Here](edit "Here") To View This App Online!

![Image](Image)

## Features

-   Generate prompts based on a role entered by the user
-   Uses a pre-trained language model to generate the prompt

## Usage

To use the app, simply enter a role in the input field and click on the "Generate" button. A prompt will be generated based on the role entered.

## Examples

Some examples of roles that can be entered:

-   Virtual Assistant
-   Customer Service Representative
-   Personal Assistant
-   Data Scientist

## Technical details

The app uses Streamlit for the user interface and the Hugging Face Transformers library to access the pre-trained language model. The model is a seq2seq language model trained using the BART architecture.

## Requirements

-   Python 3.6 or higher
-   Streamlit
-   Transformers (Hugging Face)

## Installation

1.  Clone the repository:

`git clone https://github.com/Kaludii/ChatGPT-BingChat-Prompt-Generator.git` 

2.  Install the required packages:

`pip install streamlit transformers` 

3.  Run the app:

`streamlit run app.py`