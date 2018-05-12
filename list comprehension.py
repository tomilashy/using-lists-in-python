
name = [1,2,3,4,5,6,7,8,9];
odd=[x for x in name if x%2!=0 ];
even=[x for x in name if x%2==0 ];
print (odd,even);

edit=[x if x%2==0 else x*2 for x in name  ];

print (edit);

mixed="This is jesutomi";

vowels=', '.join(v for v in mixed if v in "aeiou");
print (vowels);

nested_list=[[1,2,3],[4,5,6],[7,8,9]];

print(nested_list[0][-1]);

for first in nested_list:
    for second in first:
        print (second)

#printing odd values with nested list comprehension

[[print (second) for second in first if second%2  != 0] for first in nested_list ]