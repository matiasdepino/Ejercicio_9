import pickle
def store (data, filename):
    pickle.dump(data, open(filename, "wb"))
#pickle escribe en binario por eso se escribe wb
def retrive (filename) :
    try:
        f_o = open(filename, "rb")
    except:
        print("Error al abrir el archivo", filename)
        return None

    content = pickle.load(f_o)
    f_o.close()
    return content