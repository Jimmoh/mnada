def calculate_commission(t_sales, region_s, t_units):
    bonus = 0
    rate = 0.15 if region_s == "x" else 0.18 if region_s == "y" else 0.19 if region_s == "z" else 0
    if t_units > 300:
        t_units -= 300
        bonus = t_units * 10 if region_s == "x" else t_units * 15 if region_s == "y" else 0
    return (t_sales * rate) + bonus


def calculate_tax(commission):
    if commission > 25000:
        return commission * 0.1
    else:
        return 0


def main():
    region_x_sales = region_y_sales = region_z_sales = 0
    for x in range(50):
        print("Enter Name")
        s_name = input()
        print("Region of sale (x, y or z)")
        region = input()
        print("Units Sold")
        units = float(input())
        sales = units * 1200
        # Cumulative  sales
        if region == "x":
            region_x_sales += sales
        if region == "y":
            region_y_sales += sales
        if region == "z":
            region_z_sales += sales
        # Call functions
        commission = calculate_commission(sales, region, units)
        tax = calculate_tax(commission)
        net_commission = commission - tax
        # Output
        print(f"Name: {s_name}")
        print(f"Sales: {sales}")
        print(f"Commission: {commission}")
        print(f"Net Commission: {net_commission}")
    # Cumulative Output
    print(f"Total sales for region x: {region_x_sales}")
    print(f"Total sales for region y: {region_y_sales}")
    print(f"Total sales for region z: {region_z_sales}")


if __name__ == "__main__":
    main()

