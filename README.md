# Alpacaman
Alpacaman is an Alpaca-lora based Chatbot with infinite memory by finetune. 

![alt text](https://github.com/doxtor6/Alpacaman/blob/main/alpacaman_sg.jpg)

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
    cp gpt4-alpaca-lora-13b/* lora-alpcaman
   ```

3. Run the alpacaman.py
   The base model file should be download automatially.
   ```bash
   python alpacaman.py
   ```
