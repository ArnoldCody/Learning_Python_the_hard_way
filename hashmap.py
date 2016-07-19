def new(num_buckets = 256):
	"""Initialized a map with the given number of buckets."""
	aMap = []
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap

def hash_key(aMap, key):
	"""Given a key this will create a number and then convert it to an index for the a Map's buckets."""
	return hash(key) % len(aMap)

def get_bucket(aMap, key):
	"""Given a key, find the bucket where it would go."""
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]

def get_slot(aMap, key, default = None):
	"""
	Returns the index, key, and value of a slot found in a bucket.
	Return -1, key, and the defult (None if not set) when not found
	"""
	bucket = get_bucket(aMap, key)
	print bucket

	for i, kv in enumerate(bucket): # if no more idem in sequence, skip for loop
		print i, kv
		k, v = kv
		if key == k:
			return i, k, v
			
	return -1, key, default

def get(aMap, key, default = None):
	"""gets the value in a bucket for the given key, or the default."""
	i, k, v = get_slot(aMap, key, default = default)
	return v

def set(aMap, key, value):
	"""sets the key to the value, replacing any existing value."""
	bucket = get_bucket(aMap, key)
	print bucket
	i, k, v = get_slot(aMap, key)
	print i, k, v


	if i >= 0:
		# the key exist, replace it
		bucket[i] = (key, value)
	else:
		# the key does not, append to create it
		bucket.append((key, value))
		print bucket[0]

def delete(aMap, key):
	"""deletes the given key from the Map"""
	bucket = get_bucket(aMap, key)

	for i in xrange(len(bucket)):
		k, v = bucket[1]
		if key == k:
			del bucket[i]
			break

def list(aMap):
	"""Prints out what's in the Map."""
	for bucket in aMap:
		if bucket:	
			for k, v in bucket:
				print k, v	