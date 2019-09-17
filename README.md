
# Assignment 1 - Designing Models and Analyzing Data (Template)
(remove: **text between brackets to be removed**)

> * Participant name: Bradley 'Austin' Kriznar
> * Project Title: SUBWAY MODEL ANALYSIS

# General Introduction

The first part of this assignment explores designing models (and basic Python/Git features). 

We will look at **subway model in a city** system. A **subway system** is an underground, tube, or metro, underground railway system used to transport large numbers of passengers within urban and suburban areas - modern subways use different types of electronic data collection sensors to supply information which is used to manage assets and resources efficiently. 

The second part of the assignment explores data analysis. Data analysis and visualization is key to both the input and output of simulations. This assignment explores different random number generators, distributions, visualizations, and statistics. Additionally, it will look at getting you accustomed to specifying input and output variables to a system. We will also practice working with real data.


# Part 1: Designing a Model - Subway System
Subway transportation is incredibly important for many metroplitian areas. It is magnitudes of order more effective for traffic mitigation than individuals using cars in their commutes, and so making sure existing subways queue / run efficiently is certianly a worthy priority for city planners.   

(remove: States your motivation clearly: why is it important / interesting to solve this problem?)
There are a large number of examples of these kinds of queues. In London, the Underground logs up to 5 million journeys a day. The majority of passengers must enter the Underground via escalator tunnels, especially in the dowtown area. Ensuring appropriete passenger safety entering and exiting the subway is important for smooth operation, balanced with speed (it would make no sense to have escalators when they are slower than just taking the stairs). 
(remove: Add real-world examples, if any)

(remove: Put the problem into a historical context, from what does it originate? Are there already some proposed solutions?)


![Image of Subway City System](images/subway_model.png)

## (Part 1.1): Requirements (Experimental Design) **(10%)**

(remove: You should start by specifying a set of requirements. I specified a topic a Subway escalator. What exactly does that mean - practice formulating your own set of requirements and an experiment. Define problems cities face and hypothesize how a subway system could help alleviate these issue. This helps you think about your problem communication and system objectives inputs, functions, and outputs - they should be clearly specified.)

The system **shall [01]** model subway entrance and exit escalators.

The system **shall [02]** model an escalator compliant with ASME A17.1-2007/CSA B44-07, Safety Code for Elevators and Escalators, Part 6 Escalators and Moving Walks. 

The system **shall [03]** have step deck of length between 22 in. and 40 in.

The system **shall [04]** have step run of no less than 15.75 in. 

The system **shall [05]** have step rise of no more than 8.5 in.  

The system **shall [06]** model escalator incline at an angle of no greater than 30 degrees.

The system **shall [07]** model belt speed not exceeding 100 ft / min.

The system **shall [08]** model assume a constant belt speed.



## (Part 1.2) Subway (My Problem) Model **(10%)**

(remove: add a high-level overview of your model, the part below should link to the model directory markdown files)
(remove: Look at the [**Object Diagram**](model/object_diagram.md) for how to structure this part of Part 2 for each diagram. Only the Object diagram has the template, the rest are blank. )

* [**Object Diagram**](model/object_diagram.md) - provides the high level overview of components
* [**Class Diagram**](model/class_diagram.md) - provides details of (what are you providing details of)
* [**Behavior Diagram**](model/behavior_diagram.md) - provides details of (what are you providing details of)
* [**Agent / User case** (if appropriate)](model/agent_usecase_diagram.md) - provides details of (what are you providing details of)

## (Part 1.3) Subway (My Problem) Simulation **(10%)**

(remove: Describe how you would simulate this - including type of simulation, rough details, inputs, outputs, and how it will help you analyze your experimental hypothesis, or nullify your null hypothesis.)

## (Part 1.4) Subway City (My Problem) Model **(10%)**
[**Code template**](code/README.md) - Starting coding framework for the (insert your exact problem here.)
You are expected to create the python files - the code should run without errors, create and object(s) for your system, but not provide function detail.



