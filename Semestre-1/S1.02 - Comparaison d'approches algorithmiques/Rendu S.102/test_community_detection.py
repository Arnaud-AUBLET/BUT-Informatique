from community_detection import *

network = {
    "Alice" : ["Bob", "Dominique"],
    "Bob" : ["Alice", "Charlie", "Dominique"], 
    "Charlie" : ["Bob"], 
    "Dominique" : ["Alice", "Bob"]
}

list_of_friends = [
    'Muriel', 'Yasmine', 'Muriel', 'Joël', 'Yasmine', 'Joël', 'Yasmine',
    'Thomas', 'Joël', 'Nassim', 'Joël', 'Andrea', 'Joël', 'Ali', 'Thomas',
    'Daria', 'Thomas', 'Carole', 'Nassim', 'Andrea', 'Nassim', 'Ali', 'Andrea',
    'Ali', 'Thierry', 'Axel', 'Axel', 'Léo', 'Thierry', 'Léo', 'Léo',
    'Valentin', 'Valentin', 'Andrea'
]

def test_create_network():
    assert create_network(list_of_friends) == dico_reseau(list_of_friends)
    print('La fonction create_network() est Ok !')
    
def test_get_people():
    assert get_people(network) == ["Alice", "Bob", "Charlie", "Dominique"]
    print('La fonction get_people() est Ok !')

def test_are_friends():
    assert are_friends(network, 'Alice', 'Bob')
    assert not are_friends(network, 'Alice', 'Charlie')
    print('La fonction are_friends() est Ok !')

def test_all_his_friends():
    assert all_his_friends(network, 'Alice', ["Bob", "Dominique"])
    assert not all_his_friends(network, 'Alice', ["Bob", "Charlie"])
    print('La fonction all_is_friends() est Ok !')

def test_is_a_community():
    assert is_a_community(network, ["Alice", "Bob", "Dominique"])
    assert not is_a_community(network, ["Alice", "Bob", "Charlie"])
    print('La fonction is_a_community() est Ok !')

def test_find_community():
    assert find_community(network, ["Alice", "Bob", "Charlie", "Dominique"]) == ["Alice", "Bob", "Dominique"]
    assert find_community(network, ["Charlie", "Alice", "Bob", "Dominique"]) == ["Charlie", "Bob"]
    assert find_community(network, ["Charlie", "Alice", "Dominique"]) == ["Charlie"]
    print('La fonction find_community() est Ok !')

def test_order_by_decreasing_popularity():
    assert order_by_decreasing_popularity(network, ["Alice", "Bob", "Charlie"]) == ["Bob", "Alice", "Charlie"]
    print('La fonction order_by_decreasing_popularity() est Ok !')

def test_find_community_by_decreasing_popularity():
    assert find_community_by_decreasing_popularity(network) == ["Bob", "Alice", "Dominique"]
    print('La fonction find_community_by_dereasing_popularity() est Ok !')

def test_find_community_from_person():
    assert find_community_from_person(network, 'Alice') == ["Alice", "Bob", "Dominique"]
    assert find_community_from_person(network, 'Charlie') == ["Charlie", "Bob"]
    print('La fonction find_community_from_person() est Ok !')

def test_find_max_community():
    assert find_max_community(network) == ["Alice", "Bob", "Dominique"]
    print('La fonction find_max_commmunity() est Ok !')