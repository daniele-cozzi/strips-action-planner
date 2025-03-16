class Warehouse:
    """
    Represents an automated warehouse with shelves, exit zones, and a planning system for package delivery.
    """
    def __init__(self, shelves, exit_zones):
        """
        Initializes the warehouse.

        :param shelves: Dictionary mapping shelf locations to stored packages. E.g., {"S1": ["P1", "P2"]}.
        :param exit_zones: List of exit zones.
        """
        self.shelves = shelves
        self.exit_zones = exit_zones
        self.robots = {} # Dictionary (key: robot_id, value: Robot instance) of robots in the warehouse. E.g., {"R1": Robot("R1", "S0")}

    def add_robot(self, robot):
        """
        Adds a robot to the warehouse.

        :param robot: Robot instance.
        """
        self.robots[robot.id] = robot

    def pick_up(self, robot_id, package, position):
        """
        Handles the package pick-up action.

        :param robot_id: Robot identifier.
        :param package: Package identifier.
        :param position: Shelf position.
        :return: True if successful, False otherwise.
        """
        robot = self.robots[robot_id]
        if robot.position == position and package in self.shelves.get(position, []):
            self.shelves[position].remove(package)
            robot.pick_up(package)
            return True
        return False

    def drop_off(self, robot_id, exit_zone):
        """
        Handles the package drop-off action.

        :param robot_id: Robot identifier.
        :param exit_zone: Exit zone location.
        :return: True if successful, False otherwise.
        """
        robot = self.robots[robot_id]
        if robot.position == exit_zone and robot.package:
            delivered_package = robot.drop_off()
            print(f"Package {delivered_package} delivered to {exit_zone}.")
            return True
        return False

    def plan_delivery(self, robot_id, package, destination):
        """
        Plans and executes the package delivery.

        :param robot_id: Robot identifier.
        :param package: Package identifier.
        :param destination: Exit zone where the package is delivered.
        """
        robot = self.robots[robot_id]

        # Find package location
        package_position = None
        for shelf, packages in self.shelves.items():
            if package in packages:
                package_position = shelf
                break

        if package_position is None:
            print("Package not found!")
            return

        # Step 1: Move to package location
        robot.move(package_position)

        # Step 2: Pick up package
        if self.pick_up(robot_id, package, package_position):
            print(f"{robot_id} successfully picked up {package} from {package_position}.")

        # Step 3: Transport to exit zone
        robot.move(destination)

        # Step 4: Drop off package
        if self.drop_off(robot_id, destination):
            print(f"{robot_id} successfully delivered {package} to {destination}.")