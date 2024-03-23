provider "aws" {
  region = "us-east-1"
}

data "template_file" "init_script" {
  template = file("${path.module}/ec2-setup.tpl")
    
  vars = {
    NETWORK_NAME="my-network"
    BACKEND_CONTAINER="backend"
    FRONTEND_CONTAINER="frontend"
    BACKEND_IMAGE="jek2141/scraper_backend"
    FRONTEND_IMAGE="jek2141/scraper_frontend"
    DB_USERNAME="postgres"
    DB_PASSWORD="password"
    DB_NAME="postgres"
    DB_HOST=aws_db_instance.postgres_db.endpoint
  }
}

resource "aws_instance" "backend_server" {
  ami           = "ami-07d9b9ddc6cd8dd30"
  instance_type = "t2.micro"
  key_name = "example"
  # 
  depends_on = [aws_db_instance.postgres_db]
  vpc_security_group_ids = [aws_security_group.web_app.id]
  
  user_data = data.template_file.init_script.rendered
  
  tags = {
      Name = "backend server"
  }
}


resource "aws_security_group" "web_app" {
    name = "web app sec group"
    ingress {
        from_port   = 80
        to_port     = 80
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        cidr_blocks = [
          "0.0.0.0/0"
        ]
        from_port = 22
        to_port = 22
        protocol = "tcp"
      }
    
      egress {
       from_port = 0
       to_port = 0
       protocol = "-1"
       cidr_blocks = ["0.0.0.0/0"]
     }
}

output "ec2_connection_instructions" {
  value = "ssh with the following: ssh -i ~/.ssh/${aws_instance.backend_server.key_name}.pem ubuntu@${aws_instance.backend_server.public_dns}" 
}

