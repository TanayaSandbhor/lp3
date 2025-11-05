class Item:
	def __init__(self, value, weight):
		self.value = value
		self.weight = weight

def fractionalKnapsack(W, arr):
	arr.sort(key=lambda x: (x.value / x.weight), reverse=True)
	final_value = 0.0
	for item in arr:
		if item.weight <= W:
			W -= item.weight
			final_value += item.value
		else:
			final_value += item.value * (W / item.weight)
			break
	return final_value

if __name__ == "__main__":
	W = 50
	arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
	max_val = fractionalKnapsack(W, arr)
	print("Maximum value in Knapsack =", max_val)
