# workflow_scripts
Scripts I made to improve my workflow

#Run_selected
This script searches the active directory for files and submits them to slurm using sbatch. 
It prompts the user for the "suffix" which is the end of the file. For instance, type .s when prompted to run all .s files in the directory. 
It can interpret file names as well, so I could run all files ending in _v1.s by tyiping _v1.s when prompted
