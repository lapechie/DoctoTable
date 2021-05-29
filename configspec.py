def read_spec(file):
    """
    Returns a list of columns for each spec
    e.g [['Primary_Key', 'Feature_1', 'Feature_2', 'Feature_3'],
         ['Primary_Key', 'Feature_5', 'Feature_6', 'Feature_7']]
    """
    with open(file, "r") as specfile:
        lines = specfile.read().splitlines()
        spec_list = [line.split(",") for line in lines]
    return spec_list
