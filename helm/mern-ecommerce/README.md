# MERN eCommerce Helm Chart

This Helm chart deploys the MERN eCommerce platform on Kubernetes.

## Prerequisites

- Kubernetes 1.19+
- Helm 3.0+

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/mern-ecommerce-k8s.git
   cd mern-ecommerce-k8s
   ```

2. **Update values.yaml with your configuration:**
   ```bash
   cp helm/mern-ecommerce/values.yaml values-custom.yaml
   # Edit values-custom.yaml with your settings
   ```

3. **Install the chart:**
   ```bash
   helm install mern-ecommerce ./helm/mern-ecommerce -f values-custom.yaml
   ```

## Configuration

### Required Values

Update these values in your `values-custom.yaml`:

```yaml
image:
  backend:
    repository: 123456789012.dkr.ecr.us-east-1.amazonaws.com/mern-backend
    tag: latest
  frontend:
    repository: 123456789012.dkr.ecr.us-east-1.amazonaws.com/mern-frontend
    tag: latest

secrets:
  jwtSecret: "your-secure-jwt-secret"
  razorpay:
    keyId: "your-razorpay-key-id"
    keySecret: "your-razorpay-secret"
  email:
    user: "your-email@example.com"
    pass: "your-email-password"
    from: "your-email@example.com"
```

### Optional AWS S3 Configuration

```yaml
secrets:
  aws:
    accessKeyId: "your-aws-access-key"
    secretAccessKey: "your-aws-secret-key"
    region: "us-east-1"
    s3BucketName: "your-bucket-name"
```

### Ingress Configuration

```yaml
ingress:
  enabled: true
  hosts:
    - host: your-domain.com
      paths:
        - path: /
          pathType: Prefix
```

## Usage

### Deploy
```bash
helm install mern-ecommerce ./helm/mern-ecommerce -f values-custom.yaml
```

### Upgrade
```bash
helm upgrade mern-ecommerce ./helm/mern-ecommerce -f values-custom.yaml
```

### Uninstall
```bash
helm uninstall mern-ecommerce
```

### Check Status
```bash
helm status mern-ecommerce
kubectl get pods -l app.kubernetes.io/instance=mern-ecommerce
```

## Features

- ✅ **Configurable replicas** for frontend and backend
- ✅ **MongoDB with persistent storage**
- ✅ **Secrets management** for sensitive data
- ✅ **Ingress support** with customizable routing
- ✅ **AWS S3 integration** (optional)
- ✅ **Resource limits** and node affinity
- ✅ **Production-ready** configuration