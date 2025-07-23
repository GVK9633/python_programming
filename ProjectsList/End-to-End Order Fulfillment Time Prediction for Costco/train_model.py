import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load data
orders = pd.read_csv('costco_orders.csv')
warehouses = pd.read_csv('costco_warehouses.csv')

# Merge with warehouse data
orders = orders.merge(warehouses, on='warehouse_id')

# Feature engineering
orders['order_date'] = pd.to_datetime(orders['order_date'])
orders['order_month'] = orders['order_date'].dt.month
orders['order_dayofweek'] = orders['order_date'].dt.dayofweek
orders['order_hour'] = orders['order_date'].dt.hour

# Prepare features and target
X = orders.drop(['order_id', 'order_date', 'total_fulfillment_time_hrs', 'on_time'], axis=1)
y = orders['total_fulfillment_time_hrs']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing pipeline
numeric_features = ['num_items', 'total_weight', 'is_weekend', 'is_holiday', 'order_month', 'order_dayofweek', 'order_hour']
categorical_features = ['warehouse_id', 'membership_type', 'region', 'staff_level']

numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Model pipeline
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train model
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f} hours")
print(f"R2 Score: {r2_score(y_test, y_pred):.2f}")

# Save model
joblib.dump(model, 'costco_fulfillment_model.pkl')