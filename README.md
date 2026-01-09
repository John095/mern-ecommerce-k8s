# MERN eCommerce Platform with Kubernetes

A cloud-native eCommerce platform built with the MERN stack (MongoDB, Express.js, React, Node.js) and containerized for Kubernetes deployment. This project demonstrates modern DevOps practices with Docker containerization, Kubernetes orchestration, and automated CI/CD pipelines.

## Features

### eCommerce Functionality

- **Full-Featured Shopping Cart**: Add, remove, and manage products
- **Product Reviews and Ratings**: User feedback system
- **Product Search & Pagination**: Efficient product browsing
- **User Profiles & Order History**: Complete user management
- **Admin Dashboard**: Comprehensive admin panel for managing products, users, and orders
- **Secure Checkout**: Multi-step checkout with Razorpay integration
- **Email Notifications**: Order confirmations via Brevo SMTP

### Cloud-Native Architecture

- **Docker Containerization**: Multi-stage builds for frontend and backend
- **Kubernetes Deployment**: Production-ready K8s manifests
- **MongoDB Integration**: Containerized database with persistent volumes
- **Load Balancing**: Kubernetes services with multiple replicas
- **Secret Management**: Secure handling of sensitive configuration

### DevOps & CI/CD

- **GitHub Actions**: Automated build and deployment pipeline
- **AWS EKS Integration**: Deploy to Amazon Elastic Kubernetes Service
- **ECR Registry**: Container image management
- **Environment Configuration**: Separate dev/prod configurations

## Getting Started

### Prerequisites

**For Local Development:**

- Node.js (v16+)
- MongoDB (local or Atlas)
- Docker & Docker Compose

**For Kubernetes Deployment:**

- kubectl
- AWS CLI (for EKS)
- Docker

**Required Accounts:**

- [Razorpay](https://razorpay.com/) for payment processing
- [Brevo](https://www.brevo.com/) for email services
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) (optional)

### Clone Repository

```bash
git clone https://github.com/your-username/mern-ecommerce-k8s.git
cd mern-ecommerce-k8s
```

### Environment Configuration

Copy the example environment file and configure your variables:

```bash
cp .env.example .env
```

Update `.env` with your configuration:

```dotenv
NODE_ENV=development
PORT=5000
JWT_SECRET=your_jwt_secret_here
MONGO_URI=mongodb://mongodb:27017/mern-ecommerce  # For Docker
# MONGO_URI=mongodb://localhost:27017/mern-ecommerce  # For local dev
RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_key_secret
PAGINATION_MAX_LIMIT=12
EMAIL_HOST=smtp-relay.brevo.com
EMAIL_PORT=587
EMAIL_USER=your_brevo_login
EMAIL_PASS=your_brevo_password
EMAIL_FROM=your_brevo_login
```

## Development

### Local Development (Traditional)

```bash
# Install dependencies
npm install
cd frontend && npm install && cd ..

# Run development servers
npm run dev  # Runs both frontend and backend
# OR
npm run server  # Backend only
npm run client  # Frontend only
```

### Docker Development

```bash
# Start all services with Docker Compose
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

Services will be available at:

- Frontend: http://localhost
- Backend API: http://localhost:5000
- MongoDB: localhost:27017

## Production Deployment

### Kubernetes Deployment

1. **Update Kubernetes manifests** with your container images:

   ```bash
   # Update image references in k8s/ files
   sed -i 's|BACKEND_IMAGE|your-registry/backend:tag|g' k8s/backend-deployment.yaml
   sed -i 's|FRONTEND_IMAGE|your-registry/frontend:tag|g' k8s/frontend-deployment.yaml
   ```

2. **Create secrets**:

   ```bash
   kubectl apply -f k8s/secrets.yaml
   ```

3. **Deploy application**:
   ```bash
   kubectl apply -f k8s/
   ```

### AWS EKS Deployment

The project includes GitHub Actions workflow for automated deployment to AWS EKS:

1. **Configure GitHub Secrets**:

   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `ECR_REGISTRY`

2. **Push to main branch** - deployment happens automatically

### Manual Docker Build

```bash
# Build images
docker build -f backend/Dockerfile -t mern-backend .
docker build -f frontend/Dockerfile -t mern-frontend ./frontend

# Run production containers
docker run -d -p 5000:5000 --env-file .env mern-backend
docker run -d -p 80:80 mern-frontend
```

## Database Management

### Seed Database

```bash
# Import sample data
npm run data:import

# Clear all data
npm run data:destroy
```

### Sample User Accounts

After seeding, you can use these test accounts:

**Admin Account:**

- Email: admin@admin.com
- Password: admin123

**Customer Accounts:**

- John Doe: john@email.com / john123
- Alice Smith: alice@email.com / alice123

## Project Structure

```
mern-ecommerce-k8s/
├── backend/                 # Node.js/Express API
│   ├── controllers/         # Route controllers
│   ├── models/             # MongoDB models
│   ├── routes/             # API routes
│   ├── middleware/         # Custom middleware
│   ├── config/             # Database & email config
│   ├── utils/              # Utility functions
│   ├── data/               # Seed data
│   └── Dockerfile          # Backend container
├── frontend/               # React application
│   ├── src/                # React source code
│   ├── public/             # Static assets
│   ├── nginx.conf          # Nginx configuration
│   └── Dockerfile          # Frontend container
├── k8s/                    # Kubernetes manifests
│   ├── backend-deployment.yaml
│   ├── frontend-deployment.yaml
│   ├── mongodb.yaml
│   └── secrets.yaml
├── .github/workflows/      # CI/CD pipeline
├── uploads/                # File upload directory
├── docker-compose.yml      # Local development
└── .env.example           # Environment template
```

## Technology Stack

- **Frontend**: React, Redux Toolkit, Bootstrap
- **Backend**: Node.js, Express.js, JWT Authentication
- **Database**: MongoDB with Mongoose ODM
- **Payment**: Razorpay Integration
- **Email**: Nodemailer with Brevo SMTP
- **Containerization**: Docker & Docker Compose
- **Orchestration**: Kubernetes
- **CI/CD**: GitHub Actions
- **Cloud**: AWS EKS, ECR

Feel free to explore and customize this cloud-native eCommerce platform! 🚀

# Contributing

Contributions are welcome! This project demonstrates modern cloud-native development practices.

## Development Workflow

1. **Fork and clone the repository**:

   ```bash
   git clone https://github.com/your-username/mern-ecommerce-k8s.git
   cd mern-ecommerce-k8s
   ```

2. **Create a feature branch**:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Set up development environment**:

   ```bash
   # Option 1: Docker (recommended)
   docker-compose up -d

   # Option 2: Local development
   npm install && cd frontend && npm install
   ```

4. **Make your changes** and test thoroughly:

   ```bash
   # Test locally
   npm run dev

   # Test with Docker
   docker-compose up --build
   ```

5. **Commit and push**:

   ```bash
   git add .
   git commit -m "feat: add your feature description"
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request** with a clear description of your changes.

## Areas for Contribution

- **Features**: New eCommerce functionality
- **DevOps**: Improve CI/CD pipeline, monitoring, logging
- **Security**: Enhance authentication, data validation
- **Performance**: Optimize database queries, caching
- **Documentation**: Improve setup guides, API docs
- **Testing**: Add unit tests, integration tests
- **Cloud**: Multi-cloud support, infrastructure as code

## Code Standards

- Follow existing code style and conventions
- Write meaningful commit messages
- Update documentation for new features
- Test changes in both local and containerized environments
- Ensure Kubernetes manifests are valid

Thank you for contributing to this cloud-native eCommerce platform! 🎉
