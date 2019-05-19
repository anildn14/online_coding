import sys

if __name__ == "__main__":
    meal_cost = float(raw_input().strip())
    tip_percent = int(raw_input().strip())
    tax_percent = int(raw_input().strip())
    total = int(round(meal_cost + ((meal_cost * tip_percent) / 100) + ((meal_cost * tax_percent) / 100)))
    # total=int(round(total))
    print (total)