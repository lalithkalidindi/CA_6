from vechile import Vechile
from Fleet import Fleet

def main():
    vehicle1 = Vehicle("1234564ASDFGHDCVH", 455.50)
    vehicle2 = Vehicle("146FYASDFBHUFT7FB", 525.95)
    vehicle3 = Vehicle("3FAHP0HA7AR987654", 670.80)
    
    
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
    
    

