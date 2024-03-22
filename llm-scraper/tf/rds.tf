locals { 
    db_config = {
        db_name = "job_scraper"
        instance_name = "scraper_db"
        username = "postgres"
        password = "password"
    }
}

resource "aws_db_instance" "postgres_db" {
  allocated_storage    = 20
  db_name =             "job_scraper"
  storage_type         = "gp2"
  engine               = "postgres"
  engine_version       = "16.1"  
  instance_class       = "db.t3.micro"
  username             = "postgres"
  password             = "password"
  parameter_group_name = "default.postgres16"
  skip_final_snapshot  = true
  publicly_accessible  = true
  # remove this
  vpc_security_group_ids = [aws_security_group.postgres_access.id]
  tags = { Name = local.db_config.instance_name }
}

resource "aws_security_group" "postgres_access" {
  name = "scraper postgres access"
  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    # remove
    security_groups = [aws_security_group.web_app.id]
  }
}


output "rds_connection_instructions" {
  value = "psql -d ${aws_db_instance.postgres_db.db_name} -h ${aws_db_instance.postgres_db.endpoint} -U ${aws_db_instance.postgres_db.username}"
}