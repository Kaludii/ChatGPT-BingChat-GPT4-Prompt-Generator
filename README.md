
# ChatGPT-BingChat Prompt Generator

Generates ChatGPT/BingChat & GPT-3 prompts using [this](https://huggingface.co/Kaludi/chatgpt-gpt4-prompts-bart-large-cnn-samsum) model trained by [Kaludi](https://huggingface.co/Kaludi).

Enter a role and a prompt will be generated based on it.

# Web App
Click [Here](https://huggingface.co/spaces/Kaludi/ChatGPT-BingChat-GPT3-Prompt-Generator_App "Here") To View This App Online!

![image](https://user-images.githubusercontent.com/63890666/228079348-9df040ad-4068-4542-a9ad-319cb6717ccb.png)

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

The app uses Streamlit for the user interface and the Hugging Face Transformers and is a fine-tuned version of [philschmid/bart-large-cnn-samsum's](https://huggingface.co/philschmid/bart-large-cnn-samsum) model using [this](https://huggingface.co/datasets/fka/awesome-chatgpt-prompts) dataset. 

It achieves the following results on the evaluation set:
- Train Loss: 1.2214
- Validation Loss: 2.7584
- Epoch: 4

### Training hyperparameters

The following hyperparameters were used during training:
- optimizer: {'name': 'AdamWeightDecay', 'learning_rate': 2e-05, 'decay': 0.0, 'beta_1': 0.9, 'beta_2': 0.999, 'epsilon': 1e-07, 'amsgrad': False, 'weight_decay_rate': 0.01}
- training_precision: float32

### Training results

| Train Loss | Validation Loss | Epoch |
|:----------:|:---------------:|:-----:|
| 3.1982     | 2.6801          | 0     |
| 2.3601     | 2.5493          | 1     |
| 1.9225     | 2.5377          | 2     |
| 1.5465     | 2.6794          | 3     |
| 1.2214     | 2.7584          | 4     |

## Requirements

-   Python 3.6 or higher
-   Streamlit
-   Transformers (Hugging Face)

## Installation

1.  Clone the repository:

`git clone https://github.com/Kaludii/ChatGPT-BingChat-GPT3-Prompt-Generator.git` 

2.  Install the required packages:

`pip install streamlit transformers` 

3.  Run the app:

`streamlit run app.py`
