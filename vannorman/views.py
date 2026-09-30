import json
import uuid
import urllib
import datetime
import re 
import requests # for setting cookies

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import RedirectView
from django.utils import timezone
from django.contrib import auth
#from django.forms.util import ErrorList
from django.template.context import RequestContext
from django.shortcuts import render
from django.shortcuts import render, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

import markdown
md = markdown.Markdown()

#import requests

from vannorman.util import *
def simple_page(template):
    def handler(request):
        return renderWithNav(request, template)
    return handler

def file_a(request):
    return HttpResponse("7GN_wPd4X1PrCxmqKOrw9sHsAd0_uayFhOnWdEw6Ytc.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")
def file_b(request):
    return HttpResponse("v9b5S4UbuLtvh_PwuhqjfOUnVfiulJSmFCYkNHtD6mA.myqbUoOfbuYMTb3HuxVonYYuwHgoAV2835bCeWTwqkY")




def blog_base(request):
    return blog(request,None)

def blog(request,blog):
    if blog is None:
        obj = {}
        obj['blogs'] = []
        obj['blogs'].append(
        {
            "url":"while-vr-for-consumer-lags-corporate-training-booms.html",
            "title":"While VR for consumers lags, Corporate Training booms",
                        "description":"My views on the current market, and why I'm long on corporate VR ahead of consumer VR by 10-20 years.",
            "date":"Jan 14, 2018"
        })
        obj['blogs'].append(
        {
            "url":"virtual-reality-bridges-gamer-gap.html",
            "title":"Virtual Reality Bridges the Gamer Gap",
                        "description":"By getting out of the way of human users, VR paves the way for seameless HCI.",
            "date":"Mar 25, 2018"
        })
        obj['blogs'].append(
        {
            "url":"freedom-from-the-tyrants-deep-monkey.html",
            "title":"Freedom From The Tyrants",
                        "description":"Everyone knows tech giants rule us, but you will have more options in the future.",
            "date":"Mar 27, 2018"
        })

        obj['blogs'].append(
        {
            "url":"sustainable-futures-are-collaborative-not-adversarial.html",
            "title":"Sustainable Futures Are Collaborative Not Adversarial",
                        "description":"My unsupported arguments for world piece, rooted in capitalism.",
                        "date":"April 7, 2018"
        })

        obj['blogs'].append(
        {
            "url":"spacefrogvr.html",
            "title":"Space Frog VR",
                        "description":"A brief look at my first full-length VR title.",
                        "date":"Mar 17, 2019"
        })

        obj['blogs'].append(
        {
            "url":"redefinelearning.html",
            "title":"Redefine Schools and Learning",
                        "description":"Schools do not set students up for success in today's world. Here's what I plan to change.",
                        "date":"Sep 20, 2020"
        })

#       {
#           "url":"these-vr-startups-are-rocking-the-medical-world.html",
#           "title":"[IN PROGRESS] These VR Startups are rocking the medical world",
#           "date":"Feb 6, 2018"
#       })


        obj['blogs'].reverse()
        return renderWithNav(request,"blogbase.html",obj)
    else:
        return renderWithNav(request,"blog/"+blog)

def render_md_blog(request):
    with open('vannorman/templates/blog/redefinelearning.md', 'rb') as fp:
        v = fp.read()
        v = md.convert(v)
        obj = {}
        obj['html_text'] = v
        return renderWithNav(request,"render_md_blog.html", obj)


def jammer(request):
    obj = {}
    obj['videos'] = []
    obj['videos'].append({
        "url" : "https://www.youtube.com/watch?v=ogH7yrA-fHc",
        "id" : "ogH7yrA-fHc",
        "hotkey" : "F",
        "keycode" : 102
    })
    obj['videos'].append({
        "url" : "https://www.youtube.com/watch?v=2EUOYON3eZg",
        "id" : "2EUOYON3eZg",
        "hotkey" : "J",
        "keycode" : 106
    })
    obj['videos'].append({
        "url" : "https://www.youtube.com/watch?v=kuMY2X22PHA",
        "id" : "kuMY2X22PHA",
        "hotkey" : "D",
        "keycode" : 100
    })
    obj['videos'].append({
        "url" : "https://www.youtube.com/watch?v=2EUOYON3eZg",
        "id" : "2EUOYON3eZg",
        "hotkey" : "S",
        "keycode" : 115
    })
    obj['videos'].append({
        "url" : "https://www.youtube.com/watch?v=mKYb7Juflz0",
        "id" : "mKYb7Juflz0",
        "hotkey" : "A",
        "keycode" : 97
    })
    return renderWithNav(request,'jammer.html', obj)
    
