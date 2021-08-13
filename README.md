# nova
Nova is an AI powered chatbot that runs on GPT-2. Nova runs locally on your computer. Nova is currently *closed source* but will be released soon. On this README there are installation instructions to run Nova.
### How to install
1. **Install miniconda**

Miniconda is required for the virtual environment needed to run Nova. You can find instructions to install miniconda and installers [here](https://docs.conda.io/en/latest/miniconda.html)

2. **Start new virtual env with miniconda**

To start a new virtual environment in miniconda, enter this into your command line.

`$ conda create -n nova python=3.6 anaconda`

Activate the virtual env with

`$ conda activate nova`

3. **Install dependencies**

Install the dependencies with pip.

`$ pip install gpt_2_simple tensorflow==1.15.2`

4. **Download the script and run**

The script optimally requires it's own folder to run in. When you're ready to run, use

`$ python main.py`
