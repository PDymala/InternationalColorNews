import random

import openai
from django.shortcuts import render
from django.utils import timezone

import uti


# Create your views here.
def index(request):
    words = ['university', 'professor', 'phd', 'scientists', 'machine learning', 'light bending',
             'start-up', 'cosmic', 'technology', 'computers', 'chemistry']
    openai.api_key = uti.access_secret_version('projects/125510501046/secrets/paintme_gpt')
    r_color = uti.random_color_rgb()
    r_color_hex = uti.rgb2hex(r_color[0], r_color[1], r_color[2])

    # noob code. refractor!
    mega_words = "Include "
    for i in range(0, 4):
        r_int = random.randint(0, len(words) - 1)
        if i == 0:
            mega_words += words[r_int]
        elif i == 3:
            mega_words += ", "
            mega_words += words[r_int]
            mega_words += "."
        else:
            mega_words += ", "
            mega_words += words[r_int]
        words.pop(r_int)

    name_prompt = f"Write a catchy name for color {r_color_hex}."
    name_response = openai.Completion.create(
        model="text-davinci-002",
        prompt=name_prompt,
        temperature=0.7,
        max_tokens=20,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    name = name_response['choices'][0]['text']

    poem_prompt = f"Write an article about discovery of new color {name}. {mega_words}"
    poem_response = openai.Completion.create(
        model="text-davinci-002",
        prompt= poem_prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    poem = poem_response['choices'][0]['text']

    # name_prompt = "Give a name for color ..."
    # poem_prompt = "write an article about..."
    # name = "Lavander blue"
    # poem = "Lavender blue is a new color that was discovered by a team of scientists at " \
    #        "the University of California, Berkeley. The team, led by professor of " \
    #        "chemistry Andrew Dittmer, used computers to analyze the chemical structure of " \
    #        "lavender blue and found that it is a previously unknown color. Lavender blue " \
    #        "is a deep purple color with a subtle blue hue. It is similar to the color of " \
    #        "lavender, but has a more saturated color. The new color was discovered when " \
    #        "the team was analyzing the chemical structure of lavender oil. The team used " \
    #        "a technique called nuclear magnetic resonance spectroscopy to study the " \
    #        "chemical structure of the oil. This technique is typically used to study " \
    #        "the structure of proteins, but the team was able to adapt it to study the " \
    #        "structure of lavender oil. The team's analysis showed that lavender blue is " \
    #        "a previously unknown color. The color is created by a compound in the oil " \
    #        "called linalool. This compound is responsible for the color of lavender, " \
    #        "but the team's analysis showed that it can also create a deep purple color. " \
    #        "The team's discovery was published in the journal Nature Chemistry."
    return render(request, 'index.html', {
        'color_hex': r_color_hex,
        'color': r_color,
        'poem': poem,
        'name': name,
        'date': timezone.now(),
        'name_prompt': name_prompt,
        'poem_prompt': poem_prompt
    })
