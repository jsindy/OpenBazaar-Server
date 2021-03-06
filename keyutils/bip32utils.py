__author__ = 'chris'
import bitcoin
from binascii import unhexlify

def derive_childkey(public_key, chaincode):
    """
    Given a 33 byte public key and 32 byte chaincode (both in hex) derive the first child key.
    """

    master_pubkey = bitcoin.bip32_serialize((bitcoin.MAINNET_PUBLIC, 0, b'\x00'*4, 0,
                                             unhexlify(chaincode), unhexlify(public_key)))
    child_key = bitcoin.bip32_ckd(master_pubkey, 0)
    return bitcoin.bip32_extract_key(child_key)
