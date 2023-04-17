# Alpacaman
Alpacaman is an Alpaca-lora based Chatbot with infinite memory by finetune. 

![alt text](https://github.com/doxtor6/Alpacaman/blob/main/alpacaman_sg.jpg)

### Intro

In the majority of large language models (LLMs), the input token limit imposes significant constraints on potential applications. This limitation, often referred to as memory restriction, has emerged as a critical issue. Various methods have been proposed to address this problem. For instance, Langchain has been widely employed to augment the memory capacity of LLMs using a vector database. However, this approach serves only as a temporary enhancement rather than a definitive solution.

Alpacaman offers a potential comprehensive resolution by fine-tuning the memory within the Lora layer of the LLM, theoretically allowing for unlimited memory storage. Although one primary drawback of this method is the risk of memory loss during the fine-tuning process, the approach still presents a noticeable advantage in terms of long-term memory retention.

Here is a process flow diagram of alpacaman:

![alt text](https://github.com/doxtor6/Alpacaman/blob/main/process.jpg)


### Setup

1. Install dependencies (The same as [tloen/alpaca-lora](https://github.com/tloen/alpaca-lora/))

   ```bash
   pip install -r requirements.txt
   ```
2. Download Weight files.
   Here we are using the 13B LLAMA as base model('decapoda-research/llama-13b-hf'), thus we need lora weights for 13B. Here I recommend [chansung/gpt4-alpaca-lora-13b](https://huggingface.co/chansung/gpt4-alpaca-lora-13b)
   
   

   ```bash
    conda install git-lfs
    git-lfs install
    git clone https://huggingface.co/chansung/gpt4-alpaca-lora-13b
    cp gpt4-alpaca-lora-13b/* lora-alpacaman
   ```

3. Run the alpacaman.py
   The base model file should be download automatially.
   ```bash
   python alpacaman.py
   ```
If you meet unexpected error when loading base model, check your cuda version first.
