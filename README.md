# kin-devplatform-wallet-creation
Helper scripts to create Kin wallets.

In order to create a new Kin wallet, fire up the terminal and follow the next steps:

First make sure that python is installed on your machine, to do that, please run the command: 
```bash
python --version
```
This this the expected output:
```bash
Python 2.x.x (3 is fine as well)
```

Install Stellar Base:
```bash
pip install --user stellar_base
```

Step 1 - Key Generation

The main script will generate a random keypair, these are your public address and secret seed:
```bash
python main.py
```

This is an example output of this step:
```bash
Public: GBK5HIGM7WYC7M6GYXE6OH7PTGFQNF5A35EHXLGQUWKU6GFOC76LYLWO
Seed: SAHUI57P7RN64OR3HGNM3CI26DX423KWZBLQAHFZFJP4LRGQYS6L6VOT
```

Step 2 - Account activation, this can only be done after a third party created the account on the blockchain
To run the activate script you will need to run the following command with the 'Seed' that was generated in step 1 in 
your shell:
```bash
python activate.py SCXLXDAYWGWZMJHHJSR6KGARK43XX3HXW6XW4TVF6WR4JSE3WXVHQIFP
```