from django.shortcuts import render


def home(request):
    obj = {}

    obj['profile'] = {
        "name": "Charlie Van Norman",
        "first_name": "Charlie",
        "headline": "I build and sell technology people love.",
        "summary": "Founder and software engineer. 15+ years across enterprise systems, VR training, 3D edtech games, and AI platforms.",
        "availability": "Open to founding, sales, and engineering roles.",
        "location": "Austin, TX",
        "email": "charlie@vannorman.ai",
        # "phone": "(650) 000-0000",
        # "phone_tel": "+16500000000",
        "linkedin": "https://www.linkedin.com/in/vannorman-ai",
        "github": "https://github.com/vannorman",
        "resume": "",
    }

    obj['badges'] = [
        "Full Stack Engineer",
        "Growth Hacker",
        "Product Designer",
    ]

    obj['filters'] = [
        {"key": "all", "label": "All"},
        {"key": "games", "label": "Games"},
        {"key": "ai", "label": "AI"},
        {"key": "edtech", "label": "Edtech"},
        {"key": "xr", "label": "XR / VR"},
        {"key": "training", "label": "Training sims"},
        {"key": "science", "label": "Science"},
        {"key": "robotics", "label": "Robotics"},
    ]

    obj['works'] = []
    obj['works'].append({
        "title": "StarCoach AI",
        "video": {"source": "https://player.vimeo.com/video/1220582758", "img": "sc_1.jpg"},
        "background": "mb_1.png",
        "link": "https://starcoach.ai",
        "date": "2025-2026",
        "position": "Interim CTO",
        "org": "",
        "subtitle": "An AI Powered Math Assessment Platform",
        "description": "An AI Powered Math Assessment Platform with district pilots, built on a multi-agent content and evaluation pipeline.",
        "responsibilities": [
            "Application architecture",
            "AI integration",
            "Multi-agent pipeline: content extraction, question generation, synthetic student agents, evaluator and validator/critic agents",
            "Agent orchestration layer routing tasks to agents and evaluation criteria, decoupled from business logic",
            "Led a team of 3; interviewed, hired, and trained 2 engineers",
        ],
        "images": [],
        "tags": ["ai", "edtech"],
        "stack": ["LLM agents", "Agent orchestration", "Web platform", "Express.js", "React"],
    })
    obj['works'].append({
        "title": "MathBreakers",
        "video": {"source": "https://player.vimeo.com/video/REPLACE", "img": "REPLACE.jpg"},
        "background": "",
        "link": "https://mathbreakers.com",
        "date": "2013-2017",
        "position": "Founder",
        "org": "",
        "subtitle": "3D math adventure game for Mac, PC, and iOS with a linear storyline for arithmetic, number line, and fractions.",
        "description": "",
        "responsibilities": [
            "Game design and development",
            "Classroom playtesting",
            "Shark Tank 1st Prize, 2013",
        ],
        "images": [],
        "tags": ["games", "edtech"],
        "stack": ["Unity3D","C#","python","Mac", "PC", "iOS"],
    })
    obj['works'].append({
        "title": "Super Math World",
        "video": {"source": "https://player.vimeo.com/video/REPLACE", "img": "REPLACE.jpg"},
        "background": "",
        "link": "",
        "date": "",
        "position": "Technical Co-founder",
        "org": "",
        "subtitle": "3D open world math learning game for Web Browsers, with level builder and teacher dashboard.",
        "description": "",
        "responsibilities": [
            "Open world game development",
            "Level builder",
            "Teacher dashboard",
        ],
        "images": [],
        "tags": ["games", "edtech"],
        "stack": ["WebGL", "ES6", "Node.js", "Next.js", "Apache"],
    })
    obj['works'].append({
        "title": "Enterprise Training",
        "video": {"source": "https://player.vimeo.com/video/REPLACE", "img": "REPLACE.jpg"},
        "background": "",
        "link": "",
        "date": "",
        "position": "Co-founder",
        "org": "Vantage Point VR",
        "subtitle": "Harassment training app with virtual cell phone and branching narrative for Oculus Rift.",
        "description": "",
        "responsibilities": [
            "Virtual cell phone interface",
            "Branching narrative system",
        ],
        "images": [],
        "tags": ["xr", "training"],
        "stack": ["Oculus Rift"],
    })
    obj['works'].append({
        "title": "Military Training",
        "video": {"source": "https://player.vimeo.com/video/REPLACE", "img": "REPLACE.jpg"},
        "background": "",
        "link": "",
        "date": "",
        "position": "Lead Developer",
        "org": "",
        "subtitle": "Virtual Air Strike simulator including weather control and several interactive military equipment pieces.",
        "description": "",
        "responsibilities": [
            "Weather control system",
            "Interactive military equipment",
        ],
        "images": [],
        "tags": ["xr", "training"],
        "stack": ["VR"],
    })
    obj['works'].append({
        "title": "Remote Control Robot",
        "video": {"source": "https://player.vimeo.com/video/REPLACE", "img": "REPLACE.jpg"},
        "background": "",
        "link": "",
        "date": "",
        "position": "Developer",
        "org": "",
        "subtitle": "Remote control industrial robot which can make toast, pour drinks, and pick junkyard metals.",
        "description": "",
        "responsibilities": [
            "Remote control interface",
            "Task programming: toast, drink pouring, junkyard metal picking",
        ],
        "images": [],
        "tags": ["robotics"],
        "stack": ["Industrial robotics"],
    })
    obj['works'].append({
        "title": "Molecular Machines",
        "video": {"source": "https://player.vimeo.com/video/REPLACE", "img": "REPLACE.jpg"},
        "background": "",
        "link": "",
        "date": "",
        "position": "Developer",
        "org": "",
        "subtitle": "Animated showcase including a modular catalyst synthesizer, controlled molecule flow, and energy storage.",
        "description": "",
        "responsibilities": [
            "Modular catalyst synthesizer",
            "Controlled molecule flow",
            "Energy storage animation",
        ],
        "images": [],
        "tags": ["science"],
        "stack": ["3D animation"],
    })
    obj['works'].append({
        "title": "Cellular Anatomy",
        "video": {"source": "https://player.vimeo.com/video/REPLACE", "img": "REPLACE.jpg"},
        "background": "",
        "link": "",
        "date": "",
        "position": "Developer",
        "org": "",
        "subtitle": "An immersive exploration of an animal cell with labeled organelles and structures.",
        "description": "",
        "responsibilities": [
            "Immersive cell environment",
            "Labeled organelles and structures",
        ],
        "images": [],
        "tags": ["science", "xr"],
        "stack": ["VR"],
    })
    obj['works'].append({
        "title": "Mouse Brain Explorer",
        "video": {"source": "https://player.vimeo.com/video/REPLACE", "img": "REPLACE.jpg"},
        "background": "",
        "link": "",
        "date": "2015",
        "position": "Developer",
        "org": "Exploratorium",
        "subtitle": "Immersive tour through a mouse brain with simulated Clopidogrel administration. Exploratorium exhibit 2015.",
        "description": "",
        "responsibilities": [
            "Immersive brain tour",
            "Simulated Clopidogrel administration",
            "Public museum exhibit",
        ],
        "images": [],
        "tags": ["science", "xr"],
        "stack": ["VR"],
    })
    obj['works'].append({
        "title": "VR Fitness",
        "video": {"source": "https://player.vimeo.com/video/REPLACE", "img": "REPLACE.jpg"},
        "background": "",
        "link": "",
        "date": "",
        "position": "Developer",
        "org": "",
        "subtitle": "Boxing / Dodging game that engages the player in motion throughout the full body as they rescue the Frog Princess.",
        "description": "",
        "responsibilities": [
            "Full-body boxing and dodging mechanics",
            "Frog Princess rescue narrative",
        ],
        "images": [],
        "tags": ["xr", "games"],
        "stack": ["VR"],
    })
    obj['works'].append({
        "title": "MathBreakers Relaunch",
        "video": {"source": "", "img": ""},
        "background": "",
        "link": "https://mathbreakers.com",
        "date": "2026",
        "position": "Founder & Technical Lead",
        "org": "Manaborn Studios LLC",
        "subtitle": "Browser-based 3D math game for grades 5-8, rebuilt in PlayCanvas with accounts, classrooms, and billing.",
        "description": "",
        "responsibilities": [
            "3D scene editor with transform gizmos and room editor",
            "Procedural mesh system with 25+ primitive types",
            "Portal rendering, cinematic director and cutscene runtime",
            "NavAgent AI, conveyor systems, terrain-aligned path meshes",
            "Ammo.js physics memory management, Mixamo animation layering, Vite ES6 migration",
            "Shared JWT auth across mathbreakers.com and game.mathbreakers.com",
            "Stripe checkout, GA4, Resend email campaigns, admin analytics dashboard",
            "Hired, trained, and manages a team of 4",
        ],
        "images": [],
        "tags": ["games", "edtech"],
        "stack": ["PlayCanvas", "Node.js", "Express", "MongoDB", "Ammo.js", "Vite", "Stripe", "DigitalOcean"],
    })
    obj['works'].append({
        "title": "VR Retail Training",
        "video": {"source": "", "img": ""},
        "background": "",
        "link": "",
        "date": "2019",
        "position": "Software Engineer",
        "org": "InContext Solutions",
        "subtitle": "Unity VR retail training platform.",
        "description": "",
        "responsibilities": [
            "Feature development as an individual contributor on an 8-person engineering team",
        ],
        "images": [],
        "tags": ["xr", "training"],
        "stack": ["Unity", "C#", "VR"],
    })
    obj['works'].append({
        "title": "XR Manufacturing Training",
        "video": {"source": "", "img": ""},
        "background": "",
        "link": "",
        "date": "",
        "position": "XR Consultant",
        "org": "SoftServe",
        "subtitle": "XR-enabled training program for a client's manufacturing facility.",
        "description": "",
        "responsibilities": [
            "XR training program delivery for a manufacturing client",
        ],
        "images": [],
        "tags": ["xr", "training"],
        "stack": ["XR"],
    })
    obj['works'].append({
        "title": "Magic Leap Engagement",
        "video": {"source": "", "img": ""},
        "background": "",
        "link": "",
        "date": "",
        "position": "XR Consultant",
        "org": "SoftServe",
        "subtitle": "XR development for Magic Leap as a SoftServe client.",
        "description": "",
        "responsibilities": [
            "XR development for client Magic Leap",
        ],
        "images": [],
        "tags": ["xr"],
        "stack": ["Magic Leap"],
    })

    obj['works'].append({
        "title" : "Code Hero",
        "video": {"source": "", "img": ""},
        "summary":"A 3D game to learn coding by editing the world around you in real time using a javascript laser."
        "description",
        "link" : "https://codehero.org",
        "year" : "2011",
        "position" : "Game Developer",
        "description" : "Designed and shipped the full game prototype, leading to a $160k successful KickStarter campaign.",
        "images" : [
            {"img":"codehero.png"},
        ], 
    })

    obj['experience'] = [
        {
            "org": "Manaborn Studios LLC",
            "role": "Founder & Technical Lead",
            "date": "2026 - present",
            "summary": "Relaunching MathBreakers as a browser-based 3D math platform for grades 5-8. Full-stack development, DevOps, and go-to-market. Manages a team of 4.",
        },
        {
            "org": "StarCoach AI",
            "role": "Interim CTO",
            "date": "Sep 2025 - Feb 2026",
            "summary": "Built an AI-powered math assessment platform with district pilots. Led a team of 3.",
        },
        {
            "org": "SoftServe",
            "role": "Consultant",
            "date": "",
            "summary": "XR delivery for Magic Leap and a manufacturing training client. Government client engagements with SOC 2 requirements.",
        },
        {
            "org": "InContext Solutions",
            "role": "Software Engineer",
            "date": "2019",
            "summary": "Unity VR retail training platform on an 8-person engineering team.",
        },
        {
            "org": "Vantage Point VR",
            "role": "Co-founder",
            "date": "",
            "summary": "Immersive VR workplace training.",
        },
        {
            "org": "Havik VR",
            "role": "XR venture",
            "date": "",
            "summary": "Immersive technology venture.",
        },
        {
            "org": "MathBreakers",
            "role": "Founder",
            "date": "2013 - 2017",
            "summary": "3D math adventure game for Mac, PC, and iOS. Shark Tank 1st Prize, 2013.",
        },
    ]

    obj['skills'] = [
        {
            "group": "Sales and Leadership",
            "items": ["Hiring and team leadership", "Marketing", "Metrics-driven growth", "Enterprise pre-sales", "MEDDPICC", "District sales",],
        },
        {
            "group": "Full-Stack Programming",
            "items": ["JavaScript (ES6)", "Node.js", "Express", "EJS", "MongoDB", "Vite", "JWT auth", "Stripe"],
        },
        {
            "group": "AI",
            "items": ["Agentic Workflows", "Retrieval-augmented generation (RAG)", "Multi-agent pipelines", "Agent orchestration", "Evaluator and critic agents", "AI/ML architecture"],
        },
        {
            "group": "Cloud and ops",
            "items": ["DigitalOcean", "AWS (SAA-C03 in progress)", "GA4", "Resend", "SOC 2 client work"],
        },
        {
            "group": "XR and 3D",
            "items": ["Unity", "Unreal Engine", "PlayCanvas", "ARKit", "Oculus / Meta", "Magic Leap", "Ammo.js physics", "Mixamo animation", "Procedural meshes"],
        },
    ]

    obj['about'] = [
        """I started builing educational software in 2010 with Code Hero, a game that reprograms itself while you play. Since then I've published 5 titles including MathBreakers, Santa's Last Stand, Bank Defense, SpaceFrogVR, and NumberSpark.
        As a co-founder, I've helped bring startups to funding or major growth events including VantagePoint, Havik, Humon Automation, and Primer Labs.""",
        "Between ventures, I've written music, traveled abroad, lived in Chile and Thailand, taught English in China, and started a <a target='_blank' href='https://manaretreat.center'>retreat center</a> in Puerto Rico.",
        "Today I'm producing MathBreakers 2, a browser-based 3D platform for grades 3-8 with a built-in user generated content platform. Check it out <a target='_blank' href='https://mathbreakers.com'>here</a>.",
    ]

    obj['facts'] = [
        {"label": "Education", "value": "B.S. Business, Cal Poly Pomona"},
        {"label": "Patents", "value": "U.S. 11,488,490, immersive VR training"},
        {"label": "Languages", "value": "English, Spanish, some Mandarin"},
        {"label": "Based in", "value": "Austin, Texas"},
    ]

    obj['blogs'] = []
    obj['blogs'].append({
        "title" : "Wealth, Abundance, and Homelessness", 
        "description" : "We already pay for homelessness. What if we're doing it wrong?",
        "link" : "https://vannorman-ai.medium.com/wealth-homelessness-and-abundance-eaa66558d2e4",
    })
    obj['blogs'].append({
        "title" : "A Tribute to Hans Rosling",
        "description" : "My homage to the statistician who changed the way I look at our world.",
        "link" : "https://medium.com/@vannorman-ai/a-tribute-to-hans-rosling-2674f16d43b6",
    })
    obj['blogs'].append({
        "title" : "Enterprise Pre-Sales Equation",
        "description" : "How to consider different factors and evaluate a potential enterprise b2b opportunity.",
        "link" : "https://vannorman.medium.com/the-presales-equation-ce39703974f8",
    })
    obj['blogs'].append({
        "title" : "How to Win Across Cultures",
        "description" : "A personal account of my experience as a Westerner working at a Ukrainian company.",
        "link" : "https://vannorman.medium.com/how-to-win-across-cultures-f2434983694a",
    })
    # return renderWithNav(request,'home.html', obj)
    
    return renderWithNav(request, "home.html", obj)
    

    

