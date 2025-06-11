# workflow_scripts
Scripts I made to improve my workflow

#Run_selected
This script searches the active directory for files and submits them to slurm using sbatch. 
It prompts the user for the "suffix" which is the end of the file. For instance, type .s when prompted to run all .s files in the directory. 
It can interpret file names as well, so I could run all files ending in _v1.s by tyiping _v1.s when prompted

#make_smiles
Takes a .csv with a list of chemicals in a column named "Name" and appens a list of SMILES strings as another column using rdkit. Note, check the file as if the name is ambiguous it will not populate the SMILES column. It is recommended to put all of the names in quotes like "butane" so in the case of molecules like "2,2-dichlormethane", it doesn't split the name into two or more columns in the next step, going from SMILES to xyz.

#SMILES_to_xyz"
Takes a .csv with "Name" and "SMILES" columns and makes a .xyz file for each SMILES string using rdkit. Again, make sure each line has a SMILES string, and that the names are all in quotes, ex "butane",CCCC
