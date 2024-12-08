# SNAP To `TYPST`

This repository contains a web application that allows users to upload an image  of an equation and receive the corresponding `Typst` code. Additionally, users can input a URL to obtain the Hayagriva `YAML`-formatted bibliography reference compatible with `Typst`.

## Features
1. **Equation Parser**: Upload an image containing an equation, and the application will parse it and generate the corresponding `Typst` code.
1. **URL Bibliography Fetcher**: Input a URL, and the application will fetch and display metadata such as the author, title, and publication name in `YAML` format compatible with `Typst`.

## Installation
To install the required dependencies, run:
```zsh
uv pip install -r requirements.txt
```
You need to install the `ollama` CLI to run the application. To install the CLI, run:
```zsh
curl -fsSL https://ollama.com/install.sh | sh
```
`llama3.2-vision` is required to run the application:
```zsh
ollama run llama3.2-vision
```

## Usage
To start the application, run:
```zsh
streamlit run app.py
```

## Project Structure
- `app.py`: The main application file;
- `bib.txt`: contains the guidelines for bibliographic metadata retrieval;
- `eq.txt`: contains the guidelines for equation parsing;
- `.streamlit/config.toml`: Configuration file for Streamlit.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
