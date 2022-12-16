'''
python dictionary is an ordered collection of items.
it stores elements in key/value pairs.
keys are unique identifiers that are linked with each value.
'''

capital_city = {
    'Nepal' : 'Katmandu',
    'France' : 'Paris',
    'England' : 'London'
}

print(capital_city)

# accessing elements from dictionary
print(capital_city['Nepal'])

# loops through dictionary
for row in capital_city:
    print(row)