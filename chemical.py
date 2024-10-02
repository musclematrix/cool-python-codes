import pubchempy as pcp

# Take user input for the chemical name
chemicalName = input("Enter chemical name: ")

try:
    # Search PubChem for the compound by its name
    compound = pcp.get_compounds(chemicalName, 'name')[0]
    
    # Display information about the compound
    print(f"IUPAC Name: {compound.iupac_name}")
    print(f"Common Name: {compound.synonyms[0]}")
    print(f"Molecular Weight: {compound.molecular_weight}")
    print(f"Formula: {compound.molecular_formula}")
except IndexError:
    print(f"No information found for {chemicalName}.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