## (Part 1.5) Specifying the Inputs to a System **(10%)**
* Specify the independent and dependent input variables of your subway escalator model
Independent Variables – 
* The **escalator step dimensions** are fixed and required to be a fixed size.
* The **escalator belt speed** is assumed to be fixed. The number of people on the escalator does not have an effect on its speed as the real system is highly standardized. 
* The **maximum step capacity** is assumed to be independent as we do not believe the escalator will change length, as with real life.
Dependent Variables-
* The **person arrival rate, lambda** is dependent on the time of day. This is based on the idea subways are likely used more at different times – we may expect that ridership (and thus escalator usage) is tied to when people are coming and going to work.
* The **person size** is dependent on a few factors, including if they are a child (likely to be smaller and take only a single escalator step) or an adult (likely to be larger and may take a few steps up).
* The **escalator queue entrance availability** is dependent on the number of people currently on the escalator. If the escalator is at a full steady-state, then a line will begin to form to get onto the escalator (assuming people are standing single-abreast). 

* Specify where the data will come from measured subset of real data (empirical) or synthetic data
Ideally, direct sampling to collect real data would be done use as the base of the simulation data. That is not really likely. Luckily, a few quick searches on Google provide large set of real turnstile / usage data directly from the (Metropolitan Transportation Authority)[ http://web.mta.info/developers/download.html]. While turnstile data does not directly map onto escalator use in subways, it could be a great starting point. 
* What kind of statistics are important to capture this input data
I think it would be important to capture basic descriptive statistics for arrival rates, escalator belt speed / size, and usage information as related to time of day / day of week.  
* How do you plan to analyze the output of your model?
It would be useful to determine and analyze what the queue length waiting to enter the escalator is on average (average wait time). That is probably the most productive question to get an answer for, especially if in a very-high traffic station such as Times Square. 
* What ways will you visualize your data - charts, and graphs you will create?
A line graph depicting average escalator wait time across a day, with each day represented as a separate line, could be a clear way to visualize traffic variability. It may also be interesting to see usage or non-usage data that is subway station dependent (are there escalators that cost more to operate in maintenance costs and electricity than is covered by the local ridership fare?). 
* What clever way will you visualize your output with a useful infographic?


# Part 2: Creating a Model from Code

## (Part 2.1) **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model **(10%)**
Here [**we provide an overview**](code/POTS_system/README.md) of the **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model and provide a source code template for the code found in  [**the following folder**](code/POTS_system/). Please create a **class** diagram of this model (replace the placeholder diagram). (you can use paper and pencil or a digital tool).



# Part 3: Data Analysis

## (Part 3.1) - Real Data **(10%)**

Find a datasource that looks at part of this model - subway stations locations / escalator number, heights, widths / volume of passangers - ridership numbers   (*fits* - we are pretty loose here, it can be anything.)

* Write up a paragraph that describes the data and how it fits into your system.
* Load the data into Python
* Calculate a few useful statistic on the data - keep it simple- STD, means, etc..., this is just designed * to get used to working with real data. Explain the insights you derive from these statistics.
* Visualize the raw data - visualize a few critical aspects of the data to better describe what it is, what it is showing, and why its useful to your system.
* Calculate and plot some summary statistics that better describe the data.

(Add your plots and visualization here)
(Put your data into the data directory)


## (Part 3.2) -  Plotting 2D Random Number Generators **(15%)**

This portion of the assignment looks at generating random numbers in Python and understanding how to properly plot them. Plot two different random numbers, pseudo random and quasi random, for five different N values. There should be 10 subplots, all properly formatted 2D plots. Note, each of the N points will have two coordinates, an x and a y, therefore you will need to generate two random numbers for each point. You should replace the image with your results in a simalar format. Discuss how the patterns differ. Feel free to change the N values from the suggested N values in the image to state your case.

![Image of 2d template City](images/2Dtemplate.png)


## (Part 3.3) -  Plotting 1D Random Distributions **(15%)**

Now, choose three different distributions to plot in 1D, or as a histogram. Choose a pseudo-random generator and generate three different distributions. Example distributions are Uniform (part 8), Normal, Exponential, Poisson, and Chi-Squared, but feel free to use any three distributions of your choice. Again, plot each distribution for five different Ns. This will result in 15 different subplots, formatted similar to the image in Part 8. Include your properly formmated 1D plots below and breifly describe what we are looking at and how things change as N is changed.

Repeat the above using a quasi-random generator. Discuss the similarities and differences.
