import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Streamlit UI
st.title("Spherical Coordinates Region Plotting")

# Sliders to select the range for r, theta, and phi with LaTeX labels
r_min, r_max = st.slider('Select the range for r', 0.0, 5.0, (1.0, 3.0))
theta_min, theta_max = st.slider('Select the range for $\\theta$ (polar angle, in units of $\\pi$)', 0.0, 1.0, (0.0, 0.5))
phi_min, phi_max = st.slider('Select the range for $\\phi$ (azimuthal angle, in units of $\\pi$)', 0.0, 2.0, (0.0, 1.0))

# Slider to adjust opacity
opacity = st.slider('Adjust opacity', 0.0, 1.0, 0.3)

# Convert theta and phi from units of pi to radians
theta_min *= np.pi
theta_max *= np.pi
phi_min *= np.pi
phi_max *= np.pi

# Function to convert spherical to cartesian coordinates
def spherical_to_cartesian(r, theta, phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return x, y, z

# Generate points for the mesh surfaces
def generate_mesh(r_vals, theta_vals, phi_vals):
    x, y, z = [], [], []
    for r in r_vals:
        for theta in theta_vals:
            for phi in phi_vals:
                xi, yi, zi = spherical_to_cartesian(r, theta, phi)
                x.append(xi)
                y.append(yi)
                z.append(zi)
    return x, y, z

# Generate points specifically for theta surfaces
def generate_theta_surface(theta, r_vals, phi_vals):
    x, y, z = [], [], []
    for r in r_vals:
        for phi in phi_vals:
            xi, yi, zi = spherical_to_cartesian(r, theta, phi)
            x.append(xi)
            y.append(yi)
            z.append(zi)
    return x, y, z

# Generate points specifically for phi surfaces
def generate_phi_surface(phi, r_vals, theta_vals):
    x, y, z = [], [], []
    for r in r_vals:
        for theta in theta_vals:
            xi, yi, zi = spherical_to_cartesian(r, theta, phi)
            x.append(xi)
            y.append(yi)
            z.append(zi)
    return x, y, z

# Define ranges with more dense grid
r_vals = np.linspace(r_min, r_max, 30)
theta_vals = np.linspace(theta_min, theta_max, 30)
phi_vals = np.linspace(phi_min, phi_max, 30)

# Create figure
fig = go.Figure()

# Add mesh for r = constant surfaces
for r in [r_min, r_max]:
    x, y, z = generate_mesh([r], theta_vals, phi_vals)
    fig.add_trace(go.Mesh3d(x=x, y=y, z=z, opacity=opacity, color='lightblue'))

# Add mesh for theta = constant surfaces
for theta in [theta_min, theta_max]:
    x, y, z = generate_theta_surface(theta, r_vals, phi_vals)
    fig.add_trace(go.Mesh3d(x=x, y=y, z=z, opacity=opacity, color='lightgreen'))

# Add mesh for phi = constant surfaces
for phi in [phi_min, phi_max]:
    x, y, z = generate_phi_surface(phi, r_vals, theta_vals)
    fig.add_trace(go.Mesh3d(x=x, y=y, z=z, opacity=opacity, color='lightcoral'))

# Update layout for better visualization
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        xaxis=dict(showspikes=False, showline=True, linewidth=2, linecolor='black', showgrid=False, zeroline=False),
        yaxis=dict(showspikes=False, showline=True, linewidth=2, linecolor='black', showgrid=False, zeroline=False),
        zaxis=dict(showspikes=False, showline=True, linewidth=2, linecolor='black', showgrid=False, zeroline=False)
    ),
    width=800,
    height=800
)

# Display the plot
st.plotly_chart(fig)
