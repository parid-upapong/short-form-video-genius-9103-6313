# Storage Layer: S3 for Assets & EFS for High-Performance Rendering Cache

# 1. S3 Buckets for Media Assets
resource "aws_s3_bucket" "assets" {
  bucket        = "overlord-media-assets-${var.environment}"
  force_destroy = true
}

resource "aws_s3_bucket_lifecycle_configuration" "assets_lifecycle" {
  bucket = aws_s3_bucket.assets.id

  rule {
    id     = "cleanup-tmp"
    status = "Enabled"
    filter { prefix = "temp/" }
    expiration { days = 7 }
  }
}

# 2. EFS for Shared Workspace (Crucial for FFmpeg frame-stitching across pods)
resource "aws_efs_file_system" "rendering_cache" {
  creation_token = "overlord-rendering-cache"
  encrypted      = true
  performance_mode = "generalPurpose" # or "maxIO" for extreme parallel rendering
  throughput_mode  = "elastic"

  tags = { Name = "Overlord-GPU-Shared-Cache" }
}

resource "aws_efs_mount_target" "mount" {
  count           = length(module.vpc.private_subnets)
  file_system_id  = aws_efs_file_system.rendering_cache.id
  subnet_id       = module.vpc.private_subnets[count.index]
  security_groups = [aws_security_group.efs.id]
}

resource "aws_security_group" "efs" {
  name   = "overlord-efs-sg"
  vpc_id = module.vpc.vpc_id

  ingress {
    from_port       = 2049
    to_port         = 2049
    protocol        = "tcp"
    cidr_blocks     = [local.vpc_cidr]
  }
}