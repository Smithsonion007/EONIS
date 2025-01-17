from hashlib import sha256

WATERMARK = "Nathan Andrew Smithsonian 26021985GOSAUS336PM"

def eonis_generate_license(user_id, product_key):
    license_data = f"{user_id}:{product_key}:{WATERMARK}"
    return sha256(license_data.encode()).hexdigest()

def eonis_validate_license(user_id, product_key, license_key):
    expected_key = eonis_generate_license(user_id, product_key)
    return expected_key == license_key
