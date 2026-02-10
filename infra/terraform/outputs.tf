output "bucket_name" {
  value = google_storage_bucket.ml_bucket.name
}

output "service_account_email" {
  value = google_service_account.trainer.email
}
