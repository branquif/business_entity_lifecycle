import yaml

matrix = open('./db/state_matrix.yaml', 'r')

print(yaml.load(matrix))
print("\n\n")

