from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import ECS, EC2, ECR
from diagrams.aws.network import ALB
from diagrams.aws.security import CertificateManager
from diagrams.aws.storage import EBS
from diagrams.aws.network import ELB

with Diagram("AWS ECS Architecture", show=False, direction="TB"):
    # Certificate Manager
    cert_manager = CertificateManager("ACM Certificate")

    # Application Load Balancer
    alb = ALB("Application Load Balancer")

    # Optionally represent three separate target groups as placeholders
    with Cluster("Target Groups"):
        tg_tethys   = ELB("Tethys TG")
        tg_geoserver = ELB("GeoServer TG")
        tg_thredds  = ELB("THREDDS TG")

    # ECS Cluster
    with Cluster("ECS Cluster (t2.2xlarge + 100 GiB gp2)"):
        # Individual ECS services
        tethys_service   = ECS("Tethys Platform")
        geoserver_service = ECS("GeoServer")
        thredds_service  = ECS("THREDDS Unidata Server")
        
        # (Optional) EBS block for the gp2 volume
        ebs_volume = EBS("gp2 Volume 100 GiB")

    # ECR (for storing container images)
    ecr_repo = ECR("ECR Repository")

    # Diagram connections
    cert_manager >> alb
    alb >> tg_tethys >> tethys_service
    alb >> tg_geoserver >> geoserver_service
    alb >> tg_thredds >> thredds_service

    # Show that all ECS services pull images from the ECR repository
    ecr_repo >> tethys_service

    # Optionally connect storage to each ECS service
    ebs_volume - tethys_service
    ebs_volume - geoserver_service
    ebs_volume - thredds_service
