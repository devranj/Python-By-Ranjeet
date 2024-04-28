import boto3
from datetime import datetime, timedelta

# Initialize a session using your AWS credentials
aws_session = boto3.Session()  # Use appropriate profile
cost_explorer = aws_session.client('ce', region_name='us-east-1')  # Adjust region if needed

# Function to get daily cost breakdown by service
def get_daily_costs(date):
    return cost_explorer.get_cost_and_usage(
        TimePeriod={
            'Start': date,
            'End': (datetime.strptime(date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
        },
        Granularity='DAILY',
        Metrics=['BlendedCost'],
        GroupBy=[
            {
                'Type': 'DIMENSION',
                'Key': 'SERVICE'
            }
        ]
    )

# Get the costs for two days
date_1 = (datetime.utcnow() - timedelta(days=2)).strftime("%Y-%m-%d")  # Two days ago
date_2 = (datetime.utcnow() - timedelta(days=1)).strftime("%Y-%m-%d")  # One day ago

costs_day_1 = get_daily_costs(date_1)
costs_day_2 = get_daily_costs(date_2)

# Extract costs by service for both days
service_costs_day_1 = {item['Keys'][0]: float(item['Metrics']['BlendedCost']['Amount']) for item in costs_day_1['ResultsByTime'][0]['Groups']}
service_costs_day_2 = {item['Keys'][0]: float(item['Metrics']['BlendedCost']['Amount']) for item in costs_day_2['ResultsByTime'][0]['Groups']}

# Find services that appeared in both days
common_services = set(service_costs_day_1.keys()).intersection(set(service_costs_day_2.keys()))

# Calculate the cost differences for common services
cost_difference = {service: service_costs_day_2[service] - service_costs_day_1[service] for service in common_services}

# Output the cost differences
print("Cost differences for each service (from two days ago to yesterday):")
for service, difference in cost_difference.items():
    print(f"{service}: {difference:.2f}")