#   obj['works'].append({
#       "title" : "Admirals Multiplayer",
#       "background" : "",
#       "position" : "Developer, Game Designer",
#       "link" : "https://www.havik.us",
#       "date" : "2019",
#       "description" : "A multiplayer VR experience where you build and control a fleet of ships in space.",
#       "video" : { 
#           "source": "https://player.vimeo.com/video/362128849", 
#           "image" : "" 
#       },
#       "images" : [    
#       ],
#   })
    
#   obj['works'].append({
#       "title" : "Gamified AR mapping",
#       "background" : "mm_background.jpg",
#       "position" : "Consultant, Designer, Programmer",
#                "date" : "2018 Q3",
#       "link" : "http://vertical.ai/",
#       "description" : "PlaceNote is a platform for AR developers, many of whom need prefabs and techniques to get started for guiding the end user to optimal mapping behaviors. I wrote an extension to the PlaceNote SDK that includes prefabs for developers to help them achieve this.",
#       "video" : { 
#           "source": "https://player.vimeo.com/video/294704893", 
#           "image" : "mm_background.jpg" 
#       },
#       "images" : [    
#           {"img":"mm_1.jpg"},
#           {"img":"mm_2.jpg"},
#           {"img":"mm_3.jpg"},
#           {"img":"mm_4.jpg"},
#       ],
#   })

   
#   obj['works'].append({
#       "title" : "Village Builder",
#       "background" : "vb1.png",
#       "position" : "Developer, Designer",
#       "link" : "",
#       "year" : "2017",
#       "subtitle" : "",
#       "description" : "A LightLodges.com production for communal coherence, village building and sustainable communities. Precursor to a live Mixed Reality gameshow coming 2018", 
#       "video" : { "source": "https://player.vimeo.com/video/246606943", "image" : "vb1.png" },
#   
#       "images" : [    
#           {"img":"vb1.png"},
#           {"img":"vb2.png"},
#           {"img":"vb3.png"},
#           {"img":"vb4.png"},
#       ],  
#   })
  
