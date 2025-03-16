from robot import Robot
from warehouse import Warehouse

if __name__ == '__main__':
    # Initialize warehouse with a package on a shelf and an exit zone
    warehouse = Warehouse({"S3": ["P1"]}, ["Z1"])

    # Create and add a robot
    robot = Robot("R1", "S0")
    warehouse.add_robot(robot)

    # Execute the delivery plan
    warehouse.plan_delivery("R1", "P1", "Z1")