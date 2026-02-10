provider "google" {
  project = var.project_id
  region  = var.region
}

# Enable required APIs
resource "google_project_service" "services" {
  for_each = toset([
    "aiplatform.googleapis.com",
    "artifactregistry.googleapis.com",
    "storage.googleapis.com",
    "bigquery.googleapis.com"
  ])

  project = var.project_id
  service = each.key
}

# Storage bucket
resource "google_storage_bucket" "ml_bucket" {
  name          = "${var.project_id}-ml-bucket"
  location      = var.region
  force_destroy = true
}

# Artifact Registry
resource "google_artifact_registry_repository" "repo" {
  location      = var.region
  repository_id = "churn-repo"
  format        = "DOCKER"
}

# Service account for training
resource "google_service_account" "trainer" {
  account_id   = "churn-trainer"
  display_name = "Churn Training Service Account"
}

# IAM roles
resource "google_project_iam_member" "trainer_roles" {
  for_each = toset([
    "roles/storage.admin",
    "roles/aiplatform.user",
    "roles/artifactregistry.reader"
  ])

  project = var.project_id
  role    = each.key
  member  = "serviceAccount:${google_service_account.trainer.email}"
}
