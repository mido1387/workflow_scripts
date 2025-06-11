import pandas as pd
import pubchempy as pcp

# Read your CSV file
df = pd.read_csv("molecule_list.csv")

# Replace 'Name' with your actual column name
def name_to_smiles(name):
    try:
        compound = pcp.get_compounds(name, 'name')
        if compound:
            return compound[0].isomeric_smiles
    except:
        return None

df['SMILES'] = df['Name'].apply(name_to_smiles)

# Save to a new CSV file
df.to_csv("molecules_with_smiles.csv", index=False)
