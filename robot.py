class Robot:
    """
    Represents a robot capable of moving, picking up, and delivering packages in the warehouse.
    """
    def __init__(self, robot_id, position):
        """
        Initializes the robot.

        :param robot_id: Identifier of the robot.
        :param position: Position of the robot in the warehouse.
        """
        self.id = robot_id
        self.position = position
        self.package = None # The package currently carried by the robot

    def move(self, destination):
        """
        Moves the robot to a new location.

        :param destination: Target location.
        """
        print(f"{self.id} moves from {self.position} to {destination}.")
        self.position = destination

    def pick_up(self, package):
        """
        Assigns a package to the robot.

        :param package: Package identifier.
        """
        self.package = package
        print(f"{self.id} picks up {package}.")

    def drop_off(self):
        """
        Removes the package from the robot after delivery.
        """
        if self.package:
            print(f"{self.id} drops off {self.package}.")
            package = self.package
            self.package = None
            return package
        return None