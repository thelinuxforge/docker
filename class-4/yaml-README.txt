1. How many array keys are there in the following yaml snippet?
 {
    "Fruits": [
        "Orange",
        "Apple",
        "Banana"
    ],
    "Vegetables": [
        "Carrot",
        "Cauliflower",
        "Tomato"
    ]
}

Using above json file please try to write yaml file

Answer:->

Fruits:
  - Orange
  - Apple
  - Banana
Vegetables:
  - Carrot
  - CauliFlower
  - Tomato

2. Which of the following statements is true?

A. Dictionary is an unordered collection whereas list is an ordered collection.
B. Dictionary is an ordered collection whereas list is an unordered collection.
C. Dictionary and list, both are an ordered collection.
D. Dictionary and list, both are an unordered collection.

Answer:-> B

3. practice.yaml file with the key name and value apple. Add some additional properties (given below) to the dictionary.
-> practice.yaml
   name= apple

   properties ->   color= red
                   weight= 90g
   
Answer:->
   name: apple
   color: red
   weight: 90g


4. practice.yaml file with a dictionary named employee. Add the remaining properties to it using 
   information from the table below.

-> practice.yaml
   Key/Property	   Value
   name	           john
   gender	       male
   age	           24

Answer:->
   employee:
     name: john
     gender: male
     age: 24

5. practice.yaml file with a dictionary in dictionary. Add a dictionary named address to add the 
   address information in this file.
- > practice.yaml
    Key/Property	Value
    city	        edison
    state	        new jersey
    country	        united states

Add above details in below yaml code
    employee1:
      name: john
      gender: male
      age: 24

Answer:->
    employee1:
      name: john
      gender: male
      age: 24
      address:
         city: edison
         state: new jersey
         country: united state

6. practice.yaml file with some data for apple, orange and mango. Just like apple, we would like to 
   add additional details for each item, such as color, weight etc. Modify the remaining items to 
   match the below data.
-> practice.yaml
   - name: apple
     color: red
     weight: 100g

orange
color	weight
orange	90g

mango
color	weight
yellow	150g

Answer:->
   - name: orange
     color: orange
     weight: 90g   
   - name: mango
     color: yellow
     weight: 150g

7. practice.yaml file with a dictionary named employee. We would like to record information about multiple employees. Convert the dictionary named employee to an array named employees.
-> practice.yaml
   employees:
     - name: john
       gender: male
       age: 24

Key/Property	Value
name	        sarah
gender	        female
age	            28


Answer:->
  employees:
    - name: john
      gender: male
      age: 24
    - name: sarah
      gender: female
      age: 28

8. practice.yaml file to add some more details. Now add the pay information. Remember, while address 
   is a dictionary, payslips is an array of month and amount.
->
   payslips
   month	amount
   june	1400
   july	2400
   august	3400

-> practice.yaml
  employee:
    name: john
    gender: male
    age: 24
    address:
      city: 'edison'
      state: 'new jersey'
      country: 'united states'

Answer:->
  employee:
    name: john
    gender: male
    age: 24
    address:
      city: 'edison'
      state: 'new jersey'
      country: 'united states'
    payslip:
    - month: June
      amount: 1400
    - month: July
      amount: 2400
    - month: august
      amount: 3400
