# Test file for Artificial Intelligence CSE3812
# Run this file to test your local environment

# What version of Python do you have?
import sys

# Ignore if tensorflow.keras is not installed in case of using JetBrains Software
# Possible bug in PyCharm 2020.3.3
import tensorflow.keras
import pandas as pd
import sklearn as sk
import tensorflow as tf

print(f"Tensor Flow Version: {tf.__version__}")
print(f"Keras Version: {tensorflow.keras.__version__}")
print()
print(f"Python {sys.version}")
print(f"Pandas {pd.__version__}")
print(f"Scikit-Learn {sk.__version__}")
gpu = len(tf.config.list_physical_devices('GPU'))>0
print("GPU is", "available" if gpu else "NOT AVAILABLE")