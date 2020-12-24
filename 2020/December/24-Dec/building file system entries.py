def build_entry(self,obj):

    entry = []
    if type(obj[1] != type([]):

            #[name,data,load,exec,length]
            name = self.encode_name_from_object(obj)
            length = obj[4]
    "continued..."

            if self.adfsdisc.disc_type.find("adE") == -1 and \
                obj[0][-4:] == ".inf":

                #for .inf files,use a MIME type of text/plan.
                mimetype = "text/plain"

            else:

                #Let the client discover the MIME type by reading
                #the file.
                mimetype = None

    else:


        name = self.encode_name_from_object(obj)
        length = 0
        mimetype = "inode/directory"
    atom = KIO.UDSAtom()
    atom.m_uds = KIO.UDS_NAME
    atom.m_str = name

    entry.append(atom)

    atom = KIO.UDSAtom()
    atom.m_uds = KIO.UDS_SIZE
    atom.m_long = length

    entry.append(atom)

    atom = KIO.UDSAtom()
    atom.m_uds = KIO.UDS_MODIFICATION_TIME
    #Number of seconds since the epoch.
    atom.m_long = int(time.time())

    entry.append(atom)

    atom = KIO.UDSAtom()
    atom.m_uds = KIO.UDS_ACCESS
    #The usual octal permission information (rw-r--r-- in this case).
    atom.m_long = 0644

    entry.append(atom)

    #If the stat method is implemented then entries _must_ include
    #the UDE_FILE_TYPE atom or the whole system may not work at all.

    atom = KIO.UDSAtom()
    atom.m_uds = KIO.UDS_FILE_TYPE

    if mimetype != "inode/directory":

        atom.m_long = os.path.stat.S_IFREG

    else:

        atom.m_long = os.path.stat.S_IFDIR

    entry.append(atom)

    if mimetype:

        atom = KIO.UDSAtom()
        atom.m_uds = KIO.UDS_MIME_TYPE
        atom.m_str = mimetype

        entry.append(atom)

    return entry

            
