# sudo apt update; sudo apt install graphviz
# pip3 install diagrams
# python3 aws.py

from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.custom import Custom
from urllib.request import urlretrieve

users_url = "https://cdn-icons-png.flaticon.com/512/8452/8452029.png"
users_icon = "users.png"
urlretrieve(users_url, users_icon)

diagram_attrs = {
    # "splines": "spline",
    "margin" : "-0.5",
    "bgcolor": "white:lightgray"
}

with Diagram("Simple architecture", show=True, direction="LR", graph_attr=diagram_attrs, outformat="png"):
    users = Custom("users", users_icon, shape="square", style="filled")

    with Cluster("VPC", graph_attr= {"bgcolor": "white"}):
      lb = ELB("loadbalancer")
      with Cluster("AZ a - app"):
        appAZa = [EC2("App"),
              EC2("App")]
      with Cluster("AZ a - db"):
        rdsMain = RDS("postgres main")
      with Cluster("AZ b - app"):
        appAZb = [EC2("App"),
              EC2("App")]
      with Cluster("AZ b - db"):
        rdsStandby = RDS("postgres standby")
    
    users >> lb

    lb >> appAZa
    lb >> appAZb
    
    appAZa >> rdsMain
    appAZb >> rdsMain

    rdsMain >> Edge(color="firebrick", style="dashed") >> rdsStandby