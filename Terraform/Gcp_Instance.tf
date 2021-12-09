provider "google" {
  credentials = file("my-practice-project-54.json")
  project     = "my-practice-project-54"
  region      = "us-west1"
}


#resource "random_id" "instance_id" {
#  byte_length = 8
#}

resource "google_compute_instance" "default" {
  name         = "elk-demo"
  machine_type = "e2-standard-8"
  zone         = "us-west1-a"


  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  metadata_startup_script = "sudo apt-get update ; sudo apt-get install -y nginx"

  network_interface {
    network = "default"


    access_config {
    }

  }
}



