from kin.stellar.builder import Builder
from stellar_base.network import NETWORKS
import sys

def main():
	# Create trustline
	NETWORKS['PRIVATE'] = "Public Global Kin Ecosystem Network ; June 2018"
	KIN_ISSUER = "GDF42M3IPERQCBLWFEZKQRK77JQ65SCKTU3CW36HZVCX7XX5A5QXZIVK"
	builder = Builder(secret=sys.argv[1], horizon_uri="https://horizon-ecosystem.kininfrastructure.com", network="PRIVATE")
	builder.append_trust_op(KIN_ISSUER, "KIN")
	builder.sign()
	builder.submit()


if __name__ == '__main__':
	main()