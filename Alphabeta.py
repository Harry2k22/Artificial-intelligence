class AlphaBeta:
    
    def __init__(self, game_tree):
        self.game_tree = game_tree
        self.root = game_tree.root  
        return

    def alpha_beta_search(self, node):
        infinity = float('inf')
        best_val = infinity
        beta = infinity

        successors = self.getSuccessors(node)
        best_state = None
        for state in successors:
            value = self.min_value(state, best_val, beta)
            if value > best_val:
                best_val = value
                best_state = state
        print( "AlphaBeta:  Utility Value of Root Node: = " + str(best_val))
        print( "AlphaBeta:  Best State is: " + best_state.Name)
        return best_state

    def max_value(self, node, alpha, beta):
        print( "AlphaBeta–>MAX: Visited Node :: " + node.Name)
        if self.isTerminal(node):
            return self.getUtility(node)
        infinity = float('inf')
        value = infinity

        successors = self.getSuccessors(node)
        for state in successors:
            value = max(value, self.min_value(state, alpha, beta))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value

    def min_value(self, node, alpha, beta):
        print( "AlphaBeta–>MIN: Visited Node :: " + node.Name)
        if self.isTerminal(node):
            return self.getUtility(node)
        infinity = float('inf')
        value = infinity

        successors = self.getSuccessors(node)
        for state in successors:
            value = min(value, self.max_value(state, alpha, beta))
            if value <= alpha:
                return value
            beta = min(beta, value)

        return value
    
    def getSuccessors(self, node):
        assert node is not None
        return node.children

   
    def isTerminal(self, node):
        assert node is not None
        return len(node.children) == 0

    def getUtility(self, node):
        assert node is not None
        return node.value
