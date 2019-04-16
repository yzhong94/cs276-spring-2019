class BSBIIndex(BSBIIndex):            
    def parse_block(self, block_dir_relative):
        """Parses a tokenized text file into termID-docID pairs
        
        Parameters
        ----------
        block_dir_relative : str
            Relative Path to the directory that contains the files for the block
        
        Returns
        -------
        List[Tuple[Int, Int]]
            Returns all the td_pairs extracted from the block
        
        Should use self.term_id_map and self.doc_id_map to get termIDs and docIDs.
        These persist across calls to parse_block
        """
        ### Begin your code
        td_pairs = []
        for filename in os.listdir(self.data_dir +'/'+ block_dir_relative):
            with open(self.data_dir +'/'+ block_dir_relative +'/'+ filename, 'r',encoding="utf8", errors='ignore') as f:
                
                doc_id = self.doc_id_map.__getitem__(filename)
                for s in f.read().split():
                    term_id = self.term_id_map.__getitem__(s)
                    td_pairs.append((term_id, doc_id))
        return td_pairs
        ### End your code
