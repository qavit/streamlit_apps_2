import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Create a title
st.title("K-means Clustering Demo")

# Sidebar sliders for parameters
n_samples = st.sidebar.slider("Number of samples", 100, 1000, 300)
n_features = st.sidebar.slider("Number of features", 2, 10, 2)
n_clusters = st.sidebar.slider("Number of clusters", 2, 10, 3)
k = st.sidebar.slider("K (number of clusters)", 1, 10, 3)
random_state = st.sidebar.slider("Random State", 0, 100, 42)

# Button to regenerate data and rerun K-means
if st.button("Regenerate Data and Re-run K-means"):
    # Generate a new sample dataset
    X, _ = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, random_state=random_state)
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    y_kmeans = kmeans.predict(X)
    
    # Calculate metrics
    inertia = kmeans.inertia_
    silhouette_avg = silhouette_score(X, y_kmeans)
    
    # Display metrics
    st.write(f"Inertia: {inertia:.2f}")
    st.write(f"Silhouette Score: {silhouette_avg:.2f}")
    
    # Plot the clustering results
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X')
    plt.title(f"K-means Clustering with K={k}")
    st.pyplot(plt)
else:
    st.write("Click the button to generate new data and run K-means clustering.")
