'''
The Python pickle module basically consists of four methods:

pickle.dump(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None)
pickle.dumps(obj, protocol=None, *, fix_imports=True, buffer_callback=None)
pickle.load(file, *, fix_imports=True, encoding="ASCII", errors="strict", buffers=None)
pickle.loads(bytes_object, *, fix_imports=True, encoding="ASCII", errors="strict", buffers=None)

'''

import pickle

class examples_class:
    number_example = 42
    string_example = "ave"
    list_example = [1, 2, 3]
    dict_example = {"uno": "1", "due": 2, "tre": [1, 2, 3]}
    tuple_example = (72, 74)

ave_object = examples_class()

ave_pickled_object = pickle.dumps(ave_object)  # Pickling the object
print(f"ave pickled object:\n{ave_pickled_object}\n")

ave_object.a_dict = None

ave_unpickled_object = pickle.loads(ave_pickled_object)  # Unpickling the object
print(
    f"dict_example (unpickled object):\n{ave_unpickled_object.dict_example}\n")

    