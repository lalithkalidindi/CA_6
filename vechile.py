class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, year):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.year = year

    def __str__(self):
        return f"ID: {self.vehicle_id}, Type: {self.vehicle_type}, Year: {self.year}"


class Fleet:
    def __init__(self):
        self.vehicles = {}

    def add_vehicle(self, vehicle_id, operating_cost, status):
        self.vehicles[vehicle_id] = {
            "operating_cost": operating_cost,
            "status": status
        }

    def total_operating_cost(self):
        return sum(
            vehicle["operating_cost"]
            for vehicle in self.vehicles.values()
        )

    def active_vehicle_count(self):
        return sum(
            1
            for vehicle in self.vehicles.values()
            if vehicle["status"] == "Active"
        )

    def __str__(self):
        result = ""
        for vehicle_id, info in self.vehicles.items():
            result += (
                f"Vehicle ID: {vehicle_id}, "
                f"Cost: ${info['operating_cost']:.2f}, "
                f"Status: {info['status']}\n"
            )
        return result


def main():
    
    vehicle1 = Vehicle("V001", "Truck", 2022)
    vehicle2 = Vehicle("V002", "Van", 2021)
    vehicle3 = Vehicle("V003", "SUV", 2023)

    
    fleet = Fleet()

    
    fleet.add_vehicle(vehicle1.vehicle_id, 120.25, "Active")
    fleet.add_vehicle(vehicle2.vehicle_id, 150.80, "Maintenance")
    fleet.add_vehicle(vehicle3.vehicle_id, 175.50, "Active")

    print("Fleet Information")
    print(fleet)

    print("Total Operating Cost:", fleet.total_operating_cost())
    print("Active Vehicles:", fleet.active_vehicle_count())


if __name__ == "__main__":
    main()