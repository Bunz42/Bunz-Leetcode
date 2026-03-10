# 32 - Time Based Key-Value Store

**Difficulty:** Medium | **Link:** https://neetcode.io/problems/time-based-key-value-store/question

## 1. Problem Description
```text
Implement a time-based key-value data structure that supports:

Storing multiple values for the same key at specified time stamps
Retrieving the key's value at a specified timestamp
Implement the TimeMap class:

TimeMap() Initializes the object.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the
most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp).
If there are no values, it returns "".
Note: For all calls to set, the timestamps are in strictly increasing order.
```

**Example 1:**
```text
Input:
["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]

Output:
[null, null, "happy", "happy", null, "sad"]

Explanation:
TimeMap timeMap = new TimeMap();
timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
timeMap.get("alice", 1);           // return "happy"
timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
timeMap.get("alice", 3);           // return "sad"
```

**Constraints:**
```text
1 <= key.length, value.length <= 100
key and value only include lowercase English letters and digits.
1 <= timestamp <= 1000
```

## 2. My Approach
```text
This problem is just a class design problem. It is recommended that I solve this
with a time complexity of O(1) for the set() function and O(logn) for the get() fcn.

Let's start with the initialization of the object. The point of this class
is to create a map that stores key-value pairs, so I'm going to just initialize this
"TimeMap" as a hash table/dictionary in python.

However, since I need to store 3 values instead of 2, I'm going to make the values a tuple
instead of a single value, which is going to be the value-timestamp pair specified in the
problem. But, I also need to consider the fact that a key can be set multiple times, so I 
actually need to link the key to an array of tuples, which I add to whenever the set() method
is called.

The set() function is just going to add elements to the hashmap in the form 
key, [(value1, timestamp1), (value2, timestamp2), etc.].
Adding elements to a hashmap is O(1) so this fulfills the requirements.

The get() function is a little more complicated. The brute force implementation would be to just
iterate through the map linearly, checking all the values and their associated timestamps and comparing
it to the given timestamp, then just taking the maximum valid timestamp. However, there's a
faster way to do this. 

I can just binary search through the timestamps, since the problem states
that they're guaranteed to be in strictly increasing order, meaning they're sorted. So, I'm
basically finding the maximum timestamp with a clear upper bound of the given parameter, and a
lower bound of 1.

How do I implement this?
Since I have an array of set() calls for each key. If the key doesn't exist in the hashmap, I can 
just immediately return "".

If the key does have values associated with it, it means the set function was called on it previously.
Now, I can just binary search through the array and find the biggest timestamp that is still less
than the given timestamp restriction.

Now, the problem is just simple binary search. I define my left and right and find the middle. Then,
I first check if it's less than or equal to the given restriction. This means that
the middle timestamp could be a potential candidate, so I record its value in a max variable, then throw away
the left half and search the right half, in case there's better candidates there. There can't be any
other candidates in the left half, because those are all less recent than the middle one, and since the
middle one already works in this case, we can disregard the rest of the left half.

Note: the max variable will have a default string of "", in case no valid timestamps are found.

In the case where the middle timestamp is actually greater than the restriction, it means we need
to find a lower value so that the restriction is actually satisfied. So, we throw away the right half
and search the left.

Repeat this, then return the value associated with the max timestamp at the end. This satisfies the
O(logn) complexity specification.
```

