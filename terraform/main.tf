provider "aws" {
    region = "eu-central-1"
    access_key = var.AWS_ACCESS_KEY_ID 
    secret_key = var.AWS_SECRET_ACCESS_KEY
}

resource "aws_lightsail_instance" "watchit-test" {
    name = "watchit-test"
    availability_zone = "eu-central-1"
    blueprint_id = "amazon_linux_2023"
    bundle_id = "small_3_0"
}