#   obj['works'].append({
#       "title" : "Magic Hands",
#       "background" : "mm_background.jpg",
#       "position" : "Consultant, Designer, Programmer",
#       "link" : "http://vertical.ai/",
#       "description" : "Using Vive and Leap Motion, I built a prototype game that lets you portal between worlds, and recognizes hand gestures for casting magic spells.", 
#       "video" : { 
#           "source": "https://player.vimeo.com/video/294705016", 
#           "image" : "mm_background.jpg" 
#       },
#       "images" : [    
#           {"img":"mm_1.jpg"},
#           {"img":"mm_2.jpg"},
#           {"img":"mm_3.jpg"},
#           {"img":"mm_4.jpg"},
#       ],
#   })

#   obj['works'].append({
#       "title" : "Ring Flight",
#       "link" : "",
#       "year" : "2012",
#       "position" : "Developer",
#       "subtitle" : "Fly through rings",
#       "description" : "Made at a Kinect hackathon in 2012, this was my first experience integrating external hardware to a Unity game and capturing motion data as player input. In this game you fly through rings of different colors by tilting your body in the direction you wish to steer (lean forwards and backwards for pitch, left and right for yaw)",
#       "images" : [
#           
#       ],  
#   })  
    #   obj['works2'] = []
#   obj['works2'].append({
#       "title" : "Coffee Command ARKit",
#       "position" : "Developer/Designer",
#       "link" : "",
#       "year" : "2017",
#       "subtitle" : "A passive multiplayer base control game",
#       "description" : "Your phone becomes a ship which can attack bases and drones at your favorite coffee shop in a 3-D shooter style game. Once you clear the area, you can build your own turrets to deter other players and control the area, and mine resources from areas you control to become more powerful.",
#       "images" : [
#           {"img":"coffeecommand1.png"},
#           {"img":"coffeecommand2.png"},
#           {"img":"coffeecommand3.png"},
#       ],  
#   })
#   obj['works2'].append({
#       "title" : "Magic Hands VR",
#       "position" : "Developer/Designer",
#       "link" : "",
#       "year" : "2017",
#       "subtitle" : "An action game for Vive/Oculus + LeapMotion",
#       "description" : "Use your hands to cast spells and open portals to other worlds.",
#       "images" : [    
#           {"video" : { "source": "https://player.vimeo.com/video/241614660", "image" : "" }},
#           {"img":"magichands1.png"},
#           {"img":"magichands2.png"}
#       ],  
#   })
#   obj['works2'].append({
#       "title" : "Space Archer VR",
#       "position" : "Developer/Designer",
#       "link" : "",
#       "year" : "2017",
#       "subtitle" : "An action game for Vive/Oculus",
#       "description" : "Fly around in 3D space and shoot drones and space-men with your bow and arrow.",
#       "images" : [    
#           {"video" : { "source": "https://player.vimeo.com/video/230824116", "image" : "" }},
#           {"img":"archer2.png"},
#           {"img":"archer1.png"}
#       ],  
#   })
#   obj['works'].append({
#       "title" : "Fitness Cube VR",
#       "link" : "",
#       "year" : "2017",
#       "subtitle" : "An exercise game for Vive/Oculus",
#       "description" : "Cubes fly at you, and you smash them with your fists! Duck and dodge to prevent losing health.",
#       "images" : [
#           {"video" : { "source": "https://player.vimeo.com/video/230823053", "img" : "fitness2.png" }},
#           {"img":"fitness1.png"},
#       ],  
#   })

