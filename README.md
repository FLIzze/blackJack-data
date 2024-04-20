# Blackjack_analyse

## Introduction

This project is a data analysis of the game of Blackjack. The goal is to determine the best strategy to adopt in order to maximize the chances of winning. The analysis is based on the rules of the game of Blackjack as described in the book "The Theory of Blackjack" by Peter A. Griffin.

## Installation

To install the project, you need to clone the repository and install the required packages. You can do this by running the following commands:

```bash
git clone git@github.com:DoctorPok42/Blackjack_analyse.git

cd Blackjack_analyse

npm install

pip install -r requirements.txt
```
You also need to create a .env file with the API URL like this (this example is the default used by the API) :
```
API_URL=http://localhost:5000/
```

Or if you are on Linux you can run the script to setup the project :
```bash
./setup.sh
```

## Usage

To run the project, you need to start the server and the client. You can do this by running the following commands:

```bash
cd server && python api.py
```

```bash
npm run dev
```

Or if you are on Linux you can run the scripts to run Api and the Dashboard :
```bash
./run_api.sh
./run_dash.sh
``` 

Enjoy it!
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
