import os
import logging
from typing import Optional
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

import logging
import os
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import warnings
warnings.filterwarnings(
    "ignore", 
    message=".*urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL.*'",
    category=UserWarning,
    module="urllib3"
)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Key Vault test function triggered")

    # Get the secret_name from the query parameter
    secret_name = req.params.get("secret")
    
    # If no secret parameter is provided, return a 400 status code
    if not secret_name:
        return func.HttpResponse(
            "Please provide a 'secret' query parameter.", status_code=400
        )

    key_vault_name = os.environ.get("KEY_VAULT_NAME")
    vault_url = f"https://{key_vault_name}.vault.azure.net"
    
    # Authenticate and create a Key Vault client
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)
    
    try:
        # Get the secret value from Azure Key Vault
        secret = client.get_secret(secret_name)
        return func.HttpResponse(secret.value if secret.value else "Error", status_code=200)
    
    except Exception as e:
        logging.error(f"Error fetching secret: {str(e)}")
        return func.HttpResponse(f"Failed to retrieve secret: {str(e)}", status_code=500)



