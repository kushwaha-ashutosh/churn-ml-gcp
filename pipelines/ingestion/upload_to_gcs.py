import os
from google.cloud import storage


def upload_file_to_gcs(local_path, bucket_name, destination_blob):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob)

    blob.upload_from_filename(local_path)
    print(f"Uploaded {local_path} to gs://{bucket_name}/{destination_blob}")


if __name__ == "__main__":
    bucket = os.environ["GCS_BUCKET"]
    local_file = os.environ.get("LOCAL_FILE", "data/sample_raw_data.csv")
    dest = os.environ.get("DEST_PATH", "raw/sample_raw_data.csv")

    upload_file_to_gcs(local_file, bucket, dest)
