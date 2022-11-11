import pickle

# cube = lambda x : x * x * x
# ave_pickle = pickle.dumps(cube)

# ###################################

# # pip install dill
# import dill 

# cube = lambda x: x * x * x
# ave_pickle = dill.dumps(cube)
# print(ave_pickle)

###############
# import math 
# import dill 

# square = lambda x: x * x 
# k = square(14)

# j = math.sqrt(196)

# dill.dump_session('sess.pkl')
# exit()

###############
# import dill

# globals().items()
# dill.load_session('sess.pkl')
# globals().items()

# print(k, j)

######## Compress of Pickled Objects

# import bz2

# ave_string = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
# when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
# It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
# It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
# and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

# pckld = pickle.dumps(ave_string)
# cmprsd = bz2.compress(pckld)
# len(ave_string)
# len(cmprsd)