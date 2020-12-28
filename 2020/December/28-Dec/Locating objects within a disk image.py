def find_file_within_image(self,path,objs = None):
    if objs is None:

        objs = self.adfsdisc.files

    if path == u"":

        #Special case for root directory
        return [u"/",objs,0,0,0]
    elements = path.split(u"/")

    elements = filter(lambda x: x != u"",elements)

    for this_obj in objs:

        if type(this_obj[1]) != type([]):

            #A file is found.

            obj_name = self.encode_name_from_object(this_obj)

            if obj_name == elements[0]:

                #A match between names.

                if len(elements) == 1:

                    #This is the last path element; we have found the
                    #required file
                    return this_obj
                else:

                    #There are more elements to satisfy but we can
                    #descewd no further.
                    return None

            elif self.adfsdisc.disc_type.find("adE") == -1 and \
                 elements[0] == obj_name + u".inf":

        "Continued..."

                if len(elements) == 1:

                    file_data = "%s\t%X\t%X\t%X\n" % \
                        tuple(this_obj[:1] + this_obj[2:])

                    new obj = \
                        (
                            this_obj[0] + ".inf",file_data,
                            0,0, len(file_data)
                        )

                    return new_obj

                else:

                    #There are more elements to satisfy but we can
                    #descend no further.
                    return None

        else:

            #A directory is found.
            obj_name = self.encode_name_from_object(this_obj)

            if obj_name == elements[0]:

                #A match between names.

                if len(elements) == 1:

                    #This is the last element; we have found the
                    #required file.
                    return this_obj

                else:

                    #More path elements need to be satisfied;descend
                    #further.
                    return self.find_file_within_image(
                        u"/".join(elementts[1:]), this_obj[1]
                        )
        return None
                        
                        
