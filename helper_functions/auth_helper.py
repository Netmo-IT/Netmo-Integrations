from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from typing import Optional
import os

def get_secret(secret_name: str) -> Optional[str]:
    key_vault_name = os.environ.get("KEY_VAULT_NAME")
    if not key_vault_name:
        raise EnvironmentError("KEY_VAULT_NAME environment variable not set")

    vault_url = f"https://{key_vault_name}.vault.azure.net"
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=vault_url, credential=credential)
    
    secret = client.get_secret(secret_name)
    return secret.value
