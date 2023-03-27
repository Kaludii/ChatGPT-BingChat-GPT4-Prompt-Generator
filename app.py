import streamlit as st
import random
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Kaludi/chatgpt-gpt4-prompts-bart-large-cnn-samsum")
model = AutoModelForSeq2SeqLM.from_pretrained("Kaludi/chatgpt-gpt4-prompts-bart-large-cnn-samsum", from_tf=True)

def generate(prompt, max_new_tokens):
    batch = tokenizer(prompt, return_tensors="pt")
    generated_ids = model.generate(batch["input_ids"], max_new_tokens=max_new_tokens)
    output = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    return output[0]

st.title("ChatGPT-BingChat Prompt Generator")
st.write("This app generates ChatGPT/BingChat & GPT-3 prompts using [this](https://huggingface.co/Kaludi/chatgpt-gpt4-prompts-bart-large-cnn-samsum) model trained by [Kaludi](https://huggingface.co/Kaludi/). Enter a role and a prompt will be generated based on it.")
prompt = st.text_input("Enter a Role, Example: Virtual Assistant", placeholder="Text here", value="")
max_new_tokens = st.slider("Select Max Tokens in Response", min_value=100, max_value=500, value=150, step=10)
if st.button("Generate"):
    output = generate(prompt, max_new_tokens)
    st.write("Generated Prompt:", box=True)
    st.write("<div style='background-color: #2E2E2E; padding: 10px;'>{}</div>".format(output), unsafe_allow_html=True)
st.write("")
st.write("<div style='text-align: center; font-weight: bold;'>Examples:</div>",unsafe_allow_html=True, box=True)
st.write("<style> .stBox span { background-color: #2E2E2E; } </style>", unsafe_allow_html=True)
with open("examples.txt", "r") as f:
    examples = f.readlines()
    random_examples = random.sample(examples, 5)
    for example in random_examples:
        example = example.strip()
        st.write("<div style='background-color: #2E2E2E; padding: 10px; text-align: center;'>• {}</div>".format(example), unsafe_allow_html=True)
