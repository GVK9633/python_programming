import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configuration
NUM_ORDERS = 10000
START_DATE = datetime(2023, 1, 1)
END_DATE = datetime(2023, 12, 31)

# Generate synthetic products
products = pd.DataFrame({
    'product_id': range(1, 501),
    'category': np.random.choice([
        'Electronics', 'Grocery', 'Home', 'Appliances', 
        'Furniture', 'Clothing', 'Seasonal', 'Kirkland Signature'
    ], size=500),
    'weight_lbs': np.round(np.random.uniform(0.5, 50, size=500), 2),  # Weight in pounds
    'is_bulk': np.random.choice([0, 1], size=500, p=[0.3, 0.7]),  # 70% bulk items
    'is_perishable': np.random.choice([0, 1], size=500, p=[0.8, 0.2])  # 20% perishable
})

# Generate synthetic warehouses
warehouses = pd.DataFrame({
    'warehouse_id': range(1, 11),
    'region': np.random.choice(['West', 'Midwest', 'South', 'Northeast'], size=10),
    'capacity': np.random.randint(50000, 200000, size=10),  # Square footage
    'staff_level': np.random.choice(['Low', 'Medium', 'High'], size=10)
})

# Generate synthetic orders
def generate_orders(num_orders):
    orders = []
    for i in range(1, num_orders + 1):
        order_date = START_DATE + timedelta(days=random.randint(0, (END_DATE - START_DATE).days))
        warehouse = random.choice(warehouses['warehouse_id'].values)
        membership_type = random.choice(['Gold Star', 'Executive', 'Business'])
        is_weekend = 1 if order_date.weekday() >= 5 else 0
        is_holiday = 1 if order_date.month == 12 and order_date.day in range(15, 26) else 0  # Holiday season
        
        # Generate random fulfillment stages with timestamps
        processing_time = random.randint(1, 48)  # Hours
        picking_time = random.randint(1, 24)
        packing_time = random.randint(1, 12)
        shipping_time = random.randint(1, 72)
        
        total_time = processing_time + picking_time + packing_time + shipping_time
        
        orders.append({
            'order_id': i,
            'order_date': order_date,
            'warehouse_id': warehouse,
            'membership_type': membership_type,
            'num_items': random.randint(1, 20),
            'total_weight': round(random.uniform(5, 200), 2),
            'is_weekend': is_weekend,
            'is_holiday': is_holiday,
            'processing_time_hrs': processing_time,
            'picking_time_hrs': picking_time,
            'packing_time_hrs': packing_time,
            'shipping_time_hrs': shipping_time,
            'total_fulfillment_time_hrs': total_time,
            'on_time': 1 if total_time <= 48 else 0  # 48hrs SLA
        })
    return pd.DataFrame(orders)

orders_df = generate_orders(NUM_ORDERS)

# Save datasets
products.to_csv('costco_products.csv', index=False)
warehouses.to_csv('costco_warehouses.csv', index=False)
orders_df.to_csv('costco_orders.csv', index=False)
