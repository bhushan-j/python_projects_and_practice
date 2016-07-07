class PatMatch :
   def __init__ (self):
       self.patterns = []       # To match
       self.working  = [0]*50   # Partial matches
       self.worktop  = 0        # Limit for partials
       self.nMatches = 0        # Number matches found so far

   def addPattern(self, pattern, callBack) :
       # Add a pattern with its call back function
       self.patterns.append( (pattern, len(pattern), callBack) )

   def reset (self) :
       # Cancel all partial matches
       self.worktop = 0
       self.nMatches = 0

def seeChar (self,ch) :
    # a new char to be handled
    # if char starts a pattern - add it to top of workspace
    for p in self.patterns :
        if ch == p[0][0] :
            # partial match has pattern pointer and # chars matched
            self.working[self.worktop] = [p, 0]
            self.worktop += 1

    # scan through work area to adjust to char ch
    wp = wk = 0                   #
    while wp < self.worktop :
        # wpat is pattern, wcp chars matched so far
        wpat,wcp = self.working[wp]
        if wpat[0][wcp] == ch :
            # new character continues the match
            wcp += 1
            if wcp >= wpat[1] :
                # Oh. the new char has completed match
                wpat[2](wpat[0])   # Do the call back
                self.nMatches += 1
            else :
                # Still more to match. tuck partial match in
                self.working[wk] = (wpat,wcp)
                wk += 1  # Adjust new worktop, keeping partial
        wp += 1
    self.worktop = wk    # set worktop to matches kept