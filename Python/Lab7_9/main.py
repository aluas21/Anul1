from ro.ubb.biblioteca.Repository.Imprumuturi_repository import Imprumut_repository
from ro.ubb.biblioteca.Repository.Repository import Repository
from ro.ubb.biblioteca.Repository.file_repository_clienti import FileRepositoryClienti
from ro.ubb.biblioteca.Repository.flie_repository_carti import FileRepositoryCarti
from ro.ubb.biblioteca.Repository.flie_repository_imprumuturi import FileRepositoryImprumuturi
from ro.ubb.biblioteca.Service.Carti_service import Carti_service
from ro.ubb.biblioteca.Service.Client_service import Client_service
from ro.ubb.biblioteca.Service.Clienti_carti_service import Clienti_carti_service
from ro.ubb.biblioteca.Service.Imprumuturi_service import Imprumut_service
from ro.ubb.biblioteca.Ui.console import Consola


def start():

    #--------FISISERE-------
    carte_repository = FileRepositoryCarti("ro/data/carti.txt")
    client_repoository = FileRepositoryClienti("ro/data/clienti.txt")
    imprumut_repository = FileRepositoryImprumuturi("ro/data/imprumuturi.txt")
    clienti_carti_repository = Repository()
    #--------MEMEORIE--------
    # clienti_carti_repository = Repository()
    # carte_repository = Repository()
    # imprumut_repository = Imprumut_repository()
    # clienti_carti_repository = Repository()
    clienti_carti_service = Clienti_carti_service(clienti_carti_repository,client_repoository, imprumut_repository)
    carte_service = Carti_service(carte_repository)
    client_service = Client_service(client_repoository)
    imprumut_service = Imprumut_service(imprumut_repository)
    consola = Consola(client_service, carte_service, imprumut_service, clienti_carti_service)

    consola.meniu()


start()
