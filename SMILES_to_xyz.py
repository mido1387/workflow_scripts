import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
import os
import re

# Load the CSV
df = pd.read_csv("molecules_with_smiles.csv")

# Column names
name_col = "Name"
smiles_col = "SMILES"

# Output directory
output_dir = "xyz_files"
os.makedirs(output_dir, exist_ok=True)

# Function to sanitize filename
def clean_name(name):
    name = name.replace('"', '')       # Remove quotes
    name = name.strip()                # Remove leading/trailing spaces
    name = name.replace(" ", "_")      # Replace spaces with underscores
    name = re.sub(r'[^\w\-]', '_', name)  # Remove/replace problematic symbols
    return name

# Function to generate and save .xyz from SMILES
def smiles_to_xyz(name, smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        print(f"[!] Failed to parse SMILES for {name}")
        return

    mol = Chem.AddHs(mol)
    if AllChem.EmbedMolecule(mol) != 0:
        print(f"[!] Embedding failed for {name}")
        return

    AllChem.UFFOptimizeMolecule(mol)

    conf = mol.GetConformer()
    num_atoms = mol.GetNumAtoms()

    filename = clean_name(name) + ".xyz"
    file_path = os.path.join(output_dir, filename)

    with open(file_path, "w") as f:
        f.write(f"{num_atoms}\n{name}\n")
        for atom in mol.GetAtoms():
            pos = conf.GetAtomPosition(atom.GetIdx())
            f.write(f"{atom.GetSymbol()} {pos.x:.6f} {pos.y:.6f} {pos.z:.6f}\n")

    print(f"[+] Wrote {file_path}")

# Loop through rows
for idx, row in df.iterrows():
    name = str(row[name_col])
    smiles = row[smiles_col]
    if pd.notnull(smiles):
        smiles_to_xyz(name, smiles)
