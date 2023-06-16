##############
# SAE S01.01 #
##############

def liste_amis(amis, prenom):
    """
        Retourne la liste des amis de prenom en fonction du tableau amis.
    """
    prenoms_amis = []
    i = 0
    while i < len(amis)//2:
        if amis[2 * i] == prenom:
            prenoms_amis.append(amis[2*i+1])
        elif amis[2*i+1] == prenom:
            prenoms_amis.append(amis[2*i])
        i += 1
    return prenoms_amis

def nb_amis(amis, prenom):
    """ Retourne le nombre d'amis de prenom en fonction du tableau amis. """
    return len(liste_amis(amis, prenom))


def personnes_reseau(amis):
    """ Retourne un tableau contenant la liste des personnes du réseau."""
    people = []
    i = 0
    while i < len(amis):
        if amis[i] not in people:
            people.append(amis[i])
        i += 1
    return people

def taille_reseau(amis):
    """ Retourne le nombre de personnes du réseau."""
    return len(personnes_reseau(amis))

def lecture_reseau(path):
    """ Retourne le tableau d'amis en fonction des informations contenues dans le fichier path."""
    f = open(path, "r")
    l = f.readlines()
    f.close()
    amis = []
    i = 0
    while i < len(l):
        fr = l[i].split(";")
        amis.append(fr[0].strip())
        amis.append(fr[1].strip())
        i += 1
    return amis

def dico_reseau(amis):
    """ Retourne le dictionnaire correspondant au réseau."""
    dico = {}
    people = personnes_reseau(amis)
    i = 0
    while i < len(people):
        dico[people[i]] = liste_amis(amis, people[i])
        i += 1
    return dico

def nb_amis_plus_pop (dico_reseau):
    """ Retourne le nombre d'amis des personnes ayant le plus d'amis."""
    personnes = list(dico_reseau)
    maxi = len(dico_reseau[personnes[0]])
    i = 1
    while i < len(personnes):
        if maxi < len(dico_reseau[personnes[i]]):
            maxi = len(dico_reseau[personnes[i]])
        i += 1
    return maxi


def les_plus_pop (dico_reseau):
    """ Retourne les personnes les plus populaires, c'est-à-dire ayant le plus d'amis."""
    max_amis = nb_amis_plus_pop(dico_reseau)
    most_pop = []
    personnes = list(dico_reseau)
    i = 1
    while i < len(personnes):
        if len(dico_reseau[personnes[i]]) == max_amis:
            most_pop.append(personnes[i])
        i += 1
    return most_pop

##############
# SAE S01.02 #
##############

def create_network(list_of_friends):
    """
       fonction creer un nouveau resseau
       entrees : list_of_friends (tableau de couple d'ami)
       renvoie network (dictionnaire)
    """
    network = {}
    for i in range(0, len(list_of_friends)-1, 2):                       #boucle parcourant les indices 2 a 2
        if list_of_friends[i] not in network :                          #s'il n'existe pas on le creer avec son tableau d'ami
            network[list_of_friends[i]] = [list_of_friends[i + 1]]
        else:                                                           #sinon ajout prenom au tableau d'ami
            network[list_of_friends[i]].append(list_of_friends[i + 1])
        if list_of_friends[i + 1] not in network:                       #de meme pour le second prenom
            network[list_of_friends[i + 1]] = [list_of_friends[i]]
        else:
            network[list_of_friends[i + 1]].append(list_of_friends[i])
    return network

def get_people(network):
    """ 
       fonction determine les personnes presente
       entree : network (dictionnaire)
       renvoie le tableau des personnes
    """
    return list(network.keys()) #renvoie les cles de network (les prenoms)

def are_friends(network, person1, person2):
    """
       fonction determine si des personnes sont amis
       entrees : network (dictionnaire), person1 (str), person2 (str)
       renvoie booleen True si c'est le cas sinon False
    """
    return person1 in network[person2] #renvoie l'existance de person1 dans liste amis person2

def all_his_friends(network, person, group):
    """
       fonction determine si la personne est ami avec toute celle du groupe
       entrees : network (dictionnaire), person (str), group (tabeau)
       renvoie booleen True si c'est le cas sinon False
    """
    for persons in group:
        if persons != person:                                   #si prenom different du paramettre
            if are_friends(network, person, persons) == False:  #s'ils ne sont pas amis retourne False
                return False
    return True                                                 #sinon True

def is_a_community(network, group):
    """
       fonction determine s'ils sont tous amis entre eux
       entrees : network (dictionnaire), group (tableau d'amis)
       renvoie booleen True si c'est le cas sinon False
    """
    for name in group:                                      #boucle parcourant les prenoms du groupe
        if all_his_friends(network, name, group) == False:  #verifie s'il n'est pas amis avec toutes les menbres du groupe
            return False
    return True

def find_community(network, group):
    """
       fonction cherche communaute a partir d'un groupe
       entrees : network (dictionnaire), group (tableau d'amis)
       renvoie communaute (tableau) 
    """
    commu = []
    for name in group:
        rst = True
        for person in commu:
            if name != person:                            #si prenom different de celui en cours
                rst = rst and (name in network[person])   #verifie s'ils sont amis
        if rst:
            commu.append(name)                            #si oui ajout a commu
    return commu   



def order_by_decreasing_popularity(network, group):
    """
       fonction tri personne avec nombre amis decroissant
       entrees : network (dictionnaire), group (tableau d'amis)
       renvoir order_friend (tableau d'amis trie)
    """
    order_friend = []
    for k in range(len(group)):
        maxi = 0
        indmax = 0
        for i in range(len(group)):
            if len(network[group[i]]) > maxi:         
                maxi = len(network[group[i]])         #cherche nombre amis max
                indmax = i                            #et l'indice de la personne
        name = group.pop(indmax)                      #retire le prenom avec plus d'amis du groupe
        order_friend.append(name)                     #ajout a order_friend
    return order_friend

def find_community_by_decreasing_popularity(network):
    """
       fonction determine communaute trie par ordre ami decroissant
       entrees : network (dictionnaire
       renvoie commu trie (tableau d'amis trie)
    """
    community = order_by_decreasing_popularity(network, list(network.keys()))   #creer liste amis trie decroissant
    return find_community(network, community)                                   #cherche une communaute dans liste amis

def find_community_from_person(network, person):
    """
       fonction determine communaute plus grande avec person dedans
       entrees : network (dictionnaire), person (str)
       renvoie commu (tableau d'amis)
    """
    commu = [person]
    after = find_community(network, order_by_decreasing_popularity(network, network[person].copy())) #cherche autre personne de 
    for name in after:                                                                               #commu trie decroissant
        commu.append(name)                                                                           #ajout de chaque prenoms a commu
    return commu

def find_max_community(network):
    """
       fonction determine la plus grande communaute possible
       entrees : network (dictionnaire)
       renvoie commu_max (tableau d'amis)
    """
    commu_max = []
    for name in network:                                         #boucle des prenoms de network
        new_commu = find_community_from_person(network, name)    #creer une nouvelle communaute possible
        if len(new_commu) > len(commu_max):                      #regarde la plus grande et l'ajoute a commu_max
            commu_max = new_commu
    return commu_max