import os
import logging
from typing import Optional
import azure.functions as func
from azure.identity import DefaultAzureCredential


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Key Vault test function triggered")

    secret_name = "API-Pax8-Client-ID"
    key_vault_name = os.environ.get("KEY_VAULT_NAME")
   
    vault_url = f"https://{key_vault_name}.vault.azure.net"
    #credential = DefaultAzureCredential()
    #client = SecretClient(vault_url=vault_url, credential=credential)
    
    #secret = client.get_secret(secret_name)
    #return func.HttpResponse(secret.value if secret.value else "Bad", status_code=200)
    return func.HttpResponse("finally")




