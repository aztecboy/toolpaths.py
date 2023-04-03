




def init(Machine_Type,Axes): # Returns a class with all of the toolpath commands
    if Machine_Type=="mill":
        pass 

    else:

        raise Exception("Not a machine type")

    if Axes<=2:

        raise Exception("Cant have 2 or below axes")

    if Axes>=4:

        raise Exception("Cant have 4 or more axes")


    
         
    class TOOLPATH_FUNCTIONS:

        Machine=Machine_Type
        Toolpath=""
        Mode=None
        Feed_Rate=0
        def Set_Dimensions(Dimensions):

            if len(Dimensions)==Axes:
                pass 
            else:
                raise Exception("Cant set material dimensions with invalid amount of axes")


        def X(Location):

            if TOOLPATH_FUNCTIONS.Mode=="FEED":
                TOOLPATH_FUNCTIONS.Toolpath+="X "+str(Location)+"\n" 
            else:
                raise Exception("Cannot go to x, invalid mode")

        def Y(Location):

            if TOOLPATH_FUNCTIONS.Mode=="FEED":
                TOOLPATH_FUNCTIONS.Toolpath+="Y "+str(Location)+"\n"
            else:
                raise Exception("Cannot go to y, invalid mode")
        def Z(Location):

            if TOOLPATH_FUNCTIONS.Mode=="FEED":
                TOOLPATH_FUNCTIONS.Toolpath+="Z "+str(Location)+"\n"
            else:
                raise Exception("Cannot go to z, invalid mode") 

        def Feed():

            TOOLPATH_FUNCTIONS.Toolpath+="g01\n"
            TOOLPATH_FUNCTIONS.Mode="FEED"

        def Rapid():

            TOOLPATH_FUNCTIONS.Toolpath+="g00\n"
            TOOLPATH_FUNCTIONS.Mode="RAPID"
        
        def Set_Feed_Rate(Feed):

            TOOLPATH_FUNCTIONS.Feed_Rate=Feed
            TOOLPATH_FUNCTIONS.Toolpath+="F "+str(Feed)+"\n"
        class Material_Information:

            if Axes==3:
                Dimensions=[None,None,None]
        
        
    return TOOLPATH_FUNCTIONS


toolpath=init("mill",3)

toolpath.Feed()
toolpath.Set_Feed_Rate(15)
toolpath.Z(2.17)
toolpath.Set_Feed_Rate(60)
toolpath.X(5.0)
toolpath.Y(16.4500)
toolpath.Z(5.0)



print(toolpath.Toolpath)
