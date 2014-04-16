import sys

class Ids(object):
    '''
    ids: A class for taxonomic identifiers

    >>> pytaxize.Ids('Poa annua', db='col')
    '''
    def __init__(self, db):
        super(ids, self).__init__()
        self.db = db

        # get_colid(names, ...)

#   def classification(self):
#       print "shit"

def get_colid(sciname, ask = True, verbose = True):
  '''
  pytaxize.get_colid(sciname=['Poa annua'])
  '''
  def fun(sciname, ask, verbose):
    sciname = [sciname]
    df = col_search(name=sciname)
    
    if(df[0].shape[0] == 0):
      sys.exit("Retrieving data for taxon '" + sciname + "'")
      id = 'none'
    else:
      df = df[0][['id','name','rank','name_status']]
      df.columns = ['colid', 'name', 'rank', 'name_status']
      id = df['colid'].values.tolist()
    
    # not found on col
    if(len(id) == 0):
      sys.exit("Not found. Consider checking the spelling or alternate classification")
      id = 'none'
    
    # more than one found on col -> user input
    if(len(id) > 1):
        if(ask==True):
            print "\nMore than one eolid found for taxon '" + sciname[0] + "'\n"
            print df
            take = raw_input("\n Enter rownumber of taxon:\n\n")
            # take = raw_input("Enter rownumber of taxon: ")

            if(len(str(take)) == 0):
                take = 'notake'
            else:
                pass
            if(int(take) in range(df.shape[0])):
                take = int(take)
                print "Input accepted, took eolid '" + df['colid'][take] + "'.\n"
                id = int(df['colid'][take])
            else:
                id = 'none'
                print "\nReturned 'none'!\n\n"
        else:
            id = 'none'
    return id

  out = []
  for i in xrange(len(sciname)):
    out.append(fun(sciname[i], ask, verbose))
  
  return out

# def mssg(v): 
#   if(v) message(...)