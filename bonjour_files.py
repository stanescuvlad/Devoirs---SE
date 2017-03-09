import sys, threading, logging, os

class Bonjour(threading.Thread):
    def __init__(self, personne):
        threading.Thread.__init__(self)
        self.personne = personne
    def run(self):
        #Fonction polie - saluer une personne
        print "Bonjour %(personne)s!\n" % \
          {"personne":self.personne},
        logging.info("Bonjour : %(personne)s" %{"personne":self.personne})
   
def utilisation():
    #Affichage mode d'utilisation
    mmeThread = []
    mThread = []
    mlleThread = []

    Liste_Noms = open("Liste_Noms.txt", "r")
    for ligne in Liste_Noms:
        if ligne[0:2] == "M.":
            mThread.append(Bonjour(ligne.strip(' \r\n')))
        elif ligne[0:4] == "Mme.":
            mmeThread.append(Bonjour(ligne.strip(' \r\n')))
        else:
            mlleThread.append(Bonjour(ligne.strip(' \r\n')))
        if ligne[0:6] == "Mlle.":
            mlleThread.append(Bonjour(ligne.strip(' \r\n')))
            mlle.start()
    for mlle in mlleThread:
        mlle.start()
        mlle.join()
    for mme in mmeThread:
        mme.start()
        mme.join()
    for m in mThread:
        m.start()
        m.join()
        

def main(argv = None):
    working_dir = os.path.dirname(os.path.abspath(__file__)) + os.path.sep
    #Configurez le logging pour ecrire dans un fichier texte
    logging.basicConfig(format = '%(asctime)s %(levelname)s %(message)s',
                        filename = working_dir + 'bonjour.log',
                        level = logging.INFO)    
    logging.info("Main start")
    
    #La boucle principale
    if argv is None:
        argv = sys.argv

    if len(argv) == 1:
        utilisation()
    else:
        #Argument 1 est le nom de fichier avec un noms per ligne
        mlleThread=[]
        mmeThread = []
        mThread = []
        with open(working_dir + argv[1],'r') as f:
            #Dites bonjour a chaque personne de fichier
            for ligne in f:
                if ligne[0:5] == "Mlle.":
                    mThread.append(Bonjour(ligne.strip(' \r\n')))
                elif ligne[0:4] == "Mme.":
                    mme_local = Bonjour(ligne.strip(' \r\n'))
                    mmeThread.append(mme_local)
                    mme_local.start()
                
        for mme in mmeThread:
            mme.join()
        for m in mThread:
            m.start()
            m.join()
    logging.info("Main stop")                
    return 0

if __name__ == "__main__":
    #Simplifiez la logique de la fonction principale
    sys.exit(main())
    sys.join(main())
    print "Finished"
