from helper_functions.auth_helper import get_secret
import os

# Simulate local environment variable for Key Vault name
os.environ['KEY_VAULT_NAME'] = 'KV-Netmo-Integrations'

# Replace with the name of a real secret you’ve added in Azure
secret_name = 'API-Autotask-Client-ID'

secret_value = get_secret(secret_name)
print(f"Value for secret '{secret_name}': {secret_value}")
