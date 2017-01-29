# Xometry Code Challenge
This is a solution to the Xometry Code Challenge

1. Write a function that takes a mesh array (described below) and calculates the mesh's volume.
2. Write a unit test for the volume function in #1.
3. Write the title and text for a pull request you would open to merge this code.
4. Appropriately document the functions, modules, etc. you write as part of this code challenge.
5. Develop this code in a git repository.

# Installation

The setup script creates a virtualenv and installs the necessary dependencies.
```
bash setup.sh
```

# Example Usage
```
$ source venv/bin/activate
$ python volume/volume.py -f tests/examples/shell.npy
```

# Pull Request

From feature/volume_mesh to develop

Title: FEATURE: volume of polygon from npy file
* This is a feature to determine the volume of a polygon from a list of faces.
* Unit test uses 3 example .npy files.

# Testing
```
nosetests -c setup.cfg
```

#Linting

```
flake8 volume/ tests/
```

# Documentation
```
bash docs.sh
```

# Contact

Liz Theurer

jetheurer@gmail.com

352-672-0860
