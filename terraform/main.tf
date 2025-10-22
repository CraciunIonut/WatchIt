provider "aws" {
    region = "eu-central-1"
}

resource "aws_lightsail_instance" "watchit-test" {
    name = "watchit-test"
    availability_zone = "eu-central-1"
    blueprint_id = "amazon_linux_2023"
    bundle_id = "small_3_0"
}

resource "aws_lightsail_instance" "watchit-prd1" {
    name = "watchit-test"
    availability_zone = "eu-central-1"
    blueprint_id = "amazon_linux_2023"
    bundle_id = "small_3_0"
}

variable "AWS_ACCESS_KEY_ID" {
    type = string
    sensitive = true
}

variable "AWS_SECRET_ACCESS_KEY" {
    type = string
    sensitive = true
}