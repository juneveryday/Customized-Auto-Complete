__author__ = "June Jin"
__version__ = "10.18.3 [Done]"

import math

'''Question 1'''

class Node:
    def __init__(self, size = 27) -> None:
       
        '''
        Function description:
        Initialize a new node with the given ID.
        My reference is from the lecutre and tutorial FIT2004.
        
        Approach description:
        it will initialize the node with the given ID with the following attributes.

        Attributes:     
        link:       the list with the size of the number of alphabet + 1
        frequency:  the frequency of the word
        num_matches:the number of words in the dictionary that have the prefix (mutual letters)
        word:       the word
        definition: the definition of the word
        
        :Time complexity: O(1)
        :Aux space complexity: O(1) 
        '''
       
        # link to other nodes
        self.link = [None] * size

        # data payload
        self.frequency = 0

        # the number of words in the dictionary that have the prefix
        self.num_matches = 0

        # the word
        self.word = None

        # the definition of the word
        self.definition = None

class Trie:
    def __init__(self,dictionary) -> None:
        '''
        Function description:
        Initialize a Trie format.
        My reference is from the lecutre and tutorial FIT2004.
        
        Approach description:
        it will initialize the root node, with the following root.link attributes.
        after that, it will insert all the word and info in the dictionary into the trie.

        Attributes:

        root:       the root node of the trie

        :Time complexity: O(T) where T is the total number of characters in the dictionary
        :Aux space complexity: O(T) where T is the total number of characters in the dictionary
        '''
        # make the root node
        self.root = Node() 

        # insert all the word and info in the dictionary into the trie
        for info in dictionary:

            # info[0] is the word, info[1] is the definition, info[2] is the frequency
            self.insert(info[0],info[1],info[2])

    def insert(self,key,new_definition,frequency):
        '''
        Function description:

        A method that runs this function is to insert the key into the trie.
        When we found the correct location, it will update the frequency and definition of the node.

        While we are going down the path, will also update the num_matches of the node.

        Approach description:

        It will see the every character in the key, and insert the character into the trie in the index of the character linked list.
        If the character is already in the trie, it will go down the path.
        If the character is not in the trie, it will create a new node and go down the path.

        It will compare the frequency of the node with the new frequency.
        If the new frequency is bigger, it will update the frequency and definition of the node.

        :Input:
            argv1:  key
            - the word which will be inserted into the trie
            argv2:  new_definition
            - the definition of the word
            argv3:  frequency
            - the frequency of the word

        :Output, return: None

        :Time complexity: O (N), which N is the total number of characters in the word with the highest frequency 
        :Aux space complexity: O (N), which N is the total number of characters in the word with the highest frequency 
        '''

        # insert the key and data into the trie 
        current = self.root

        # store the new frequency for comparison later with the exist frequency
        new_frequency = frequency

        # go through till the end of the word
        for char in key:

            index = ord(char) - 97 + 1

            # if path exist, go down the path
            if current.link[index] is not None:
                current = current.link[index]

                # need to compare new frequency with the exist frequency

                if current.frequency < new_frequency or (current.frequency == new_frequency and current.word > key):
                    current.word = key
                    current.frequency = new_frequency
                    current.definition = new_definition

                # update the num_matches cuz we are going down the path later
                current.num_matches += 1

            # if path does not exist, create a new node and go down the path
            else:

                # make new node
                current.link[index] = Node()

                # go down the path
                current = current.link[index]
                
                # update the frequency and definition
                current.word = key
                current.definition = new_definition
                current.frequency = frequency
                current.num_matches = 1

    def prefix_search(self,key):
        '''
        Function description:

        A method that runs this function is to search the key in the trie.
        It will return the highest frequency word and its definition as well as the number of matches with the input prefix.

        Approach description:

        It will see the every character in the key.
        And it will search the character in the trie in the index of the character linked list.
        If the self.link in any of the character in the key is None, then there is no terminating node for the key. 
        If the self.link in any of the character in the key is not None, then there is a terminating node for the key.

        If the character is already in the trie, it will go down the path.
        If the character is not in the trie, it will return None.

        (Special case) 
        If the input is ("") and the path exist, 
        it will return the highest frequency word in the trie with the number of matches.
       
        :Input:
            argv1: key
            - the word that will be searched in the trie

        :Output, return:
        return the word and definition of the key with the number of matches.

        :Time complexity: O (M + N),
            where M is the length of the prefix entered by the user
            where N is the total number of characters in the word with the highest frequency
        :Aux space complexity: 
                          O (M + N)
        '''

        current = self.root

        num_matches = 0

        for char in key:

            index = ord(char) - 97 + 1

            # if the path exist, go down the path
            if current.link[index] is not None:
                current = current.link[index]

            # if the path does not exist, return None
            else:
                return [None, None, num_matches]

        # if the input is (""), return the highest frequency word in the trie
        if not len(key):

            # check current's links for the highest frequency word O(N)
            highest_frequency_index = 1

            for i in range(1,27):

                if current.link[i] is not None:
                    
                    # update the num_matches
                    num_matches += current.link[i].num_matches

                    # if the frequency is bigger, update the highest_frequency_index
                    if current.link[i].frequency > current.link[highest_frequency_index].frequency:
                        highest_frequency_index = i

            # return the highest frequency word
            return([current.link[highest_frequency_index].word,current.link[highest_frequency_index].definition,num_matches])

        # if the input is not ("") and the path exist, return the word and definition
        return([current.word,current.definition,current.num_matches])
