import kagglehub

# Download latest version
path = kagglehub.dataset_download("gmadevs/atp-matches-dataset")

print("Path to dataset files:", path)