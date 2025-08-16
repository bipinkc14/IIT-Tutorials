feed_time_reached = input("Is it feeding time? (yes/no): ").strip().lower() == "yes"
food_bin_contains_food = input("Is there food in the bin? (yes/no): ").strip().lower() == "yes"
weight_changed_after_feeding = input("Did the pet eat the food? (yes/no): ").strip().lower() == "yes"


dispense_motor = 0
alert_eat = 0
alert_bin = 0

# Logic based on inputs
if feed_time_reached:
    if not food_bin_contains_food:
        dispense_motor = 0
        alert_bin = 1
    else:
        dispense_motor = 1
        if not weight_changed_after_feeding:
            alert_eat = 1
else:
    dispense_motor = 0

print("\n--- Automated Pet Feeder Status ---")
print("Dispense Motor Activated:", "Yes" if dispense_motor else "No")
print("Alert: Pet Not Eating:", "Yes" if alert_eat else "No")
print("Alert: Bin Empty:", "Yes" if alert_bin else "No")
