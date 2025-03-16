terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~>4.16"
        }
    }
    required_version = ">= 1.2.0"
}

terraform {
  backend "s3" {
    bucket = "terraform-kartik"
    key    = "terraform.tfstate"
    region = "ca-central-1"
    encrypt = false
  }
}
