class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        self.prob = prob
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''

def Calculate_Probability(data):
    symbols = dict()
    for ch in data:
        if symbols.get(ch) is None:
            symbols[ch] = 1
        else:
            symbols[ch] += 1
    return symbols

def Calculate_Codes(node, val=''):
    new_val = val + str(node.code)
    if node.left:
        Calculate_Codes(node.left, new_val)
    if node.right:
        Calculate_Codes(node.right, new_val)
    if not node.left and not node.right:
        codes[node.symbol] = new_val
    return codes

def Output_Encoded(data, encoding):
    encoded_output = ''
    for ch in data:
        encoded_output += encoding[ch]
    return encoded_output

def Total_Gain(data, encoding):
    before = len(data) * 8
    after = 0
    for ch in data:
        after += len(encoding[ch])
    return before, after

def Huffman_Encoding(data):
    symbol_with_probs = Calculate_Probability(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    print("symbols:", symbols)
    print("probabilities:", probabilities)
    nodes = []
    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.prob)
        right = nodes[0]
        left = nodes[1]
        left.code = 0
        right.code = 1
        newNode = Node(left.prob + right.prob, left.symbol + right.symbol, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
    global codes
    codes = dict()
    huffman_encoding = Calculate_Codes(nodes[0])
    print("symbols with codes", huffman_encoding)
    before, after = Total_Gain(data, huffman_encoding)
    print("Space usage before compression (in bits):", before)
    print("Space usage after compression (in bits):", after)
    encoded_output = Output_Encoded(data, huffman_encoding)
    print("Encoded output", encoded_output)

# ----------- Input ------------
data = "AAAAAAABCCCCCCDDEEEEE"
Huffman_Encoding(data)