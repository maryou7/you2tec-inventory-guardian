def get_positive_float(prompt):
    while True:
        value = input(prompt).strip()
        try:
            value = float(value)
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Invalid number. Please enter a numeric value.")


def get_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def calculate_risk(days_of_supply):
    if days_of_supply < 15:
        return "High Risk", "Urgent reorder needed"
    if days_of_supply <= 30:
        return "Medium Risk", "Review and reorder soon"
    return "Low Risk", "No immediate action needed"


def format_result(data):
    width_left = 18
    width_right = 40
    divider = "+" + "-" * (width_left + 2) + "+" + "-" * (width_right + 2) + "+"

    lines = [divider]
    for label, value in data:
        lines.append(f"| {label:<{width_left}} | {value:<{width_right}} |")
        lines.append(divider)
    return "\n".join(lines)


def main():
    print("YOU2TEC Inventory Risk Monitor")
    print("--------------------------------")

    sku = get_non_empty_text("Enter SKU: ")
    product_name = get_non_empty_text("Enter Product Name: ")
    current_inventory = get_positive_float("Enter Current Inventory: ")
    average_daily_sales = get_positive_float("Enter Average Daily Sales: ")

    days_of_supply = current_inventory / average_daily_sales
    risk_level, recommended_action = calculate_risk(days_of_supply)

    result_data = [
        ("SKU", sku),
        ("Product Name", product_name),
        ("Current Inventory", f"{current_inventory:.2f}"),
        ("Average Daily Sales", f"{average_daily_sales:.2f}"),
        ("Days of Supply", f"{days_of_supply:.2f}"),
        ("Risk Level", risk_level),
        ("Recommended Action", recommended_action),
    ]

    print("\nInventory Risk Summary")
    print(format_result(result_data))


if __name__ == "__main__":
    main()
