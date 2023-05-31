#!/bin/bash

# NOTE: This is a script for installing the dependencies for the Alpaca LoRa project. 
#       It is not meant to be run as a script, but rather to be used as a reference
#       for installing the dependencies on your own machine.

# Update package lists
sudo apt-get update && sudo apt-get upgrade -y

wget https://developer.download.nvidia.com/compute/cuda/12.1.1/local_installers/cuda_12.1.1_530.30.02_linux.run
sudo sh cuda_12.1.1_530.30.02_linux.run
make LLAMA_CUBLAS=1

# set GGML_CUDA_MAX_STREAMS in ggml-cuda.cu to 1 for reproducability

# Install required software
sudo apt-get install -y git curl software-properties-common

# Add Python PPA and install Python 3.10
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt install -y python3.10

# Clean up package lists
sudo rm -rf /var/lib/apt/lists/*

# Set Python 3.10 as default Python version
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1

# Use a virtual environment if there are errors
#python -m venv venv --without-pip
#source venv/bin/activate

# Install pip and Python dependencies
curl -sS https://bootstrap.pypa.io/get-pip.py | python
python -m pip install -r requirements.txt
python -m pip install numpy --pre torch==2.0.0+cu118 torchvision==0.15.1+cu118 --force-reinstall --extra-index-url https://download.pytorch.org/whl/cu118

# You may need to install ipykernel if you are using Jupyter Notebook:
#python -m pip install ipykernel
#python -m ipykernel install --user --name=alpaca-lora 




# If you have more files to copy, do so here
#cp -r path/to/your/files .

# You may need to ensure that the CUDA version is correct:
#sudo ls /usr/lib/x86_64-linux-gnu/libcudart.so* # Check the current versions of cuda
#sudo rm /usr/lib/x86_64-linux-gnu/libcudart.so # Remove the current lubcudart.so to the current version of cuda
#sudo ln -s /usr/lib/x86_64-linux-gnu/libcudart.so.11.8.89 /usr/lib/x86_64-linux-gnu/libcudart.so # Set the lubcudart.so to the current version of cuda
#export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH # Make sure it is added to path



#sudo ls /venv/lib/python3.10/site-packages/bitsandbytes/libbitsandbytes_cuda.so* # Check the current versions of cuda
#sudo rm /usr/lib/x86_64-linux-gnu/libcudart.so # Remove the current lubcudart.so to the current version of cuda
export CUDA_VISIBLE_DEVICES=0
# Entrypoint
python finetune.py --base_model 'decapoda-research/llama-7b-hf' --data_path 'yahma/alpaca-cleaned' --output_dir './lora-alpaca'