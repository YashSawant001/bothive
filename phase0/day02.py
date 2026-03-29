name = "Yash"
city = "Pune"

message ="Hello to BotHive"

print(name.upper())
print(city.lower())

print(message[0])
print(message[-1])

print(message[0:5])
print(message[-1:0:-2])

new_message = message.replace("BotHive", "AI Platform")
print(new_message)

words = message.split(" ")
print(words)

joined = "-".join(words)
print(joined)