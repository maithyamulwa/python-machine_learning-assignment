from collections import Counter
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Dataset: [Monthly Spending (KES), Monthly Visits]
data = [
    [1000, 2],  # Customer 1
    [1500, 3],  # Customer 2
    [2000, 2],  # Customer 3
    [5000, 6],  # Customer 4
    [6000, 7],  # Customer 5
    [5500, 5],  # Customer 6
    [12000, 12],  # Customer 7
    [15000, 14],  # Customer 8
    [13000, 11],  # Customer 9
    [3000, 4],  # Customer 10
]

# Step 4: Scale the spending and visits features
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Step 5 & 6: Create K-Means model with n_clusters=3, random_state=42, n_init=10
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

# Step 7: Train the model and assign clusters
clusters = kmeans.fit_predict(scaled_data)

# Step 8: Display the cluster assigned to each customer
for i, cluster_id in enumerate(clusters, start=1):
  print(f"Customer {i} belongs to Cluster {cluster_id}")

print("-" * 40)

# Step 9: Display the total number of customers in each cluster
cluster_counts = Counter(clusters)
for cluster_id in sorted(cluster_counts.keys()):
  print(f"Cluster {cluster_id}: {cluster_counts[cluster_id]} customer(s)")

# Bonus Task: Matplotlib Scatter Plot showing customer groups in different colors
spending = [row[0] for row in data]
visits = [row[1] for row in data]

plt.figure(figsize=(8, 5))
scatter = plt.scatter(
    spending, visits, c=clusters, cmap="viridis", s=120, edgecolor="k", alpha=0.8
)
plt.title("Customer Segmentation Using K-Means Clustering")
plt.xlabel("Monthly Spending (KES)")
plt.ylabel("Monthly Visits")
plt.grid(True, linestyle="--", alpha=0.5)

# Add a colorbar legend for the clusters
plt.colorbar(scatter, label="Cluster ID")
plt.show()
