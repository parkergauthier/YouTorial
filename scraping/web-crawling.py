import api
import pandas

GET https://www.googleapis.com/youtube/v3/videos


search_list = ['jump start car', 'change oil', 'change tire', 'change car battery', 'drive car', 'drive stick', 'drive manual', 'parellel park',  ,'apply eyeliner', 'apply lipstick',  'apply foundation', 'apply mascara', 'apply blush',  'code python', 'code R', 'code C+', 'code Javascript', 'code Pandas', 'code SQL', 'photoshop', 'video edit', 'program', 'make popcorn', 'make rice', 'cook spagetti', 'cook steak', 'dice onion', 'chop onion', 'bake potatoes', 'bake cookies', , 'mince garlic']

def search_terms(list):
    for i in list:
        