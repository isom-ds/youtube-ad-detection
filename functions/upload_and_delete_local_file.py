import os
from google.cloud import storage

def upload_and_delete_local_file(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to Google Cloud Storage and deletes the local file afterward."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Upload the file to GCS
    blob.upload_from_filename(source_file_name)

    # Delete the local file
    if os.path.exists(source_file_name):
        os.remove(source_file_name)
    else:
        pass