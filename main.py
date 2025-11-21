import pyotp
import qrcode
import time

# -----------------------------
#  TWO FACTOR AUTHENTICATION
# -----------------------------

# Step 1: Generate a secret key
secret_key = pyotp.random_base32()
print("\nGenerated Secret Key:", secret_key)

# Step 2: Create a TOTP object
totp = pyotp.TOTP(secret_key)

# Step 3: Generate QR Code URL (Google Authenticator compatible)
qr_url = totp.provisioning_uri(name="User", issuer_name="My2FAProject")

print("\nScan this QR code with Google Authenticator:")
print(qr_url)

# Step 4: Save QR Code as image
qr = qrcode.make(qr_url)
qr.save("2fa_qr.png")

print("\nQR Code saved as 2fa_qr.png (open it and scan).\n")

# Step 5: Display current OTP
current_otp = totp.now()
print("Current OTP (for testing):", current_otp)

# Step 6: User enters OTP
user_input = input("\nEnter OTP from Google Authenticator: ")

# Step 7: Verify OTP
if totp.verify(user_input):
    print("\n✔ Authentication Successful!")
else:
    print("\n✘ Authentication Failed!")
