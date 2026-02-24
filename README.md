# Binance Interactive Trading CLI

A robust, interactive Python command-line interface (CLI) application for executing algorithmic trades on the Binance Spot Testnet. This project demonstrates secure API integration, robust error handling, input validation, and professional application logging.

## Features

* **Interactive CLI:** Built with `Typer` and `Questionary` to provide a seamless, colorful, and user-friendly terminal experience.
* **Spot Market Trading:** Execute real-time `MARKET` and `LIMIT` orders directly on the Binance Testnet.
* **Live Wallet Verification:** Automatically fetches and displays updated asset balances immediately after a successful trade.
* **Bulletproof Error Handling:** Gracefully intercepts and translates complex Binance API exceptions into human-readable terminal alerts without crashing.
* **Production-Grade Logging:** Implements a custom logging configuration to silently track all API requests, successful executions, and system errors in a dedicated `bot.log` file.
* **Modern Python Packaging:** Utilizes `pyproject.toml` for clean, standard dependency management.

## Tech Stack

* **Language:** Python 3.11+
* **Core Libraries:** `python-binance` (API wrapper), `Typer` (CLI framework), `questionary` (Interactive prompts)
* **Environment Management:** `python-dotenv` for secure API key handling

## Installation

**1. Clone the repository**
```bash
git clone [https://github.com/manishpatel836/TREADING_BOT.git](https://github.com/manishpatel836/TREADING_BOT.git)
cd TREADING_BOT
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install .

To use this bot without risking real funds, you must use the Binance Spot Testnet.

Go to the Binance Spot Testnet.

Log in using your GitHub account.

Click "Generate HMAC_SHA256 Key".

Copy the generated API Key and Secret Key.
Go to TRADING_BOT/.env File and add
BINANCE_API_KEY=your_testnet_api_key_here
BINANCE_API_SECRET=your_testnet_api_secret_here

##USAGE##
Run the main CLI script to launch the interactive prompt:
python cli.py
Example Execution
? Enter trading symbol: ETHUSDT
? BUY or SELL?: BUY
? MARKET or LIMIT?: LIMIT
? Enter quantity to trade: 0.01
? Enter the LIMIT price: 2500