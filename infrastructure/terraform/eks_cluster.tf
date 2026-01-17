# EKS Cluster Setup with GPU Support

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 19.0"

  cluster_name    = local.name
  cluster_version = "1.28"

  vpc_id                         = module.vpc.vpc_id
  subnet_ids                     = module.vpc.private_subnets
  cluster_endpoint_public_access = true

  # Managed Node Group for Control Plane Apps (CPU)
  eks_managed_node_groups = {
    system_nodes = {
      instance_types = ["t3.medium"]
      min_size       = 1
      max_size       = 3
      desired_size   = 2
    }
  }

  # Fargate Profile for API (Optional, but good for cost)
  fargate_profiles = {
    api = {
      name = "api-profile"
      selectors = [{ namespace = "overlord-api" }]
    }
  }
}

# IAM Role for Karpenter (The GPU Autoscaler)
module "karpenter" {
  source = "terraform-aws-modules/eks/aws//modules/karpenter"

  cluster_name = module.eks.cluster_name

  irsa_oidc_provider_arn          = module.eks.oidc_provider_arn
  irsa_namespace_service_accounts = ["karpenter:karpenter"]

  enable_karpenter_instance_profile_creation = true
}