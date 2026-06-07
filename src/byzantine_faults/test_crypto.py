from crypto_utils import sign_message, verify_message
message = "TX001 : Pay Rs 100"
signature = sign_message(message)
print("Message:", message)
print("Signature Generated")
if verify_message(message, signature):
    print("Signature Verified")
else:
    print("Verification Failed")