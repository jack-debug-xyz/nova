# nova
Nova is an AI powered chatbot that runs on GPT-2. Nova runs locally on your computer. Nova is currently *closed source* but will be released soon. On this README there are installation instructions to run Nova.
### How to run on Google Colabatory (recommended)
1. Go to [this link](https://colab.research.google.com/drive/1PFIN-raNql7RnE5ZyHde15EttQj4TEmr?usp=sharing)

2. Click the run button next to the text that says '6 cells hidden' (this code is hidden because it takes up a large section of the page)

3. After it's finished, click the run button next to the code that says "novaMain()"

### How to install on your local machine
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
