import collections

class Solution(object):
    def evaluate(self, expression):
        tokens = collections.deque(expression.replace('(', ' ( ').replace(')', ' ) ').split())
        
        def helper(env):
            tok = tokens.popleft()
            if tok != '(':
                if tok.lstrip('-').isdigit():
                    return int(tok)
                for scope in reversed(env):
                    if tok in scope:
                        return scope[tok]
                return 0
            
            op = tokens.popleft()
            if op == 'let':
                env.append({})
                val = 0
                while True:
                    if tokens[0] == ')':
                        tokens.popleft()
                        break
                    if tokens[0][0].isalpha() and tokens[1] != ')':
                        var = tokens.popleft()
                        v = helper(env)
                        env[-1][var] = v
                    else:
                        val = helper(env)
                        tokens.popleft()
                        break
                env.pop()
                return val
            
            if op == 'add':
                a = helper(env)
                b = helper(env)
                tokens.popleft()
                return a + b
            
            if op == 'mult':
                a = helper(env)
                b = helper(env)
                tokens.popleft()
                return a * b
            
            return 0
        
        return helper([])
