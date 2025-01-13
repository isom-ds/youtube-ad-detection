# YouTube Sponsored Ad Segment Detection

This repository provides a Python project template for YouTube ad detection. It utilizes Docker to create a standardized development environment using local containers.

## Requirements
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Visual Studio Code](https://code.visualstudio.com/)

## Getting Started
To get started with this project, follow these steps:

1. Clone this repository to your local machine.
2. Open the project in Visual Studio Code.
3. Edit the `requirements.txt` file to install any additional Python modules you may need.
4. Run the Docker container with Python 3.12.5 to start working on your project.

## Usage
Once you have set up the project, you can use it to detect YouTube ads. Add your ad detection code to the appropriate files and run the project within the Docker container.

You will need to create a `keys.py` in the root directory of the project.
It must contain your YouTube API and OpenAI keys like so:

```python
yt_key = 'youtube-api-key'
openai_key = "open-ai-api-key"
```
