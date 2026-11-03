from tabulate import tabulate
from src.models import TariffCalculator
from src.analyzer import ConsumptionAnalyzer
from src.visualizer import EnergyVisualizer

def main():
    calculator = TariffCalculator(fixed_charge=60.0)
    analyzer = ConsumptionAnalyzer()

    while True:
        print("\n==============================================")
        print("   ELECTRICITY BILL & ENERGY ANALYZER CLI     ")
        print("==============================================")
        print("1. Calculate Bill for Given Units")
        print("2. View Consumption History & Analytics")
        print("3. Log New Month Consumption Record")
        print("4. Visualize Usage Trends")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ").strip()

        if choice == "1":
            try:
                units = float(input("Enter total units consumed (kWh): "))
                breakdown = calculator.calculate_bill(units)
                print("\n--- Bill Breakdown ---")
                for k, v in breakdown.items():
                    print(f"{k}: ${v:.2f}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            df = analyzer.load_data()
            print("\n--- Consumption History ---")
            print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))
            
            stats = analyzer.get_summary_statistics()
            print("\n--- Summary Insights ---")
            print(f"Total Yearly Consumption: {stats['total_consumption']} kWh")
            print(f"Average Monthly Usage: {stats['average_monthly_consumption']:.2f} kWh")
            print(f"Peak Consumption: {stats['max_consumption']} kWh")
            print(f"Total Amount Spent: ${stats['total_spent']:.2f}")

        elif choice == "3":
            month = input("Enter Month (e.g., Jul, Aug): ").strip()
            try:
                units = float(input("Enter units consumed (kWh): "))
                breakdown = calculator.calculate_bill(units)
                bill = breakdown["Total Bill"]
                analyzer.add_record(month, units, bill)
                print(f"Successfully logged record for {month} with bill ${bill:.2f}!")
            except ValueError:
                print("Invalid input format. Please enter numeric values for units.")

        elif choice == "4":
            df = analyzer.load_data()
            if df.empty:
                print("No data available to plot.")
            else:
                print("Generating visual charts...")
                EnergyVisualizer.plot_trends(df)

        elif choice == "5":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()