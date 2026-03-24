import random

message = input("What is your message? ")
key_pair = int(input("What is your key? Please pick a number 1 or greater: "))
run_times = key_pair * 2
print("Message original:", message)

# converts each character to ascii, and adds 100 to each ascii value
message = [ord(c) + 100 for c in message]


# pushes array together, then for every int (determined by pair) adds random numbers
def obfuscate(msg, pair):
	nums = ""
	for n in msg:
		nums += str(n)
	obfuscated = ""
	for i in range(0, pair):
		obfuscated += str(random.randint(0, 9))
	for i in nums:
		obfuscated += str(i)
		for _ in range(0, pair):
			obfuscated += str(random.randint(0, 9))
	return obfuscated


message = obfuscate(message, key_pair)


# takes in a string of an integer
# outputs string derived from obfuscated ascii
def encrypt(a):
	if not len(a) % 2:
		a = a[:len(a) - 1]
	return ''.join(chr(int(j) + 22)for j in [str(i) for i in ([''.join(a) for a in zip(a[0::2], a[1::2])])])

message = encrypt(message)
print("Message after encryption:", message, "\n\n")
# message is in characters at this point

message = [str(ord(c)) for c in message]
count = 0
for i in message:
	if (len(str(int(i) - 22)) == 1):
		message[count] = '0' + str(int(i) - 22)
	else:
		message[count] = str(int(message[count]) - 22)
	count += 1


def deobfuscate(msg, pair):
	nums = ""
	for n in msg:
		nums += str(n)
	msg = nums
	ascii = []
	temp = ""
	i = pair
	while i < len(msg):
		temp += str(msg[i])
		i += pair + 1
		if (len(temp) == 3):
			ascii.append(int(temp))
			temp = ""
	return ascii


def translate(list):
	return ''.join([chr(n) for n in [n - 100 for n in list]])


message = deobfuscate(message, key_pair)

print(translate(message))
