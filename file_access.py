# reads crewmate list form file
# expected format is one integer per line
# returns a list of integers
def read_crewmates_from_file(provided_filename):
    f = open(provided_filename, "r")
    staging = []
    for x in f:
        staging.append(int(x))
    return staging
