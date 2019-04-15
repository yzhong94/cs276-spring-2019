class InvertedIndexIterator(InvertedIndex):
    """"""
    def __enter__(self):
        """Adds an initialization_hook to the __enter__ function of super class
        """
#         print("entering a new iterator")
        super().__enter__()
#         print(self.index_file)
        self._initialization_hook()
        return self

    def _initialization_hook(self):
        """Use this function to initialize the iterator
        """
        ### Begin your code
        self.nums = 0
        self.index_file.seek(0)
        ### End your code

    def __iter__(self): 
        return self
    
    def __next__(self):
        """Returns the next (term, postings_list) pair in the index.
        
        Note: This function should only read a small amount of data from the 
        index file. In particular, you should not try to maintain the full 
        index file in memory.
        """
        '''(start_position_in_index_file, 
                                                  number_of_postings_in_list,
                                                  length_in_bytes)'''
        ### Begin your code
        

        '''
        self.nums = self.nums + 1
        print(self.index_file[0])
        #print("in try, returning",(self.terms[self.nums], self.postings_list[self.nums]) )
        '''

#         print("index file", self.index_file)
#         print("length of self.terms",len(self.terms))
        if self.nums >= len(self.terms):
            raise StopIteration
        else:
            super().__enter__()

            term_ID = self.terms[self.nums]
#             print("self.nums",self.nums)
#             print("posting term", term_ID)
#             print("posting meta data",self.postings_dict[term_ID])

            start_position_in_index_file, number_of_postings_in_list,length_in_bytes = self.postings_dict[term_ID]
            self.index_file.seek(start_position_in_index_file)
            posting_list = UncompressedPostings.decode(self.index_file.read(length_in_bytes))

            #print("current position of the stream",self.index_file.tell())
            self.nums = self.nums + 1
#             print("tuple",(term_ID,posting_list))
            return (term_ID,posting_list)
#         else:
#             print("enterring else clause in __next__")
#             self.__exit__(None, None, None)
#             #

                
        #return (self.terms[self.nums], self.postings_list[self.nums])
        ### End your code

    def delete_from_disk(self):
        """Marks the index for deletion upon exit. Useful for temporary indices
        """
        self.delete_upon_exit = True

    def __exit__(self, exception_type, exception_value, traceback):
        """Delete the index file upon exiting the context along with the
        functions of the super class __exit__ function"""
        self.index_file.close()
        if hasattr(self, 'delete_upon_exit') and self.delete_upon_exit:
            os.remove(self.index_file_path)
            os.remove(self.metadata_file_path)
        else:
            with open(self.metadata_file_path, 'wb') as f:
                pkl.dump([self.postings_dict, self.terms], f)
