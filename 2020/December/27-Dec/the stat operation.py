def stat(self,url):

    path = self.parse_url(url)

    if path is None:

        #Try redirecting to the protocol contained in the path.
        redir_url = KURL(url.path())
        self.redirection(redir_url)
        self.finished()
        #self.error(KIO.ERR_DOES_NOT_EXIST,url.path())
        return
    adfs_object = self.find_file_within_image(path)

    if not adfs_object:

        self.error(KIO.ERR_DOES_NOT_EXIST,path)
        return

    if type(adfs_object[1]) != type([]):

        entry = self.build_entry(adfs_object)

    elif path != u"" and path[-1] != u"/":

        #Directory referenced,but URL does not end in a slash.

        url.setPath(unicode(url.path()) + u"/")
        self.redirection(url)
        self.finished()
        return
    else:

        entry = self.build_entry(adfs_object)

        if entry != []:

            self.stateEntry(entry)

            self.finished()

        else:

            self.error(KIO.ERR_DOES_NOT_EXIST,path)
