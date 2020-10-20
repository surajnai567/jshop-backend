import paytmchecksum
from typing import Dict
# initialize an Hash/Array
paytmParams = {}

paytmParams["MID"] = "123456789"
paytmParams["ORDERID"] = "054300"

# Generate checksum by parameters we have
# Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
paytmChecksum = paytmchecksum.generateSignature(paytmParams, "YOUR_MERCHANT_KEY")
print("generateSignature Returns:" + str(paytmChecksum))


def create_paytm_checksum(params: Dict, merchant_key):
    return paytmChecksum.generatesSignature(params, merchant_key)


def validate_checksum(params: Dict, merchant_key, check_sum):
    return paytmChecksum.verifySignature(params, merchant_key, check_sum)

print(create_paytm_checksum(paytmParams, 123456789))