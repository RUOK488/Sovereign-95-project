import pandas as pd
import os

class ConsumptionAnalyzer:
    def __init__(self, file_path: str = "data/sample_consumption.csv"):
        self.file_path = file_path
        self._initialize_storage()

    def _initialize_storage(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            df = pd.DataFrame({
                "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
                "Units_Consumed": [240, 190, 310, 420, 510, 480],
                "Total_Bill": [910.0, 735.0, 1205.0, 1710.0, 2175.0, 2015.0]
            })
            df.to_csv(self.file_path, index=False)

    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.file_path)

    def add_record(self, month: str, units: float, bill: float):
        df = self.load_data()
        new_row = pd.DataFrame({"Month": [month], "Units_Consumed": [units], "Total_Bill": [bill]})
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(self.file_path, index=False)

    def get_summary_statistics(self) -> dict:
        df = self.load_data()
        if df.empty:
            return {}
        return {
            "total_consumption": df["Units_Consumed"].sum(),
            "average_monthly_consumption": df["Units_Consumed"].mean(),
            "max_consumption": df["Units_Consumed"].max(),
            "min_consumption": df["Units_Consumed"].min(),
            "total_spent": df["Total_Bill"].sum()
        }