#   obj['works2'].append({
#       "title" : "Radian.ai",
#       "link" : "http://radian.ai",
#       "year" : "2017",
#       "position" : "Consultant",
#       "description" : "Consulting for VR and AR applications, including project management, enterprise sales, experience design, and full stack development. ",
#       "responsibilities" : 
#       [
#       ],
#       "images" : [
#           { "img" : "radian_logo.png", "class" : "contain square", "link" : "http://radian.ai"},
#       ],  
#   })
#   obj['works'].append({
#       "title" : "Fractal Games",
#       "link" : "https://fractalgames.com (old)",
#       "year" : "2010 - 2011",
#       "position" : "Founder",
#       "subtitle" : "An iOS game development studio.",
#       "description" : "I led a small team of developers and artists to design and publish two titles, \"Santa's Last Stand\" and \"Bank Defense\" for iOS." ,
#       "responsibilities" : 
#       [
#           "Game design & programming",
#           "Hired and managed art team",
#       ],
#       "images" : [    
#           {"img": "fg.png","class":"contain"},
#           {"img" : "bd1.png"},
#           {"img" : "bd2.png"},
#           {"img" : "bd3.png"},
#           {"img" : "sls1.png"},
#           {"img" : "sls2.png"}
#           ],  
#       })
#   obj['works'].append({
#       "title" : "Startup Grid (Hactus)",
#       "link" : "https://startupgrid.net",
#       "year" : "2012",
#       "position" : "Founder",
#       "description" : "One of my first solo projects, a search-and-filter website for exploring the startup landscape and searching for new opportunities. The startup data is scraped from CrunchBase. The original vision was to provide startups a go-to resource for funding, incubators, and other opportunities.",
#       "images" : [{"img":'startupgrid.png', "link":"http://startupgrid.net"}],    
#       })
                    
