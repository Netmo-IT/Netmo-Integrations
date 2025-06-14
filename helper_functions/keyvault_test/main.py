import logging
import azure.functions as func
from helper_functions.auth_helper import get_secret

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Key Vault test function triggered")

    secret_name = req.params.get("secret")
    if not secret_name:
        return func.HttpResponse("Please provide a 'secret' query parameter.", status_code=400)

    try:
        secret_value = get_secret(secret_name)
        return func.HttpResponse(f"Value of secret '{secret_name}': {secret_value}")
    except Exception as e:
        logging.error(f"Error fetching secret: {str(e)}")
        return func.HttpResponse(f"Failed to retrieve secret: {str(e)}", status_code=500)
