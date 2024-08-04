# Telegram RAG Chatbot

This repository contains the code for a Telegram bot that interfaces with the Telegram Bot API and integrates AI chatbot features. The bot leverages advanced speech-to-text and natural language processing capabilities to provide intelligent responses to user queries.

## Features

- **Text and Voice Message Handling**: The bot can process both text and voice messages from users.
- **Speech-to-Text Conversion**: Utilizes OpenAI's Whisper API to transcribe voice messages into text.
- **AI-Powered Responses**: Integrates with the VectorShift API to generate intelligent responses based on user input.
- **Command Handling**: Supports custom commands such as `/start` and `/caps`.

## Setup and Installation

### Prerequisites

- Python 3.12+
- Telegram Bot Token
- OpenAI API Key
- VectorShift API Key

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/telegram-rag-chatbot.git
    cd telegram-rag-chatbot
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Configure your environment variables:
    ```sh
    export TELEGRAM_BOT_TOKEN='your-telegram-bot-token'
    export OPENAI_API_KEY='your-openai-api-key'
    export VECTORSHIFT_API_KEY='your-vectorshift-api-key'
    ```

### Running the Bot

To run the bot locally, use the following command:
    ```sh
    python -m src.bot.main
    ```


### Deploying to Heroku

1. Log in to Heroku and create a new app:
    ```sh
    heroku login
    heroku create your-app-name
    ```

2. Set the required environment variables on Heroku:
    ```sh
    heroku config:set TELEGRAM_BOT_TOKEN='your-telegram-bot-token'
    heroku config:set OPENAI_API_KEY='your-openai-api-key'
    heroku config:set VECTORSHIFT_API_KEY='your-vectorshift-api-key'
    ```

3. Deploy the code to Heroku:
    ```sh
    git push heroku main
    ```

4. Scale the worker dyno:
    ```sh
    heroku ps:scale worker=1
    ```

## Usage

- **/start**: Initiates a conversation with the bot.
- **/caps**: Converts the text sent by the user to uppercase (for testing purposes).
- **Text and Voice Messages**: The bot processes and responds to both text and voice messages intelligently.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
