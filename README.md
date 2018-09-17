# kin-devplatform-wallet-creation
Helper scripts for creating Kin wallets.

By creating a digital wallet, the responsibility about keeping the wallet safe is in your hands.
Part of kin's company policy is to encourage the end users to take responsibility on their own 
property and make an intelligent use in order to prevent loss of assets.
Before creating a new wallet, we highly recommend to search outer resources to learn the best 
practices that are driven in the market, for example: 
https://goo.gl/SYR4ye

Befor starting the creating wallet process, please notice that you are going to generate two a key pair consisting of 
public address and a seed. **After creating this wallet we will not be able to restore or replace the these keys, we 
will not be able to restore it under no circumstances**. 
You are the only person who is responsible to keep this wallet and the pair keys. 
Please notice that the seed key must be kept where you and only you have access. We do recommend to use a hardware 
wallet. 


In order to create a new Kin wallet, fire up the terminal and follow the next steps:

First make sure that python is installed on your machine, to do that, please run the command: 
```bash
python3 --version
```
This this the expected output:
```bash
Python 2.7.15
```

Install Stellar Base:
```bash
pip3 install --user stellar_base
```

Step 1:

The main script will generate a random key pair hashed keys by using stellar codebase and prints them.
```bash
python3 main.py
```

This is the output of this step:
```bash
Public: GBK5HIGM7WYC7M6GYXE6OH7PTGFQNF5A35EHXLGQUWKU6GFOC76LYLWO
Seed: SAHUI57P7RN64OR3HGNM3CI26DX423KWZBLQAHFZFJP4LRGQYS6L6VOT
```

Step 2:
This script is registering the new wallet according to the output created in sep on.
To run the activate script you will need to run the following command with the 'Seed' that was generated in step 1 in 
your shell:
```bash
python3 activate.py SCXLXDAYWGWZMJHHJSR6KGARK43XX3HXW6XW4TVF6WR4JSE3WXVHQIFP
```
