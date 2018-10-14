from kin.stellar.builder import Builder
from stellar_base.network import NETWORKS


def add_signer(master_seed, signer_address):
    # Add signer
    builder = Builder(secret=master_seed,
                      horizon_uri="https://horizon-ecosystem.kininfrastructure.com",
                      network="PROD")

    # Add the signer to the account, the signer should be able to remove the master key if he wants to.
    builder.append_set_options_op(high_threshold=2, signer_address=signer_address, signer_type='ed25519PublicKey',
                                  signer_weight=2)
    builder.sign()
    builder.submit()




if __name__ == '__main__':
    NETWORKS['PROD'] = "Public Global Kin Ecosystem Network ; June 2018"
    # Once we have all the keys, we can probably the seeds from amazon and the signers from a csv
    add_signer('base_seed',
               'signer_to_add')

