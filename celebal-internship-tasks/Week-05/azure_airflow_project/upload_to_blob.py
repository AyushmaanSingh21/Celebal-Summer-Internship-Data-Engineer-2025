import os
from azure.storage.blob import BlobServiceClient
from config import AZURE_CONN_STRING, AZURE_CONTAINER_NAME

def upload_files(table_name):
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONN_STRING)
    container_client = blob_service_client.get_container_client(AZURE_CONTAINER_NAME)

    for fmt in ["csv", "parquet", "avro"]:
        file_path = f"{table_name}.{fmt}"
        blob_path = f"{table_name}/{fmt}/{file_path}"

        with open(file_path, "rb") as data:
            container_client.upload_blob(name=blob_path, data=data, overwrite=True)
            print(f"✅ Uploaded {file_path} to Azure Blob → {blob_path}")

# 👇 THIS is what was missing
if __name__ == "__main__":
    upload_files("products")
