#!/bin/bash

# ECR Setup Script for MERN eCommerce
# This script creates ECR repositories and provides push commands

set -e

# Configuration
AWS_REGION=${AWS_REGION:-us-east-1}
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
ECR_REGISTRY="${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com"

echo "🚀 Setting up ECR repositories for MERN eCommerce"
echo "AWS Account ID: ${AWS_ACCOUNT_ID}"
echo "AWS Region: ${AWS_REGION}"
echo "ECR Registry: ${ECR_REGISTRY}"

# Create ECR repositories
echo "📦 Creating ECR repositories..."

aws ecr create-repository \
    --repository-name mern-backend \ 
    --region ${AWS_REGION} \
    --image-scanning-configuration scanOnPush=true \
    || echo "Repository mern-backend already exists"

aws ecr create-repository \
    --repository-name mern-frontend \
    --region ${AWS_REGION} \
    --image-scanning-configuration scanOnPush=true \
    || echo "Repository mern-frontend already exists"

# Get ECR login token
echo "🔐 Logging into ECR..."
aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REGISTRY}

echo "✅ ECR setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Build and push images:"
echo "   docker build -f backend/Dockerfile -t ${ECR_REGISTRY}/mern-backend:latest ."
echo "   docker push ${ECR_REGISTRY}/mern-backend:latest"
echo ""
echo "   docker build -f frontend/Dockerfile -t ${ECR_REGISTRY}/mern-frontend:latest ./frontend"
echo "   docker push ${ECR_REGISTRY}/mern-frontend:latest"
echo ""
echo "2. Update Helm values or K8s manifests with:"
echo "   Backend Image: ${ECR_REGISTRY}/mern-backend:latest"
echo "   Frontend Image: ${ECR_REGISTRY}/mern-frontend:latest"
echo ""
echo "3. Deploy with Helm:"
echo "   helm install mern-ecommerce ./helm/mern-ecommerce --set image.backend.repository=${ECR_REGISTRY}/mern-backend --set image.frontend.repository=${ECR_REGISTRY}/mern-frontend"