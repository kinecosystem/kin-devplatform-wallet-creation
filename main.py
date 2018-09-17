from stellar_base.keypair import Keypair


def main():
	# Generate keys
	keys = Keypair.random()
	public = keys.address().decode()
	seed = keys.seed().decode()

	print("Public: {}" .format(public))
	print("Seed: {}" .format(seed))


if __name__ == '__main__':
	main()