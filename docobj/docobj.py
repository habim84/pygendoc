
class DocObject:
    
    def __init__(self, file_name, doc_string):
        self.file_origin = file_name
        self.docstring = doc_string

    @property
    def file_origin(self):
        return self.__file_origin
    
    @file_origin.setter
    def file_origin(self, fileName):
        try:
            assert len(fileName) > 0, "filename supplied must not be empty."
            self.__file_origin = fileName
        except AssertionError as error:
            print("Could not set filename: "+repr(error))

    @property
    def docstring(self):
        return self.__docstring
    
    @docstring.setter
    def docstring(self, doc_string):
        try:
            tempArr = doc_string.split('\n')
            docArr = []
            for line in tempArr:
                if line != "":
                    docArr.append(line)
            assert len(docArr) > 0, "The docstring supplied was empty."
            self.__docstring = doc_string
        except AssertionError as error:
            print("Could not set doc string: "+repr(error))

class ClassDocObject(DocObject):
    
    def __init__(self, file_name, doc_string):
        self.__oneline = False
        self.__description = ""
        DocObject.__init__(file_name, doc_string)
    
    

    