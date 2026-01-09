from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server
from diagrams.onprem.database import MongoDB
from diagrams.onprem.inmemory import Redis
from diagrams.k8s.compute import Deployment, Pod, StatefulSet
from diagrams.k8s.network import Service, Ingress
from diagrams.k8s.storage import PV, PVC, StorageClass
from diagrams.aws.compute import EKS
from diagrams.aws.storage import EBS
from diagrams.aws.network import ELB
from diagrams.programming.framework import React
from diagrams.programming.language import NodeJS
from diagrams.saas.chat import Slack
from diagrams.saas.identity import Auth0

graph_attr = {
    "fontsize": "16",
    "bgcolor": "white",
    "pad": "0.5",
}

with Diagram("MERN eCommerce Kubernetes Architecture", 
             show=False, 
             direction="TB",
             graph_attr=graph_attr):
    
    users = Users("End Users")
    
    with Cluster("External Services"):
        razorpay = Auth0("Razorpay\nPayment")
        brevo = Slack("Brevo\nSMTP Email")
    
    with Cluster("AWS Cloud"):
        loadbalancer = ELB("Load Balancer")
        
        with Cluster("EKS Cluster"):
            ingress = Ingress("Ingress\nController")
            
            with Cluster("Frontend"):
                frontend_svc = Service("Frontend\nService")
                frontend_deploy = Deployment("Frontend\nDeployment\n(3 replicas)")
                frontend_pods = [
                    Pod("Nginx +\nReact App"),
                    Pod("Nginx +\nReact App"),
                    Pod("Nginx +\nReact App")
                ]
                
            with Cluster("Backend"):
                backend_svc = Service("Backend\nService")
                backend_deploy = Deployment("Backend\nDeployment\n(3 replicas)")
                backend_pods = [
                    Pod("Express\nAPI"),
                    Pod("Express\nAPI"),
                    Pod("Express\nAPI")
                ]
            
            with Cluster("Database"):
                mongo_svc = Service("MongoDB\nService")
                mongo_stateful = StatefulSet("MongoDB\nStatefulSet")
                mongo_pod = Pod("MongoDB")
                
                with Cluster("Storage"):
                    pvc = PVC("PVC\n10Gi")
                    pv = PV("Persistent\nVolume")
                    ebs = EBS("AWS EBS")
    
    # User flow
    users >> Edge(label="HTTPS") >> loadbalancer
    loadbalancer >> ingress
    
    # Frontend flow
    ingress >> Edge(label="Port 80") >> frontend_svc
    frontend_svc >> frontend_deploy
    frontend_deploy >> frontend_pods
    
    # Backend flow
    frontend_pods >> Edge(label="API Calls") >> backend_svc
    backend_svc >> backend_deploy
    backend_deploy >> backend_pods
    
    # Database flow
    backend_pods >> Edge(label="Port 5000") >> mongo_svc
    mongo_svc >> mongo_stateful
    mongo_stateful >> mongo_pod
    
    # Storage
    mongo_pod >> pvc
    pvc >> pv
    pv >> ebs
    
    # External services
    backend_pods >> Edge(label="Payment\nProcessing") >> razorpay
    backend_pods >> Edge(label="Order\nEmails") >> brevo


# Alternative: Detailed Component View
with Diagram("MERN eCommerce - Component Architecture", 
             show=False, 
             direction="LR",
             graph_attr=graph_attr,
             filename="mern_components"):
    
    with Cluster("Client Layer"):
        browser = Users("Web Browser")
        react_app = React("React App")
        redux = Server("Redux Store")
    
    with Cluster("Kubernetes - Frontend Tier"):
        nginx = Server("Nginx Server")
        static = Server("Static Assets")
    
    with Cluster("Kubernetes - Backend Tier"):
        with Cluster("Express API"):
            auth = NodeJS("Auth\nController")
            products = NodeJS("Product\nController")
            orders = NodeJS("Order\nController")
            
        with Cluster("Middleware"):
            jwt = Server("JWT Auth")
            error = Server("Error Handler")
    
    with Cluster("Data Layer"):
        mongodb = MongoDB("MongoDB")
        
        with Cluster("Collections"):
            users_col = Server("Users")
            products_col = Server("Products")
            orders_col = Server("Orders")
    
    with Cluster("External APIs"):
        payment = Auth0("Razorpay API")
        email = Slack("Brevo SMTP")
    
    # Flow
    browser >> react_app
    react_app >> redux
    redux >> Edge(label="HTTP/REST") >> nginx
    nginx >> static
    nginx >> Edge(label="API Proxy") >> auth
    
    auth >> jwt
    jwt >> products
    jwt >> orders
    
    auth >> users_col
    products >> products_col
    orders >> orders_col
    
    [users_col, products_col, orders_col] >> mongodb
    
    orders >> Edge(label="Process Payment") >> payment
    orders >> Edge(label="Send Email") >> email


# CI/CD Pipeline View
with Diagram("MERN eCommerce - CI/CD Pipeline", 
             show=False, 
             direction="LR",
             graph_attr=graph_attr,
             filename="mern_cicd"):
    
    from diagrams.programming.framework import React
    from diagrams.onprem.vcs import Github
    from diagrams.onprem.ci import GithubActions
    from diagrams.aws.compute import ECR
    from diagrams.onprem.container import Docker
    
    dev = Users("Developer")
    github = Github("GitHub\nRepository")
    actions = GithubActions("GitHub Actions")
    
    with Cluster("Build Stage"):
        docker_build = Docker("Docker Build")
        backend_img = Docker("Backend Image")
        frontend_img = Docker("Frontend Image")
    
    ecr = ECR("AWS ECR\nRegistry")
    
    with Cluster("Deploy Stage"):
        kubectl = Server("kubectl")
        eks = EKS("AWS EKS\nCluster")
    
    with Cluster("Kubernetes Resources"):
        deployments = Deployment("Update\nDeployments")
        pods = Pod("Rolling\nUpdate Pods")
    
    # Pipeline flow
    dev >> Edge(label="git push") >> github
    github >> Edge(label="trigger") >> actions
    
    actions >> docker_build
    docker_build >> backend_img
    docker_build >> frontend_img
    
    [backend_img, frontend_img] >> Edge(label="push") >> ecr
    
    ecr >> Edge(label="deploy") >> kubectl
    kubectl >> eks
    eks >> deployments
    deployments >> Edge(label="rollout") >> pods


print("Diagrams generated successfully!")
print("Files created:")
print("1. mern_ecommerce_kubernetes_architecture.png")
print("2. mern_components.png")
print("3. mern_cicd.png")