#   obj['social'] = [
#       { "name" : "github.com/vannorman", "link" : "https://github.com/vannorman" },
#       { "name" : "linkedin.com/in/vannorman", "link" : "https://www.linkedin.com/in/vannorman" },
#       { "name" : "facebook.com/vannorman", "link" : "https://www.facebook.com/vannorman" },
#       { "name" : "twitter.com/@vannorman", "link" : "https://twitter.com/@vannorman" },
#       { "name" : "angel.co/supermathworld", "link" : "https://angel.co/supermathworld" },
#       { "name" : "soundcloud.com/vannorman", "link" : "https://soundcloud.com/vannorman" },
#   ]
   

    obj['blogs'] = []
    obj['blogs'].append({
        "title" : "Wealth, Abundance, and Homelessness", 
        "description" : "We already pay for homelessness. What if we're doing it wrong?",
        "link" : "https://vannorman-ai.medium.com/wealth-homelessness-and-abundance-eaa66558d2e4",
    })
    obj['blogs'].append({
        "title" : "A Tribute to Hans Rosling",
        "description" : "My homage to the statistician who changed the way I look at our world.",
        "link" : "https://medium.com/@vannorman-ai/a-tribute-to-hans-rosling-2674f16d43b6",
    })
    obj['blogs'].append({
        "title" : "Enterprise Pre-Sales Equation",
        "description" : "How to consider different factors and evaluate a potential enterprise b2b opportunity.",
        "link" : "https://vannorman.medium.com/the-presales-equation-ce39703974f8",
    })
    obj['blogs'].append({
        "title" : "How to Win Across Cultures",
        "description" : "A personal account of my experience as a Westerner working at a Ukrainian company.",
        "link" : "https://vannorman.medium.com/how-to-win-across-cultures-f2434983694a",
    })
    return renderWithNav(request,'home.html', obj)

def file_a(request):
    return HttpResponse("7GN_wPd4X1PrCxmqKOrw9sHsAd0_uayFhOnWdEw6Ytc.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")

def file_b(request):
    return HttpResponse("Z9DF236bXRfXjvGlUflaI98PMWAKsG9qpGnrDXllb2o.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")  


def test(request):
    return renderWithNav(request,"test.html", {})

