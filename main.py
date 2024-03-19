import rsa
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='RSA', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input', type=str, help='Input file')
    parser.add_argument('-o', '--output', type=str, help='Output file')
    args = parser.parse_args()
    with open(args.input, 'r') as input_file:
        message = input_file.read()

    public_key, private_key = rsa.generate_keypair()

    encrypted_message = rsa.encrypt(message, public_key)
    decrypted_message = rsa.decrypt(encrypted_message, private_key)
    assert message == decrypted_message

    with open(args.output, 'w') as output_file:
        output_file.write(decrypted_message)

    print('Success')
