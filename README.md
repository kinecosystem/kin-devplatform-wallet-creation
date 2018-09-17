# kin-devplatform-wallet-creation
Helper scripts for creating Kin wallets.

In order to create a new Kin wallet, fire up the terminal and follow the next steps:

First make sure that python3 is installed on your machine, to do this run the command: 
```bash
python3 --version
```
This this the expected output (any version above 3.0.0 will do):
```bash
Python 3.6.5
```

Install Stellar Base:
```bash
pip3 install --user stellar_base
```

Step 1:
```bash
python3 main.py
```

Step 2:

Run the following command with the 'seed' from step 1 in your shell:
```bash
python3 activate.py SCXLXDAYWGWZMJHHJSR6KGARK43XX3HXW6XW4TVF6WR4JSE3WXVHQIFP
```
